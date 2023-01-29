import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_newsletter(subscribers_file, subject, message, sender_email, sender_password):
    with open(subscribers_file) as file:
        reader = csv.reader(file)
        next(reader) # skip header row
        subscribers = [row[0] for row in reader]
        
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    for subscriber in subscribers:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = subscriber
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message, 'plain'))
        
        server.send_message(msg)
        
    server.quit()

subscribers_file = 'subscribers.csv'
subject = 'Monthly Newsletter'
message = 'Hello subscriber,\n\nHere is this month\'s newsletter.\n\nBest,\nYour Name'
sender_email = 'sender@email.com'
sender_password = 'sender_password'

send_newsletter(subscribers_file, subject, message, sender_email, sender_password)
