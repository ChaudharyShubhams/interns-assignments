import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('shubhamchaudhary.mail3@gmail.com', '******')
message = MIMEMultipart()
message['Subject'] = 'Challenge 3 Completed'

text = """\
1.Shubham Chaudhary, Semester-passout, Branch-cse, and roll number-1ST18CS134.
"""

msg_ready = MIMEText(text)

# Image should be in same folder
image_open = open('image.jpg', 'rb').read()
image_ready = MIMEImage(image_open, 'jpg', name='image')

message.attach(msg_ready)
message.attach(image_ready)

server.sendmail('shubhamjps543@gmail.com', 'hr@ignitershub.com',
                message.as_string())  # message should be in string format
print("sent")