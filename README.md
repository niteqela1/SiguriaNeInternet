# Leximi i fjalëkalimeve të ruajtura të WiFi-ve
## Teknologjitë e përdorura
* Python
    * `Flask`
---
## Instalimi 

Paraprakisht duhet instaluar Python dhe një IDE për të, për më shumë klikoni [këtu](https://realpython.com/installing-python/).

Për të konfiguruar mjedisin punues për Flask duhet instaluar paketa:
- Flask
```bash
pip install Flask
```
---

## Implementimi

> Hapat realizues:
1. Importimi i modulit të ***subprocess***.
2. Marrja e meta të dhënave të WLAN (WiFi) me anë të metodës check_output. 
3. Dekodimi i meta të dhënave dhe ndarja sipas rreshtit.
4. Nga meta të dhënat e dekoduara marrim emrat e rrjeteve të ruajtura (WLAN networks).
5. Për çdo emër marrim përsëri meta të dhënat e WLAN sipas emrit
6. Marrim fjalëkalimin e emrit të Wi-Fi
7. Shtypim fjalëkalimin dhe emrin WiFi. Në rast se WiFi e caktuar nuk ka fjalëkalim atëherë për atë do jetë hapësirë e zbrazët.

### Marrja e detajeve të Wi-Fi

```python
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profile']).decode('utf-8').split('\n')
profiles = []
for profile in data:
    if "All User Profile" in profile:
        profiles.append(profile.split(":")[1][1:-1])
```
### Ruajtja e fjalëkalimeve
```python
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
```
### Pamja Aplikacionit
![app](https://user-images.githubusercontent.com/75278492/148682180-e6070ced-3669-49ea-99e7-4402f235a159.PNG)

---
## Punuan
- [@nitëqela](https://github.com/niteqela1)
- [@midiemerovci](https://github.com/midie-merovci)
- [@valdetesalihi](https://github.com/valdetesalihi)