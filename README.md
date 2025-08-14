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
   ```
2. **Install dependencies**
   ```bash
   pip install openai
   ```
3. **Prepare assets folder**
   Create assets/token.txt with your Github-compatible Token.
   Edit assets/command.txt and assets/persona.txt to customize AI behavior.
---
## 📝 Notes
This project uses the GitHub Marketplace for AI.
The assets/token.txt file should contain your GitHub token to authenticate requests.
Treat your token as sensitive — never share it publicly.
---
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
---
## ⚠ Disclaimer
This program **executes arbitrary PowerShell commands**.
Malicious prompts could damage your system.
Use **only** in secure, controlled environments.
The author assumes **no responsibility** for misuse or damage.

## 🤝 Contributing & Support

Got an idea to improve **CortexShell**? Found a bug? Need help using it?  
Here’s how you can contribute:

- **Open an Issue** — Report bugs or request features.
- **Submit a Pull Request** — Add improvements or fix problems.
- **Suggest Ideas** — Share your thoughts in the Discussions tab.
- **Collaborate** — I’m open to working together on expanding this project.

Your feedback and ideas are always welcome! 🚀


---
## 📜 License (MIT)
MIT License

Copyright (c) 2025 Mansour

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
---

🔥 **Pro Tip:** Star ⭐ this repo if you find it useful — it helps more people discover it!
