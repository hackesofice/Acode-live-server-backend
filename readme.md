<p align="centre">
  <a href="">
  <img src="https://raw.githubusercontent.com/hackesofice/Z/refs/heads/main/Live-Server-backend/Live.jpg" alt="Live server img">
</p>

![](https://readme-typing-svg.demolab.com?font=Fira+Code&size=28&duration=3000&pause=1000&color=C084FC&center=true&vCenter=true&width=705&lines=🚀+Acode+Live+Server+Plugin+by+Hackesofice;💻+Live+Preview+for+HTML+on+Android;🌐+Open+Source+and+Free+Forever!)



  
  <p align="center">
        <img src="https://media.giphy.com/media/2wYFfJR9uZoOs/giphy.gif" height="25">
        <a href="https://github.com/hackesofice/Acode-live-server-backend/issues?q=is%3Aissue+is%3Aclosed">
          <img alt="Closed Issues" src="https://img.shields.io/github/issues-closed/hackesofice/Acode-live-server-backend?style=for-the-badge&color=3cb371&logo=checkmarx">
        </a>
    <img src="https://media.giphy.com/media/l2JHRhAtnJSDNJ2py/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend/stargazers">
      <img alt="Stars" src="https://img.shields.io/github/stars/hackesofice/Acode-live-server-backend?style=for-the-badge&color=ffd700&logo=github">
    </a>
    <img src="https://media.giphy.com/media/d31vTpVi1LAcDvdm/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend/network">
      <img alt="Forks" src="https://img.shields.io/github/forks/hackesofice/Acode-live-server-backend?style=for-the-badge&color=ff7f50&logo=git">
    </a>
    <img src="https://media.giphy.com/media/LmNwrBhejkK9EFP504/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/hackesofice/Acode-live-server-backend?style=for-the-badge&color=00bfff&logo=bugatti">
    </a>
    <img src="https://media.giphy.com/media/W5T1OR1XEDaXS/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server/pulls">
      <img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/hackesofice/Acode-live-server-backend?style=for-the-badge&color=9370db&logo=githubactions">
    </a>
    <img src="https://media.giphy.com/media/U3qYN8S0j3bpK/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend/commits/main">
      <img alt="Last Commit" src="https://img.shields.io/github/last-commit/hackesofice/Acode-live-server-backend?style=for-the-badge&color=32cd32&logo=clockify">
    </a>
    <img src="https://media.giphy.com/media/3oEjI5VtIhHvK37WYo/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend/blob/main/LICENSE">
      <img alt="License" src="https://img.shields.io/github/license/hackesofice/Acode-live-server-backend?style=for-the-badge&color=ff69b4&logo=open-source-initiative">
    </a>
    <img src="https://media.giphy.com/media/SuV6PMf5dUvvW/giphy.gif" height="25">
    <a href="https://acode.app/plugin/liveserver">
      <img alt="Downloads" src="https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Facode.app%2Fapi%2Fplugin%2Fliveserver&query=downloads&style=for-the-badge&label=Downloads&labelColor=363a4f&color=c084fc&logo=download">
    </a>
    <img src="https://media.giphy.com/media/j5QcmXoFWlYJk/giphy.gif" height="25">
    <a href="https://github.com/hackesofice/Acode-live-server-backend">
      <img alt="Repo Size" src="https://img.shields.io/github/repo-size/hackesofice/Acode-live-server-backend?style=for-the-badge&color=00ced1&logo=files">
    </a>
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
