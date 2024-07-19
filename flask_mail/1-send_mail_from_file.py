import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from os import getenv

# Read HTML content from file
def read_html_content(file_path):
    with open(file_path, 'r') as file:
        html_content = file.read()
    return html_content

# Configure API key authorization
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = getenv('MAIL_API_KEY')

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
sender = {"name": "Wikki Company", "email": "wisdomokposin@gmail.com"}
recipient = [{"email": "wisdomokposin@gmail.com", "name": "Wisdom Okposin"}]

# Email subject and HTML content from file
subject = "[AGS] Complete your registration"
html_content = read_html_content('1-email_content.html')

send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
    to=recipient,
    sender=sender,
    subject=subject,
    html_content=html_content,
)

try:
    # Send email
    api_response = api_instance.send_transac_email(send_smtp_email)
    pprint(api_response)
except ApiException as e:
    print(f"Error: {e}")

