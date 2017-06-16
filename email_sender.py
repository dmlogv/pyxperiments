"""Simple email send wizard"""

import smtplib
from email.message import EmailMessage


class Cache:
    """Stores user inputs between tries"""
    def __init__(self, **kwargs):
        self._cache = kwargs

    def __getitem__(self, key):
        return self._cache.get(key)

    def __setitem__(self, key, value):
        self._cache[key] = value
    
    def update(self, **kwargs):
        """Update all items"""
        self._cache.update(kwargs)


CACHE = Cache()


def send_email(server, login, passw, sender, receiver, subject, msg):
    """Send email via secured SMTP server"""
    server = smtplib.SMTP('email.magnit.ru')
    server.set_debuglevel(1)

    server.starttls()
    server.login(login, passw)

    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = sender
    email['To'] = receiver
    email.set_content(msg)

    server.send_message(email)
    server.quit()


def prompt(prompt, default=None):
    """Get cleaned input"""
    prompt = f'{prompt} ({default}): ' if default else f'{prompt}: '
    return input(prompt).strip() or default


def interact():
    """Get user inputs"""
    server = prompt('Enter SMTP server host', CACHE['server'])
    login = prompt('Your login', CACHE['login'])
    passw = prompt('Any password', CACHE['passw'])
    sender = prompt('Sender email', CACHE['sender'])
    receiver = prompt('Receiver email', CACHE['receiver'])
    subject = prompt('Email subject', CACHE['subject'])
    msg = prompt('Message', CACHE['msg'])

    CACHE.update(server=server, login=login, passw=passw, sender=sender, 
                 receiver=receiver, subject=subject, msg=msg)

    send_email(server, login, passw, sender, receiver, subject, msg)


if __name__ == '__main__':
    print('Hello human.\nI try to send your stupid email.\n\n'
          'Follow the instructions. Press Ctrl+C to break any stage.\n')
    while True:
        try:
            interact()
        except KeyboardInterrupt:
            print('Interrupted by human')
            break

        print('Done\n')
