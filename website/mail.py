__author__ = 'ruslan'

import smtplib
import datetime
from django.conf import settings

def send_contact_message(name, email, message):
    to_addr = settings.CONTACT_TO
    from_addr = settings.CONTACT_FROM
    now = datetime.datetime.now()
    subject = settings.CONTACT_SUBJECT % (now.strftime("%Y-%b-%d %H:%M:%S"))

    server = None
    try:
        msg = "From: %s\nReply-To: %s\nTo: %s\nSubject: %s\n\n" % (from_addr, email, to_addr, subject)
        msg += "Sender Name:\n%s\n\nEmail:\n%s\n\nContact Message:\n%s" % (name, email, message)

        server = smtplib.SMTP(settings.MAIL_SERVER)
        server.sendmail(from_addr, to_addr, msg)

        return True
    except smtplib.SMTPException:
        print "Error to send contact email from %s %s with message %s" % (name, email, message)
        return False
    finally:
        if server is not None:
            server.quit()
  