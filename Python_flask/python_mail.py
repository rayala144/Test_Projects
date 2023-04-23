import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Set up the SMTP server
server = smtplib.SMTP('smtp.example.com', 587)
server.starttls()
server.login("username@example.com", "password")

# Create the message
msg = MIMEMultipart()
msg['from'] = 'username@example.com'
msg['to'] = 'you@example.com'
msg['subject'] = 'This is an automated email.'

body = 'This is an automated email with an attachment.'
msg.attach(MIMEText(body, 'plain'))

filename = '.\Misc\qrcode.png'
fp = open(filename, 'rb')
attachment = MIMEText(fp.read(), 'plain')
fp.close()
attachment.add_header('Content-Disposition', 'attachment', filename=filename)

msg.attach(attachment)

# Send the message
server.sendmail(msg['from'], msg['to'], msg.as_string())

# Log out of the server
server.quit()

