# coding: utf-8

import smtplib as smtp
from email.mime.text import MIMEText
from decouple import config
import sys
import os

sys.path.append(os.path.abspath(os.curdir))


def sendEmail(to: str, _from: str, subject: str, message: str) -> None:
    """
    sendEmail is capable to get emissor, receiver and a message and send it using Simple Mail Transfer Protocol(SMTP).\n
    Args:
        to: receiver email
        from: emissor email
        subject: message's subject
        message: email body
    """

    key = config("PASSWORD")
    mimeMSG = MIMEText(
        _text=message,
        _charset="utf-8",
    )
    mimeMSG["Subject"] = subject
    mimeMSG["From"] = _from
    mimeMSG["To"] = to

    with smtp.SMTP("smtp.gmail.com: 587") as s:
        s.starttls()
        s.login(_from, key)
        s.sendmail(_from, to, mimeMSG.as_string())
