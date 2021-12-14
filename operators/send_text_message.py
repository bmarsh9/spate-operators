def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    account_sid = locker(kwargs["config"],"default","003_accountsid") ##input:type=text:name=003_accountsid:label=Enter your account SID - found at twilio.com/console
    auth_token = locker(kwargs["config"],"default","003_authtoken") ##input:type=text:name=003_authtoken:label=Enter authentication token - found at twilio.com/console

    if not account_sid or not auth_token:
        logging.error("<account_sid> and <auth_token> is required")
        return False
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=body,
                         from_="+1{}".format(from),
                         to="+1{}".format(to)
                     )
    logging.info("successfully sent the text message to {}".format(to))

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
