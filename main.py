import subprocess
from flask import Flask, render_template

app = Flask(__name__)

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
profiles = []
for profile in data:
    if "All User Profile" in profile:
        profiles.append(profile.split(":")[1][1:-1])

passwords = []
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    for res in results:
        if "Key Content" in res:
            passwords.append(res.split(":")[1][1:-1])
        elif "Key Index" in res:
            passwords.append(" ")

res = {}
for key in profiles:
    for value in passwords:
        res[key] = value
        passwords.remove(value)
        break

@app.route("/")
def home():
    return render_template("index.html", dictionary_names_pw = res)

if __name__ == "__main__":
    app.run(debug = True)