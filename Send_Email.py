from email.message import EmailMessage
import ssl
import smtplib

email_sender = "--Sender Mail--"
email_password = "--Email app password--"
email_receiver = "--Reciever Mail--"

def SendMail(Email_Body):
    subject = "New events have been created !"
    body = Email_Body

    em  = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as SMTP:
        SMTP.login(email_sender,email_password)
        SMTP.sendmail(email_sender,email_receiver,em.as_string())