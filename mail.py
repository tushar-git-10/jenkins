import smtplib
from email.mime.text import MIMEText
from datetime import datetime

# 🔐 Sender email (use your secondary Gmail)
from_email =  "tkokare17@gmail.com";
# 🔑 App Password (NOT normal password)
password ="lpwo azzy uxvt mplv";

# 📩 Receiver email
to_email = "tushar.kokare.aids.2024@vpkbiet.org";

# ✉️ Email content
subject = "Jenkins Build Notification"
body = f"""
Hello,

Your Jenkins job executed successfully!

Time: {datetime.now()}

Regards,
CI/CD System
"""

# Create message
msg = MIMEText(body)
msg['Subject'] = subject
msg['From'] = from_email
msg['To'] = to_email

try:
    # Connect to Gmail SMTP server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(from_email, password)

    # Send email
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()

    print("Email Sent Successfully!")

except Exception as e:
    print("Error:", e)