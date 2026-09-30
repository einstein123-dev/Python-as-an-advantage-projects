import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Hello This is Einstein Testing"
msg["From"] = "realeinstein2@gmail.com"
msg["To"] = "richardeinstein40@gmail.com"
msg.set_content("Hello from Python and it is awesome!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("richardeinstein40@gmail.com", "pcidgwjzewqhnwbo")
    smtp.send_message(msg)