
import smtplib
from email.message import EmailMessage
from senderDetails import *
import imaplib
from email.utils import formataddr

def emailSender(gifter, giftee, email):
    """
    Sends an email to the gifter with the name of their giftee.

    Args:
    gifter (str): The name of the person who is giving the gift.
    giftee (str): The name of the person who is receiving the gift.
    email (str): The email address of the gifter.

    Returns:
    None
    """
    msg = EmailMessage()
    msg['Subject'] = 'It\'s Mariah Carey Time!!'
    msg['From'] = formataddr(('Santa Claus', sender)) #adds the name of sender to the email
    msg['To'] = formataddr((gifter, email)) #adds the name of the reciever to the email 

    html = """\
    <!DOCTYPE html>
    <html>
        <body>
            <h1>Hello {gifter},</h1>
            <p>You are {giftee}'s secret santa this christmas, Spread some joy!!</p>
        </body>
    </html>
    """.format(**locals())

    msg.set_content(html, subtype='html')

    # Attempt to send the email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password)
            smtp.send_message(msg)
    except Exception as e:
        print(f"An error occurred: {e}")

def emailDeleter():    
    try:
        imap = imaplib.IMAP4_SSL("imap.gmail.com")
        imap.login(sender, password)
        imap.select('"[Gmail]/Sent Mail"') 
        # Get all email IDs in the "Sent" folder
        status, messages = imap.search(None, "ALL")

        # Convert messages to a list of email IDs
        messages = messages[0].split(b' ')

        # Mark and delete the emails
        for mail in messages:
            _, msg = imap.fetch(mail, "(RFC822)")
            imap.store(mail, "+FLAGS", "\\Deleted")

        # Expunge to permanently delete the marked emails
        imap.expunge()
        # Close the mailbox
        imap.close()
        # Logout from the account
        imap.logout()
        print("Emails deleted successfully")    
    except Exception as e:
        print(f"An error occurred: {e}")    

emailSender("Noel", "Tom", "stephcurrysburner@gmail.com")
