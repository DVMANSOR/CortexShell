# CortexShell
CortexShell is a Windows AI assistant powered by OpenAI GPT-4.1 that can chat, automate tasks, and execute PowerShell commands directly on your system. Fully customizable with personas and command rules, it offers powerful system control — but use with caution, as it has full access to your PC.

# ⚡ Windows AI Assistant — Chat & Control Your PC with PowerShell

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Python](https://img.shields.io/badge/python-3.9%2B-blue)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)
[![OpenAI Powered](https://img.shields.io/badge/OpenAI-GPT--4.1-brightgreen)](https://openai.com/)

**Your PC, your rules — a powerful AI assistant that can chat, automate, and run PowerShell commands directly on Windows.**

---

## ✨ Features
- 🖥 **System Detection** — Auto-detects Windows & PowerShell versions.
- 🤖 **AI Brain** — Powered by OpenAI GPT-4.1 or compatible endpoints.
- 🗂 **Customizable Persona** — Control AI behavior via config files.
- 📝 **Persistent Memory** — Keeps logs of all conversations.
- ⚙ **Command Execution** — Direct PowerShell control.

---
## 🔧 Installation
1. **Clone this repo**
   ```bash
   git clone https://github.com/yourusername/windows-ai-assistant.git
   cd windows-ai-assistant
2. **Install dependencies**
   ```bash
   pip install openai
3. **Prepare assets folder**
   Create assets/token.txt with your OpenAI-compatible API key.
   Edit assets/command.txt and assets/persona.txt to customize AI behavior.
## 🚀 Usage

Run the script:
  ```bash
  python main.py
  ```
Then type your request:
```bash
> list all running processes
Sure I will list the running processes for you
@&
Get-Process
```
## ⚠ Disclaimer
This program **executes arbitrary PowerShell commands**.
Malicious prompts could damage your system.
Use **only** in secure, controlled environments.
The author assumes **no responsibility** for misuse or damage.
