import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('hemelmomin520@gmail.com','cfqtcwquxtcdddub')

from_add = "hemelmomin520@gmail.com"
to_add = "pi.py.developer@gmail.com"
subject = "mail from stock script "
msg = MIMEMultipart()
msg["From"] = from_add
msg["To"] = to_add
msg["Subject"] = subject

body  = "hay there! sending mail through  python!"

msg.attach(MIMEText(body, 'html'))
masage = msg.as_string()


server.sendmail(from_add,to_add, masage)
server.quit()