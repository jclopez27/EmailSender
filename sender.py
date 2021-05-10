import smtplib
import ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "juandevelopmet@gmail.com"  # Enter your address
    password = input('Type your password and press enter: ')

    subject = "An email with attachment from Python"
    body = "This is an email with attachment sent from Python.\n" \
           "El finde que viene jugamos contra boca. Acá tenes un estudio de la" \
           "construcción de la rivalidad River-Boca.\n #AcaVanTusImpuestos."
    # Create e multipart message and set headers
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    filename = "RivalidadRiverBoca.pdf"

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename = {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Create a secure SSL context
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)


def send_email_with_html(receiver_email):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "juandevelopmet@gmail.com"  # Enter your address
    password = input('Type your password and press enter: ')

    # Create e multipart message and set headers
    message = MIMEMultipart("alternative")
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Email with plain-text and HTML version"

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
