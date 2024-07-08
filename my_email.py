import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pickle
from config import email_config
def send_email(data):
    sent_links = load_sent_links()
    if data['link'] in sent_links:
        return
    sender = email_config['sender']
    receiver = email_config['receiver']
    password = email_config['smtp_password']

    msg = MIMEMultipart()
    msg['From'] = email_config['sender']
    msg['To'] = email_config['receiver']
    msg['Subject'] = 'Bitcoin Talk New Forum Post'

    body = f"""
    Title: {data['title']}
    Link: {data['link']}
    Author: {data['author']}
    Replies: {data['replies']}
    Views: {data['views']}
    Last Post: {data['last_post']}
    """
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(email_config['smtp_server'], email_config['smtp_port'])
    server.login(sender, password)
    text = msg.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()
    sent_links.append(data['link'])
    save_sent_links(sent_links)
def load_sent_links():
    try:
        with open('sent_links.pkl', 'rb') as f:
            return pickle.load(f)
    except FileNotFoundError:
        return []

def save_sent_links(links):
    with open('sent_links.pkl', 'wb') as f:
        pickle.dump(links, f)


