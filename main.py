from openai import OpenAI
import subprocess
import platform
import os

with open("./assets/token.txt", "r") as f:
    token = f.read()

endpoint = "https://models.github.ai/inference"
model = "openai/gpt-4.1"

client = OpenAI(
    base_url=endpoint,
    api_key=token,
)


def get_versions():
    windows_version = platform.platform()
    print("Windows version:", windows_version)

    try:
        ps_version = subprocess.check_output(
            ["powershell", "$PSVersionTable.PSVersion"],
            text=True
        ).strip()
        print("PowerShell version:\n", ps_version)
        return f"Windows version: {windows_version}, Powershell version: {ps_version}"
    except Exception as e:
        print("Could not get PowerShell version:", e)
        return f"Windows version: {windows_version}, Could not get PowerShell version"

versions = get_versions()

def Ai(text:str):
    with open("./assets/command.txt", "r") as f:
        command = f.read()

    with open("./assets/persona.txt", "r") as f:
        persona = f.read()

    with open("./assets/logs.log", "r") as f:
        logs = f.read()

    response = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": command,
            },
            {
                "role": "system",
                "content": versions,
            },
            {
                "role": "system",
                "content": persona,
            },
            {
                "role": "system",
                "content": logs,
            },
            {
                "role": "user",
                "content": text,
            }
        ],
        temperature=1,
        top_p=1,
        model=model
    )

    return(response.choices[0].message.content)


def run_code(code:str):
    completed = subprocess.run(
    ["powershell", "-Command", code],
    capture_output=True,
    text=True
    )
    return completed.stdout

while True:
    user_text = input("> ")
    respons = Ai(text=user_text)
    try:
        respons = respons.split("@&")
        output = respons[0]
        print(output)
        code = respons[1]
        print(run_code(code))
    except:
        pass
    with open("./assets/logs.log", 'w') as f:
        f.write(f"User: {user_text}, You: {respons}")