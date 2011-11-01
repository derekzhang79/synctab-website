import smtplib
import datetime
from django.conf import settings

def send_contact_message(name, email, message):
    """ Sends Context message to Ruslan """
    to_addr = settings.CONTACT_TO
    from_addr = settings.CONTACT_FROM
    now = datetime.datetime.now()
    subject = settings.CONTACT_SUBJECT % (now.strftime("%Y-%b-%d %H:%M:%S"))

    # prepare the message to send
    msg = ("Sender Name:\n%s\n\n" +
           "Email:\n%s\n\n" + 
           "Contact Message:\n%s") % (name, email, message)
    
    return send_email(from_addr, to_addr, email, subject, msg)

def send_issue_message(name, email, module, description):
    """ Sends New Issue message to Ruslan """
    to_addr = settings.SUBMIT_ISSUE_TO
    from_addr = settings.SUBMIT_ISSUE_FROM
    now = datetime.datetime.now()
    subject = settings.SUBMIT_ISSUE_SUBJECT % (now.strftime("%Y-%b-%d %H:%M:%S"))

    # prepare the message to send
    msg = ("Reporter Name:\n%s\n\n" +
           "Email:\n%s\n\n" +
           "Issue Module:\n%s\n\n" +
           "Issue Description:\n%s") % (name, email, module, description)
    
    return send_email(from_addr, to_addr, email, subject, msg)

def send_email(from_addr, to_addr, reply_to_addr, subject, message):
    """ Sends the email with specified headers and body """

    server = None
    try:
        # prepare headers
        msg = ("From: %s\n" +
               "Reply-To: %s\n" +
               "To: %s\nSubject: %s\n\n") % \
              (from_addr, reply_to_addr, to_addr, subject)

        # and append message
        msg += message

        # connect to the SMTP server and send email
        server = smtplib.SMTP(settings.EMAIL_HOST)
        server.sendmail(from_addr, to_addr, msg)

        return True
    except smtplib.SMTPException:
        # if failed to send an email, than output a message,
        # so can be checked for later!
        print "Error to send contact email %s" % message
        return False
    finally:
        if server is not None:
            server.quit()
