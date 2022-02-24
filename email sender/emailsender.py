import smtplib
import ssl
from email.message import EmailMessage

subject = "email from python"
body = "this is test email. from python"
sender_email = "pchocamiletisim@gmail.com"
receiver_email = "pchocamiletisim@gmail.com"
password = input("enter a password: ")

message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject

html = f"""
<html>
     <body>
         <h1>{subject}</h1>
         <p>{body}</p>
    </body>
</html>
"""

message.add_alternative(html, subtype="html")

context = ssl.create_default_context()

print("sending email")

with smtplib.SMTP_SSL("smtb.gmail.com", 465, context=context)as server:
    server.login(sender_email, password)
    server.sendemail(sender_email, receiver_email, message.as_strint())


print("succes")