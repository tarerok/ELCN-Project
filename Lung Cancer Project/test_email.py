import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

# Define the email
message = Mail(
    from_email='tarerok@gmail.com',       # Must be a verified sender in SendGrid
    to_emails='ethan.carmona@gmail.com',     # Replace with your own email
    subject='Project Test Email',
    plain_text_content='Good Afternoon, this is a test email.'
)

try:
    sg = SendGridAPIClient(SENDGRID_API_KEY)
    response = sg.send(message)
    print(f"Email sent! Status code: {response.status_code}")
except Exception as e:
    print(f"Error sending email: {e}")
