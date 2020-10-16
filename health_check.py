#!/usr/bin/env python3

import emails, psutil, shutil, socket

#report error if:
#CPU > 80%
#available disk space < 20%
#available memory < 500MB
#hostname 'localhost' cannot be resolved to "127.0.0.1"

def cpu_check():
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        subject = "Error - CPU usage is over 80%"
        error_email(subject)

def disk_check():
    disk_usage = shutil.disk_usage("/")
    disk_free_percent = (disk_usage.free / disk_usage.total) * 100
    if disk_free_percent < 20:
        subject = "Error - Available disk space is less than 20%"
        error_email(subject)

def mem_check():
    mem = psutil.virtual_memory()
    mem_threshold = 500 * 1024 * 1024
    if mem.available < mem_threshold:
        subject = "Error - Available memory is less than 500MB"
        error_email(subject)

def hostname_check():
    hostname = socket.gethostbyname('localhost')
    if hostname != '127.0.0.1':
        subject = "Error - localhost cannot be resolved to 127.0.0.1"
        error_email(subject)

def error_email(subject):
    sender = 'automation@example.com'
    recipient = 'username@example.com'
    body = "Please check your system and resolve the issue as soon as possible"
    message = emails.generate_error_report(sender, recipient, subject, body)
    emails.send_email(message)

if __name__ == "__main__":
    emails.generate_email
    emails.generate_error_report
    emails.send_email
