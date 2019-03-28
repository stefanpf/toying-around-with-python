import os
import smtplib
import requests
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS_SENDER = os.environ.get('EMAIL_ADDRESS_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
EMAIL_ADDRESS_RECEIVER = os.environ.get('EMAIL_ADDRESS_RECEIVER')
MONITOR_URL = os.environ.get('MONITOR_URL')
SMTP_SERVER = os.environ.get('SMTP_SERVER')

response = requests.get(MONITOR_URL, timeout=5)

# if response.status_code != 200:
with smtplib.SMTP(SMTP_SERVER, 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS_SENDER, EMAIL_PASSWORD)

    subject = f'{MONITOR_URL} IS DOWN!'
    body = f"""GET request failed, status code != 200.\n\n
           Received status code: {response.status_code}
            """
    msg = f'Subject: {subject}\n\n{body}'
    smtp.sendmail(EMAIL_ADDRESS_SENDER, EMAIL_ADDRESS_RECEIVER, msg)
