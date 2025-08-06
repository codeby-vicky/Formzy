Absolutely, Vicky! Below is the **full `README.md` content** for your project **Formzy** — complete with pip installs, Ollama setup, and everything in a **copy-paste** ready format:

---

```markdown
# 🧾 Formzy

**Formzy** is an AI-powered smart form generator that uses **LLM models through Ollama** to dynamically generate forms based on user prompts. Built using **Python + Flask** on the backend and **HTML/CSS/JS** on the frontend, this tool helps automate surveys, feedback forms, and other custom form creation workflows with just a single prompt.

---

## 🚀 Features

- ✅ Auto-generate HTML forms from natural language prompts using Ollama LLM
- 🌐 Clean frontend UI with Flask templating
- 📩 Form submissions saved in JSON format
- 🧠 Stores chat history and form logic for audit/tracking
- 🖥️ Works fully offline with local LLM (via Ollama)

---

## 📁 Folder Structure

```

Formzy/
│
├── appy.py                 # Main Flask backend app
├── form\_templates/         # LLM-generated form structure files (JSON)
├── forms/                  # Stored HTML forms
├── json\_submissions/       # Form responses (JSON format)
├── static/                 # Static files: CSS, JS, images
├── submissions/            # Raw submissions or exports (CSV, TXT)
├── templates/              # Jinja2 templates (Flask rendering)
│
├── chat\_history.json       # Logs conversation with LLM
├── form\_log.json           # Log for generated forms
├── form\_logs.json          # Backup logs or alternate tracking
├── memory.json             # Stores persistent memory context

````

---

## 🛠️ Installation Guide

### 1. Clone the Repository

```bash
git clone https://github.com/codeby-vicky/Formzy.git
cd Formzy
````

### 2. Create Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
```

### 3. Install Python Requirements

```bash
pip install flask
pip install flask-cors
pip install requests
pip install python-dotenv
```

---

## 🧠 Ollama LLM Setup (Optional but Powerful)

Formzy uses [**Ollama**](https://ollama.com) to generate form structures via local LLMs like LLaMA3 or Mistral.

### 🔹 Install Ollama

👉 [Download Ollama](https://ollama.com/download) for your OS and install it.

Or via terminal (macOS/Linux with Homebrew):

```bash
brew install ollama
```

### 🔹 Start Ollama and Load a Model

```bash
ollama run mistral
```

> Make sure Ollama is running before you start Formzy for AI functionality to work.

---

## ▶️ Run the Flask App

```bash
python appy.py
```

Then open your browser:

```
http://127.0.0.1:5000/
```

You’re now live!

---

## 📸 Screenshots
[!screenshots] (screenshots/Picture1.png)


### 🔻 Project Folder Structure

![Project Structure](./8ff0bcd0-a7f4-45f8-b7d7-604e880920e0.png)


---

## 🔗 Connect With Me

* 👨‍💼 **LinkedIn**: [Vicky’s LinkedIn](https://www.linkedin.com/in/codeby-vicky)
* 💻 **GitHub**: [Formzy on GitHub](https://github.com/codeby-vicky/Formzy)

---

## 💡 Future Roadmap

* [ ] Drag-and-drop visual form builder
* [ ] Export to Excel / Google Sheets
* [ ] Admin dashboard for form analysis
* [ ] Authentication and user roles

---

## 📃 License

This project is licensed under the **MIT License**.

---

