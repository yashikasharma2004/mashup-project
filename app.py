import static_ffmpeg
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
    msg['From'] = 'your-email@gmail.com'  # <--- Yahan apni email ID likhein
    msg['To'] = receiver_email
    msg.set_content('Attached is your requested mashup zip file.')

    with open(zip_path, 'rb') as f:
        msg.add_attachment(f.read(), maintype='application', subtype='zip', filename='102317089-result.zip')

    # SMTP Login (App Password zaroori hai)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your-email@gmail.com', 'your-app-password') # <--- Yahan App Password likhein
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
    
    # Program-1 ko call karna
    # Command: python 102317089.py <singer> <n> <y> <output_name>
    subprocess.run(["python", "102317089.py", singer, n, y, "102317089-output.mp3"])

    zip_file = "102317089-output.zip"
    
    if os.path.exists(zip_file):
        send_email(email, zip_file)
        return f"<h1>Success!</h1><p>Mashup zip sent to {email}</p>"
    else:
        return "<h1>Error!</h1><p>Mashup generation failed. Check terminal for errors.</p>"



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

