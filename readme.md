<p align="centre">
  <a href="">
  <img src="https://raw.githubusercontent.com/hackesofice/Z/refs/heads/main/Live-Server-backend/Live.jpg" alt="Live server img">
</p>
    
# Disclaimer

This is a simple **backend server** for the **<a href="https://acode.app/plugin/liveserver">Acode Live Server</a>** plugin. It runs inside the **Termux** app on your Android device.

[![Typing SVG](https://readme-typing-svg.demolab.com?font=Fira+Code&weight=700&duration=4000&pause=1000&center=true&vCenter=true&width=435&lines=HEY+DEAR+WELCOME+TO+THE+REPOSITORY+;PLEASE+DON'T+FORGET+TO+STAR+%E2%AD%90+US;REPORT+FOR+ANY+ISSUES+;FOLLOW+US+ON+YOUTUBE;USE+100%+FREE+)](https://git.io/typing-svg)

---

## Installation Steps

### BACKEND (THIS ONE)

1. <a href="https://f-droid.org/repo/com.termux_1000.apk">Download</a> Termux from F-Droid  
2. Install and open Termux.  
3. Copy and paste the following commands one by one **OR** all at once into Termux, then press Enter:

```
rm -rf Acode-live-server-backend
pkg update && pkg upgrade -y
termux-setup-storage
pkg install python -y
pkg install git -y
git clone https://github.com/hackesofice/Acode-live-server-backend.git
cd Acode-live-server-backend
pip install -r requirements.txt
python main.py
```

> Note - If you're asked for permission or prompted with Y/N, type `Y` and press Enter, or tap "Allow" when requested.

---

### HOW TO RUN NEXT TIME

Each time you want to use the plugin, run these two commands:

```
cd Acode-live-server-backend
python main.py
```

---

### BONUS STEP (RECOMMENDED)

If you don’t want to run the commands manually every time, check out this tool:  
<a href="https://github.com/hackesofice/all-in-one-runner.git">https://github.com/hackesofice/all-in-one-runner.git</a>

---

## Frontend (Acode App Plugin)

1. Install the **Acode app** from the Google Play Store.  
2. Tap the **menu icon** (top-left corner).  
3. Tap the **Extensions** icon.  
4. Search for **Live Server**.  
5. Tap on the result, then tap **Install**.

---

## Contribution

Contributions are welcome! Everything is open source:  
- Found an issue? Open one on GitHub.  
- Want to contribute code? Fork the repo, make your changes, and submit a pull request with a clear description.
