# 🧠 Formzy — AI-Powered Form Generator with Ollama LLM

**Formzy** is an intelligent form generation tool powered by Ollama LLM. It allows users to generate fully functional HTML forms by simply describing them in natural language. Built with Python and Flask, it offers a modern UI using HTML, CSS, and JavaScript.

---

## 🚀 Features

- 🤖 **Form Generation via Ollama LLM**  
  Generate custom forms from prompts like “Create a registration form with name, email, and password.”

- 🌐 **Python + Flask Backend**  
  Lightweight and fast backend for processing requests and serving templates.

- 🎨 **Responsive Web UI**  
  Clean and interactive frontend built with HTML5, CSS3, and vanilla JavaScript.

- 💾 **Form History and Submission Logs**  
  Every generated form and submission is stored as structured JSON for review and reuse.

---

## 🛠️ Technologies Used

- Python 3.10+
- Flask
- Ollama (local LLM)
- HTML5 / CSS3 / JavaScript
- JSON for data handling and logging

---

## 📁 Folder Structure

backend/
│
├── appy.py # Main Flask app entry point
├── form_templates/ # Predefined prompt-based templates
├── forms/ # Auto-generated HTML forms
├── json_submissions/ # Form submissions saved as JSON
├── static/ # Static assets (CSS, JS, images)
├── submissions/ # HTML format user submissions
├── templates/ # Flask HTML templates
│
├── chat_history.json # Ollama interaction logs
├── memory.json # Persistent memory state
├── form_log.json # Individual form logs
├── form_logs.json # Aggregated log entries



---

## 💡 How It Works

1. **Prompt Input:**  
   User gives a natural language request like _“Generate a feedback form with rating and comments.”_

2. **Ollama LLM Response:**  
   The system sends the prompt to the Ollama language model and receives structured instructions or raw HTML.

3. **Form Builder Engine:**  
   Formzy parses the response and constructs the HTML form, saving it for reuse.

4. **UI Rendering:**  
   The generated form is shown via Flask + HTML, ready for real user input.

5. **Submission Logging:**  
   Responses are saved both as raw HTML and JSON files for analysis or reuse.

---

## 📷 Screenshots

### 🧾 Formzy Web UI
![Form Screenshot](screenshots/form_ui_example.png)

### 🧠 Prompt-to-Form Flow
![Prompt Flow](screenshots/.png)



---

## 🔗 Project Links

- 🔗 [View on GitHub](https://github.com/codeby-vicky/Formzy)
- 💼 [Connect on LinkedIn](https://www.linkedin.com/in/vignesh-m-n-3b5282270?)

---

## ⚙️ Setup Instructions

### 1. Install Requirements
```bash
pip install flask
````

### 2. Run the Application

```bash
python appy.py
```

### 3. Open in Browser

```
http://localhost:5000/
```

> Make sure your Ollama LLM instance is running locally or connected properly.
```
