# importing email
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# adding sender and receiver
sender_email_id = 'i.sage0007@gmail.com'
receiver_email_id = ['aneeqahjones2@gmail.com', 'naeemahndavis@gmail.com', 'thapelo@lifechoices.co.za', 'brentleejohnson73@gmail.com']
# input password
password = input("Password: ")
subject = "Greetings"
msg = MIMEMultipart()
msg['From'] = sender_email_id
msg['To'] = ', '.join(receiver_email_id)
msg['Subject'] = subject
body = "Hello there!\n"
body = body + "Did you hear about the Italian chef who died? He pasta-way"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login(sender_email_id, password)
# message to be sent

# sending the mail
s.sendmail(sender_email_id, receiver_email_id, text)
# terminating the session
s.quit()
