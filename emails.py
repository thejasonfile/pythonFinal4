#!/usr/bin/env python3

from email.message import EmailMessage
message = EmailMessage()
import mimetypes
import os

def generate_email(sender, recipient, subject, body, attachment_path):
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)

    with open(attachment_path, 'rb') as ap:
        message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

    return message

def generate_error_report(sender, recipient, subject, body):
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
