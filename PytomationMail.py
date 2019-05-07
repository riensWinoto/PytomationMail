import smtplib
import sys
import time
from datetime import datetime

# variable
myName = "your name"
myEmail = "your@email.com"
myPass = "y0urP4s5w0rd"
myEmailSMTP = "smtp.yourEmailProvider.com" #for gmail: smtp.gmail.com  for outlook: smtp-mail.outlook.com
mySMTPPort = 587

receiverNames = ["receiver name"]
receiverEmails = ["receiver@email.com"]
emailSubject = "This is Python Automation First Try"
emailBody = """
Hello there,
This is me, Riens Winoto just try the research for automation \
using Python.
Python do the magic well

Regards,
Riens Winoto
"""

# function
def inital_setup():

    type(broadCaster)
    broadCaster.ehlo()
    broadCaster.starttls()
    try:
        broadCaster.login(myEmail, myPass)
    except IOError as err:
        print(str(err))
        time.sleep(1.0)
        sys.exit()


def get_date_time():
    date_and_time = datetime.now()
    str_date_time = date_and_time.strftime('%b %-d,%Y, %-I:%M%p')
    return str_date_time


if __name__ == "__main__":
    broadCaster = smtplib.SMTP(myEmailSMTP, mySMTPPort)
    inital_setup()

    count = 0
    while count < len(receiverNames):
        while count < len(receiverEmails):

            fromSender = "from:" + " " + myName + " " + "<" + myEmail + ">"
            toReceiver = "to:" + " " + receiverNames[count] + " " + "<" + receiverEmails[count] + ">"
            emailMessage = "subject:" + " " + emailSubject + "\n" + emailBody
            messenger = fromSender + "\n" + toReceiver + "\n" + emailMessage

            broadCaster.sendmail(myEmail, receiverEmails[count], messenger)
            sendDateTime = get_date_time()

            print("e-mail sent successfully to {} at {} \n".format(receiverNames[count], sendDateTime))
            count += 1
            if count >= len(receiverNames) or count >= len(receiverEmails):
                break
            else:
                continue
        continue
    broadCaster.quit()
