def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                         from_='+15017122661',
                         to='+15558675310'
                     )

    print(message.sid)

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
