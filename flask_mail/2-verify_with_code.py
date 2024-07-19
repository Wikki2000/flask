import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from os import getenv


"""
install Sendinblue API: pip install sib-api-v3-sdk
Register to get api-key: https://app.brevo.com
"""

def generate_random():
    """ Generate a 6-digits random number """
    from random import randint
    rand_number = randint(1000000, 9999999)
    return rand_number

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = getenv('MAIL_API_KEY')

email = input("Enter your email: ")

# Create an instance of the API class
api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))
sender = {"name": "AGS Company", "email": "wisdomokposin@gmail.com"}
recipient = [{"email": email, "name": "Wisdom Okposin"}]

code = generate_random()

# Email content
subject = "[AGS] Complete your registration"
html_content = f"""
<html>
<head></head>
<body>
    <h1>Hey there!</h1>
    <p>This is your one time confirmation code: {code}</p>
</body>
</html>
"""

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

confirm_code = input("Enter the confirmation code sent to your E-mail: ")

if confirm_code == code:
    print("Registration Successfull")
else:
    print("You enter wrong code")
