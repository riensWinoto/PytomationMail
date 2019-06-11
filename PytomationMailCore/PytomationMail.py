import pytomationfunc as pymfunc
import pytomationvar as pymvar

if __name__ == "__main__":
    broadCaster = pymfunc.initial_setup()
    if pymvar.trigger >= len(pymvar.receivers):
        print("Enter receiver name and email next time")
    else:
        for receiverName, receiverEmail in pymvar.receivers.items():
            fromSender = pymfunc.get_sender(pymvar.myName, pymvar.myEmail)
            toReceiver = pymfunc.get_receiver(receiverName, receiverEmail)
            emailMessage = pymfunc.get_email_message(pymvar.emailSubject, pymvar.emailBody)
            messenger = fromSender + "\n" + toReceiver + "\n" + emailMessage

            broadCaster.sendmail(pymvar.myEmail, receiverEmail, messenger)
            sendDateTime = pymfunc.get_date_time()

            print("e-mail sent successfully to {} at {} \n".format(receiverName, sendDateTime))
        broadCaster.quit()
