# smtplib module is necessary to create a server to send the email

from os import name
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path



html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Vignesh Jayaraman'
email['to'] = 'aiworld@gmail.com'
email['subject'] = 'Greetings'

email.set_content(html.substitute({'name' : "Vignesh"}),'html')

with smtplib.SMTP (host = "smtp.gmail.com", port = "587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("vigneshjayaraman@gmail.com", "itsmevicky")
    smtp.send_message(email)