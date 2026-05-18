#  AI-Powered Study Assistant Chatbot

> **Hackathon Project** | Theme: *AI Agents Unleashed – Building the Future of Automation*

An intelligent conversational chatbot that helps university students study smarter — explaining concepts, summarizing notes, and providing personalized guidance using AI.

---

##  Features

-  **Chat Interface** — Clean, ChatGPT-style conversation UI
-  **Conversation Memory** — Remembers the last 5 messages for context-aware replies
-  **Notes Summarizer** — Paste lecture notes and get a bullet-point summary instantly
-  **Study-Focused AI** — System-prompted to explain concepts simply and encouragingly
-  **Secure API Key Input** — Enter your key in the sidebar (never stored)
-  **Clear Chat** — Reset conversation history with one click

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Python 3.10+ |
| AI Model | OpenAI GPT-3.5-Turbo |
| Memory | Streamlit Session State |
| Deployment | Localhost / Streamlit Cloud |

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/ai-study-assistant.git
cd ai-study-assistant
```

### 2. Create and activate a virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up your API key
```bash
cp .env.example .env
# Open .env and replace with your real OpenAI API key
```

### 5. Run the app
```bash
streamlit run app.py
```

The app opens at **http://localhost:8501** in your browser.

---



##  Example Prompts

- *"Explain Object-Oriented Programming in simple terms"*
- *"What is the difference between RAM and ROM?"*
- *"Give me 5 study tips for memorizing formulas"*
- *"Summarize the water cycle in 3 bullet points"*

---

##  Security Note

Your API key is entered in the sidebar and used only for that session. It is **never stored** in code or files. Make sure your `.env` file is listed in `.gitignore` before pushing to GitHub.

---

##  Author

Built with ❤️ for the university hackathon.

---

##  License

MIT License — free to use and modify.
"# NEURO-STUDY-AI" 
"# NEURO-STUDY-AI" 
