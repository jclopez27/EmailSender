import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def main():
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "juandevelopmet@gmail.com"  # Enter your address
    receiver_email = "jcruzlopez27@gmail.com"  # Enter receiver address
    password = input('Type your password and press enter: ')

    message = MIMEMultipart("alternative")
    message["Subject"] = "multipart test"
    message["From"] = sender_email
    message["To"] = receiver_email

    # Create the plain-text and HTML version of you message

    text = """\
    Hi,
    How are you?
    Check your FCI and the options to subcribe
    https://clientes.balanz.com/"""

    html = """\
    <html>
        <body>
            <p> Hi, <br>
                How are you?<br>
                Check your FCI and the options to subcribe in
                <a href="https://clientes.balanz.com/">Balanz</a><br>
                Balanz has many great FCI.<br>
                Ya puedo mandar links! Estamos cerca de mandarle mails a los hinchas de boca.
            </p>
        </body>
    </html>
    """

    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plaint")
    part2 = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try o render the last part first
    message.attach(part1)
    message.attach(part2)

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
