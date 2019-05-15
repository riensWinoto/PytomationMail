import pytomationfunc as pymfunc
import pytomationvar as pymvar

if __name__ == "__main__":
    broadCaster = pymfunc.initial_setup()
    if pymvar.trigger >= len(pymvar.receiverNames) or pymvar.trigger >= len(pymvar.receiverEmails) \
            or len(pymvar.receiverNames) != len(pymvar.receiverEmails):
        print("Enter receiver mail or receiver name next time")

    else:
        while pymvar.count < len(pymvar.receiverNames):
            while pymvar.count < len(pymvar.receiverEmails):

                fromSender = pymfunc.get_sender(pymvar.myName, pymvar.myEmail)
                toReceiver = pymfunc.get_receiver(pymvar.receiverNames[pymvar.count], pymvar.receiverEmails[pymvar.count])
                emailMessage = pymfunc.get_email_message(pymvar.emailSubject, pymvar.emailBody)
                messenger = fromSender + "\n" + toReceiver + "\n" + emailMessage

                broadCaster.sendmail(pymvar.myEmail, pymvar.receiverEmails[pymvar.count], messenger)
                sendDateTime = pymfunc.get_date_time()

                print("e-mail sent successfully to {} at {} \n".format(pymvar.receiverNames[pymvar.count], sendDateTime))

                if pymvar.count >= len(pymvar.receiverNames) or pymvar.count >= len(pymvar.receiverEmails):
                    break
                else:
                    pymvar.count += 1
                    continue
            continue
        broadCaster.quit()
