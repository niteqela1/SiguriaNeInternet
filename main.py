import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
# print(data)

profiles = []
for profile in data:
    print(profile)
