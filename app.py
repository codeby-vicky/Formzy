from flask import Flask, request, jsonify, send_from_directory, render_template_string
import ollama
import os
import json
import uuid
import time
import re
import psutil
from duckduckgo_search import DDGS

app = Flask(__name__)
FORM_FOLDER = os.path.join(os.getcwd(), 'forms')
os.makedirs(FORM_FOLDER, exist_ok=True)

MEMORY_FILE = "memory.json"
CHAT_HISTORY_FILE = "chat_history.json"
FORM_LOG_FILE = "form_logs.json"

def load_json(filename):
    return json.load(open(filename)) if os.path.exists(filename) else []

def save_json(filename, data):
    json.dump(data, open(filename, "w"), indent=2)

def load_memory(): return load_json(MEMORY_FILE)
def save_memory(memory): save_json(MEMORY_FILE, memory)

def load_chat_history(): return load_json(CHAT_HISTORY_FILE)
def save_chat_history(history): save_json(CHAT_HISTORY_FILE, history)

def load_form_logs(): return load_json(FORM_LOG_FILE)
def save_form_logs(logs): save_json(FORM_LOG_FILE, logs)

def search_web(query):
    results = []
    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=5):
            results.append(r['body'])
    return "\n".join(results)

def has_enough_memory(required_gb=3.2):
    available_gb = psutil.virtual_memory().available / (1024 ** 3)
    return available_gb >= required_gb

def ask_llama(prompt, model="llama3"):
    try:
        if not has_enough_memory():
            return "❌ Not enough system memory to run the model. Please close background apps or try a smaller model."
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        return response['message']['content']
    except Exception as e:
        return f"❌ Error generating response: {str(e)}"

def update_memory(user_input, memory):
    if "my name is" in user_input.lower():
        memory["name"] = user_input.split("my name is")[-1].strip().split()[0]
    return memory

def enhance_prompt(user_input):
    lower = user_input.lower()
    if "leave" in lower:
        return "Generate a professional leave form using TailwindCSS with full name, employee ID, leave type, start/end date, reason, and signature."
    elif "certificate" in lower:
        return "Create a certificate request form with TailwindCSS, asking for full name, student ID, course, semester, reason, and contact info."
    elif "register" in lower:
        return "Build a user registration form using TailwindCSS with name, email, phone, gender, address, password, and confirmation."
    else:
        return f"Generate a detailed TailwindCSS form for: {user_input}"

def create_form_from_prompt(prompt):
    heading = "Generated Form"
    if not has_enough_memory():
        return "❌ Your system does not have enough memory to generate the form."

    try:
        response = ollama.chat(
            model='codellama',  # ✅ Use a valid model name you have pulled
            messages=[
                {"role": "system", "content": "You are a creative form generator. Return only the <form> element using TailwindCSS with appropriate fields, labels, and submit button."},
                {"role": "user", "content": prompt}
            ]
        )
        form_html = response['message']['content']
    except Exception as e:
        return f"❌ Error while generating form: {str(e)}"

    if '<button' not in form_html.lower():
        form_html += '\n<button type="submit" class="mt-4 bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">Submit</button>'

    form_id = str(uuid.uuid4())[:8]
    file_name = f"form_{form_id}.html"
    file_path = os.path.join(FORM_FOLDER, file_name)

    full_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>{heading}</title>
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-gradient-to-r from-blue-100 via-purple-100 to-pink-100 min-h-screen flex items-center justify-center p-4">
  <div class="bg-white/80 backdrop-blur-lg shadow-2xl rounded-3xl p-10 w-full max-w-2xl transition-transform hover:scale-[1.01]">
    <h1 class="text-3xl font-extrabold text-center text-gray-800 mb-6">{heading} 📝</h1>
    <div class="space-y-6 text-gray-700">
      {form_html}
    </div>
    <div class="mt-8 text-right">
      <button onclick="downloadForm()" class="bg-gradient-to-r from-blue-600 to-purple-600 text-white px-6 py-3 rounded-full shadow-lg hover:from-purple-700 hover:to-pink-600 transition duration-300">📥 Download Form</button>
    </div>
  </div>
  <script>
    function downloadForm() {{
      const blob = new Blob([document.documentElement.outerHTML], {{type: 'text/html'}});
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = '{file_name}';
      a.click();
      URL.revokeObjectURL(url);
    }}
  </script>
</body>
</html>
"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(full_html)

    return f"http://localhost:5000/forms/{file_name}"

@app.route("/")
def home():
    return "<h2>AI Form Generator</h2><p>Use terminal to request forms.</p>"

@app.route("/forms/<filename>")
def serve_form(filename):
    return send_from_directory(FORM_FOLDER, filename)

@app.route("/submit", methods=["POST"])
def handle_submit():
    submitted_data = request.form.to_dict()
    file_data = {k: v.filename for k, v in request.files.items() if v.filename}
    html = f"""
    <html><head><script src='https://cdn.tailwindcss.com'></script></head>
    <body class='p-6 bg-green-100'>
    <div class='bg-white p-4 rounded shadow max-w-xl mx-auto'>
      <h2 class='text-xl font-bold mb-2'>Form Submitted Successfully!</h2>
      <h3 class='font-semibold'>Data Received:</h3>
      <pre class='bg-gray-100 p-2 rounded'>{json.dumps(submitted_data | file_data, indent=2)}</pre>
    </div>
    </body></html>
    """
    return html

def chat():
    memory = load_memory()
    chat_history = load_chat_history()

    print("🤖 Hello! I'm your AI Form Generator.\nType 'exit' to quit. Type 'history' to view past chats.\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        elif user_input.lower() == "history":
            print("\n--- Chat History ---")
            for i, entry in enumerate(chat_history[-10:], 1):
                print(f"{i}. You: {entry['user']}\n   AI: {entry['ai']}\n")
            continue

        memory = update_memory(user_input, memory)
        save_memory(memory)

        if "form" in user_input.lower():
            print("[Info] Generating form based on user request...")
            enhanced = enhance_prompt(user_input)
            link = create_form_from_prompt(enhanced)
            reply = f"✅ Your form is ready! Click the link below:\n{link}"
        else:
            prompt = f"You are a helpful assistant. Here's user memory: {json.dumps(memory)}.\nUser says: {user_input}"
            reply = ask_llama(prompt)

        print(f"AI: {reply}\n")
        chat_history.append({"user": user_input, "ai": reply})
        save_chat_history(chat_history)
        time.sleep(0.5)

if __name__ == '__main__':
    import threading
    threading.Thread(target=lambda: app.run(debug=False, use_reloader=False)).start()
    time.sleep(1)
    chat()
