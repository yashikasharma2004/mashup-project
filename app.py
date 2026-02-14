import static_ffmpeg
# FFmpeg ko path mein add karna zaroori hai process ke liye
static_ffmpeg.add_paths() 

from flask import Flask, render_template, request
import subprocess
import smtplib
from email.message import EmailMessage
import os

app = Flask(__name__)

# Email bhejne ka function
def send_email(receiver_email, zip_path):
    msg = EmailMessage()
    msg['Subject'] = 'Mashup Result - 102317089'
    msg['From'] = 'your-email@gmail.com'  # <--- Apni Email ID yahan likhein
    msg['To'] = receiver_email
    msg.set_content('Attached is your requested mashup zip file.')

    with open(zip_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='102317089-result.zip')

    # SMTP Login (Google App Password use karein)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your-email@gmail.com', 'your-app-password') # <--- 16-digit App Password yahan likhein
        smtp.send_message(msg)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    singer = request.form['singer']
    n = request.form['num_videos'] # Validation: N > 10
    y = request.form['duration']   # Validation: Y > 20
    email = request.form['email']
    
    zip_file = "102317089-output.zip"

    # Purani zip file agar exists karti hai toh delete kar dein
    if os.path.exists(zip_file):
        os.remove(zip_file)
    
    # Program-1 ko call karna - Sabse important change .zip extension yahan hai
    # Render ke liye 'python3' use karna zyada safe hai
    subprocess.run(["python3", "102317089.py", singer, n, y, zip_file])

    # Check karna ki zip file bani ya nahi
    if os.path.exists(zip_file):
        send_email(email, zip_file)
        return f"<h1>Success!</h1><p>Mashup zip sent to {email}</p>"
    else:
        # Agar file nahi bani toh logs mein check karna padega
        return "<h1>Error!</h1><p>Mashup generation failed. Please check inputs or try again.</p>"

if __name__ == '__main__':
    # Render ke liye port binding
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
