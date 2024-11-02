import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "superpeppino0000@gmail.com"
    password = os.getenv("GMAIL_PASSWORD")
    receiver = "daiello.giuseppe02@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP("smtp.gmail.com") as server:
        server.starttls() and server.login(user=username, password=password)
        server.sendmail(from_addr=username,
                        to_addrs=receiver,
                        msg=message)







