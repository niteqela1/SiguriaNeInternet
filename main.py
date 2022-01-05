import subprocess

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
# print(data)

profiles = []
for profile in data:
    print(profile)
    if "All User Profile" in profile:
        print(profile.split(":"))
        profiles.append(profile.split(":")[1][1:-1])
print(profiles)
for profile in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', profile, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        print ("{:<35}|  {:<}".format(profile, results[0]))
    except IndexError:
        print ("{:<35}|  {:<}".format(profile, ""))
