# Something in lines of http://stackoverflow.com/questions/348630/how-can-i-download-all-emails-with-attachments-from-gmail

import email
import imaplib
import os
import sys
import time
import datetime

def main():

    while(True):
        print datetime.datetime.now().time()
        detach = "."
        if 'attachments' not in os.listdir("."):
            print "Could not find attachments folder, so i made it."
            os.mkdir('attachments')

        try:
            imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
            typ, account = imapSession.login('username','password')
            imapSession.list()
            if typ != "OK":
                print "Error: Could not sign in, check creds"
            else:
                print "Logged in, checking labelname Emails"
                imapSession.select("label to check")
                
                (typ, data) = imapSession.search(None, '(UNSEEN)')
                if(data[0]==""):
                    print "No new mail"
                else:
                    print "There is new mail"

                    for msgs in str(data[0]).split():
                        typ, msgInfo = imapSession.fetch(msgs,'(RFC822)')
                        if typ != "OK":
                            print "error fetching mail"
                        else:
                            msgBody = msgInfo[0][1]
                            mail = email.message_from_string(msgBody)
                            for part in mail.walk():
                                fileName = part.get_filename()

                                if bool(fileName):
                                    filePath = os.path.join(detach, 'attachments',fileName)
                                    print "Downloading",fileName
                                    if not os.path.isfile(filePath):
                                        print fileName,"from", str(mail['From'])
                                        fp = open(filePath,'wb')
                                        fp.write(part.get_payload(decode=True))
                                        fp.close()
                                    print "Downloaded",fileName
                                    print "Now printing",filePath
                                    os.startfile(filePath, "print")
                                    time.sleep(15)
                                    os.system('cmd.exe /c taskkill /f /im AcroRd32.exe')
                                    print "Deleting file"
                                    os.remove(filePath)
            imapSession.close()
            print "checking again..."
            time.sleep(60)

    #imapSession.logout()

        except:
            print sys.exc_info()[0:]
            break

if __name__ == '__main__':
    main()
