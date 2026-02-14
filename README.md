# 🎵 MASHUP PRO: High-Quality Audio Mashup Generator

[![Python Version](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![Flask Version](https://img.shields.io/badge/Flask-3.0.0-green?logo=flask)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-Educational-orange)](https://github.com/yashikasharma2004/mashup-project)
[![Deployment](https://img.shields.io/badge/Render-Live-brightgreen?logo=render)](https://mashup-project-xq17.onrender.com)

**MASHUP PRO** is a powerful web-based service that allows users to create custom audio mashups of their favorite singers. By simply providing a singer's name, the number of tracks, and a specific duration, the application automates the process of fetching, trimming, and merging audio files.

---
<img width="912" height="888" alt="image" src="https://github.com/user-attachments/assets/2a08bf0e-7b41-4630-8c6c-37b6aeb18963" />

## 🚀 Live Demo
Experience the magic here: **[Mashup Pro Live on Render](https://mashup-project-xq17.onrender.com)**

---

## ✨ Key Features
* **Automated Retrieval**: Uses `yt-dlp` to fetch high-quality audio streams directly from YouTube.
* **Precision Trimming**: Trims each audio clip to the exact duration ($Y > 20$) specified by the user using `MoviePy`.
* **Seamless Merging**: Concatenates multiple clips ($N > 10$) into a single high-fidelity audio output.
* **Cloud Email Delivery**: Automatically zips the final output and sends it to the user's provided email address.
* **Modern UI**: A "Jhakaas" glassmorphism interface built with Bootstrap 5 and Google Fonts.

---

## 🛠️ Tech Stack
| Component | Technology |
| :--- | :--- |
| **Backend** | Python / Flask |
| **Frontend** | HTML5, CSS3, Bootstrap 5 |
| **Libraries** | `yt-dlp`, `moviepy`, `pydub`, `subprocess` |
| **Deployment** | Render (Web Service) |
| **Mailing** | Python `smtplib` & `email.message` |

---

## 📂 Project Structure
```text
mashup-project/
├── templates/          # Frontend HTML files
│   └── index.html      # The "Jhakaas" UI
├── app.py              # Flask server & Port binding
├── 102317089.py        # Core logic for mashup generation
├── requirements.txt    # List of dependencies
└── README.md           # This file



📖 How to Run Locally
1. Clone the Repo:
git clone [https://github.com/yashikasharma2004/mashup-project.git](https://github.com/yashikasharma2004/mashup-project.git)

2. Install Dependencies:
pip install -r requirements.txt

3. Run the App:
python app.py

4. Open http://127.0.0.1:5000 in your browser.




👤 Author
Name: Yashika Sharma

Roll No: 102317089
