<div align="center">

# 🤖 Gemini CLI Assistant

**A terminal-based AI assistant powered by the Gemini API.**

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Gemini](https://img.shields.io/badge/Gemini%20API-8E75B2?style=for-the-badge&logo=google&logoColor=white)

![Status](https://img.shields.io/badge/status-complete-22c55e?style=flat-square)
![Phase](https://img.shields.io/badge/Phase%203-LLM%20%26%20RAG%20Core%20Day%2017-3b82f6?style=flat-square)

</div>

---

## 📖 Overview

A simple command-line chat assistant that sends your messages to Google's Gemini API and prints the response — with conversation memory across turns and graceful handling of common API errors (bad key, rate limits, server downtime, no internet).

---

## ✨ Features

- 💬 Accepts input directly from the terminal in a loop
- 🔗 Sends each prompt to the Gemini API (`gemini-2.5-flash`)
- 🧠 Keeps a rolling conversation history so follow-up questions have context
- ⚠️ Handles errors gracefully — invalid API key, rate limits, server outages, and connection issues all print a clear message instead of crashing
- 🚪 Exit anytime by typing `exit`, `quit`, or pressing Enter on an empty line

---

## 🔑 API Setup

1. Get a free Gemini API key from **[Google AI Studio](https://aistudio.google.com/apikey)**.
2. Set it as an environment variable named `GEMINI_API_KEY`:

```bash
# macOS / Linux
export GEMINI_API_KEY="your-key-here"

# Windows (PowerShell)
setx GEMINI_API_KEY "your-key-here"
```

Or copy `.env.example` to `.env` and fill in your key if you're using a tool like `python-dotenv` to load it — this project reads it via `os.environ`, so any method that sets the variable in your shell works.

**Never commit your real API key to GitHub.** `.env.example` is a template only — add `.env` to `.gitignore` if you create one.

---

## ⚙️ Required Environment Variables

| Variable | Description |
|---|---|
| `GEMINI_API_KEY` | Your Gemini API key from Google AI Studio. Required — the app exits with setup instructions if it's missing. |

---

## ▶️ Setup & Run

```bash
git clone https://github.com/atharva-9423/unprof.git
cd unprof/day-17

pip install -r requirements.txt
$env:GEMINI_API_KEY="your-actual-api-key-here"

python assistant.py
```

---

## 🧪 Example Session

```
==================================================
  🤖  Gemini CLI Assistant
  Type your message and press Enter.
  Type 'exit' or press Enter on empty input to quit.
==================================================

You: What's a good way to learn Python quickly?
Gemini: Build small real projects early — a to-do app, a simple
scraper, a calculator — rather than only reading theory...

You: exit
👋 Goodbye!
```

---

## ⚠️ Error Handling

| Situation | What happens |
|---|---|
| `GEMINI_API_KEY` not set | Prints setup instructions and exits immediately, before making any request |
| Invalid API key / bad request (4xx) | Caught as `ClientError` — prints the status code and a clear message, loop continues |
| Gemini API outage (5xx) | Caught as `ServerError` — tells you to try again shortly, loop continues |
| No internet / connection failure | Caught as a generic exception — tells you to check your connection, loop continues |

The assistant never crashes on an API failure — every error is caught, explained, and the conversation loop keeps running so you can try again.

---

## 📁 Project Structure

```
day-17/
├── assistant.py       # main CLI app
├── requirements.txt
├── .env.example         # template for the required API key
└── README.md
```

---

<div align="center">

Built during **Phase 3 – LLM & RAG Core**, Day 17: *LLM API Basics*

</div>
