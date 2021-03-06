import smtplib
import sys
import time
from datetime import datetime

# variable
trigger = 0
myName = "your name"
myEmail = "your@email.com"
myPass = "y0urP4s5w0rd"
myEmailSMTP = "smtp.yourEmailProvider.com" #for gmail: smtp.gmail.com  for outlook: smtp.office365.com
mySMTPPort = 587

receivers = {"receiver name": "receiver@email.com"}
emailSubject = "I'm Pytomation Mail"
emailBody = """
Hello there,

Feel free to use this Pytomation Mail and modify it \
base on your needs


Thanks and Regards,
Riens Winoto
"""

# function
def initial_setup():
    try:
        broad_caster = smtplib.SMTP(myEmailSMTP, mySMTPPort)
        broad_caster.ehlo()
        broad_caster.starttls()
        broad_caster.login(myEmail, myPass)
    except IOError as err:
        print(str(err))
        time.sleep(1.0)
        sys.exit()
    return broad_caster


def get_date_time():
    date_and_time = datetime.now()
    str_date_time = date_and_time.strftime('%b %-d,%Y, %-I:%M%p')
    return str_date_time


def get_sender(sender_name, sender_email):
    from_sender = "from:" + " " + sender_name + " " + "<" + sender_email + ">"
    return from_sender


def get_receiver(receiver_name, receiver_email):
    to_receiver = "to:" + " " + receiver_name + " " + "<" + receiver_email + ">"
    return to_receiver


def get_email_message(email_subject, email_body):
    email_message = "subject:" + " " + email_subject + "\n" + email_body
    return email_message


if __name__ == "__main__":
    broadCaster = initial_setup()
    if trigger >= len(receivers):
        print("Enter receiver name and email next time")
    else:
        for receiverName, receiverEmail in receivers.items():
            fromSender = get_sender(myName, myEmail)
            toReceiver = get_receiver(receiverName, receiverEmail)
            emailMessage = get_email_message(emailSubject, emailBody)
            messenger = fromSender + "\n" + toReceiver + "\n" + emailMessage

            broadCaster.sendmail(myEmail, receiverEmail, messenger)
            sendDateTime = get_date_time()

            print("e-mail sent successfully to {} at {} \n".format(receiverName, sendDateTime))
        broadCaster.quit()