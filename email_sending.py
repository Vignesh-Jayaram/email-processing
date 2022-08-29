# smtplib module is necessary to create a server to send the email

import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path



html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'Vignesh Jayaraman'
email['to'] = "receiver emailid"
email['subject'] = 'Greetings'

email.set_content(html.substitute({'name' : "Vignesh"}),'html')

with smtplib.SMTP (host = "smtp.gmail.com", port = "587") as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("< user_email >", "< user_password >") 
    smtp.send_message(email)