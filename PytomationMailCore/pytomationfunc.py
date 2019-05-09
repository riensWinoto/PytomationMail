import smtplib
import sys
import time
from datetime import datetime
import pytomationvar as pymvar


# function
def initial_setup():
    broad_caster = smtplib.SMTP(pymvar.myEmailSMTP, pymvar.mySMTPPort)
    broad_caster.ehlo()
    broad_caster.starttls()
    try:
        broad_caster.login(pymvar.myEmail, pymvar.myPass)
    except IOError as err:
        print(str(err))
        time.sleep(1.0)
        sys.exit()
    return broad_caster


def get_sender(sender_name, sender_email):
    from_sender = "from:" + " " + sender_name + " " + "<" + sender_email + ">"
    return from_sender


def get_receiver(receiver_name, receiver_email):
    to_receiver = "to:" + " " + receiver_name + " " + "<" + receiver_email + ">"
    return to_receiver


def get_email_message(email_subject, email_body):
    email_message = "subject:" + " " + email_subject + "\n" + email_body
    return email_message


def get_date_time():
    date_and_time = datetime.now()
    str_date_time = date_and_time.strftime('%b %-d,%Y, %-I:%M%p')
    return str_date_time
