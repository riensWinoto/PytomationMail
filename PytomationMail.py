import pytomationvar as pymvar
import pytomationfunc as pymfunc

if __name__ == "__main__":
    broadCaster = pymfunc.initial_setup()
    count = 0
    while count < len(pymvar.receiverNames):
        while count < len(pymvar.receiverEmails):

            fromSender = pymfunc.get_sender(pymvar.myName, pymvar.myEmail)
            toReceiver = pymfunc.get_receiver(pymvar.receiverNames[count], pymvar.receiverEmails[count])
            emailMessage = pymfunc.get_email_message(pymvar.emailSubject, pymvar.emailBody)
            messenger = fromSender + "\n" + toReceiver + "\n" + emailMessage

            broadCaster.sendmail(pymvar.myEmail, pymvar.receiverEmails[count], messenger)
            sendDateTime = pymfunc.get_date_time()

            print("e-mail sent successfully to {} at {} \n".format(pymvar.receiverNames[count], sendDateTime))

            if count >= len(pymvar.receiverNames) or count >= len(pymvar.receiverEmails):
                break
            else:
                count += 1
                continue
        continue
    broadCaster.quit()
