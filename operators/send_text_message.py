def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    account_sid = locker(kwargs["config"],"default","003_accountsid") ##input:type=text:name=003_accountsid:label=Enter your account SID - found at twilio.com/console
    auth_token = locker(kwargs["config"],"default","003_authtoken") ##input:type=text:name=003_authtoken:label=Enter authentication token - found at twilio.com/console
    body = locker(kwargs["config"],"default","003_body") ##input:type=text:name=003_body:label=Enter the body of the text message
    _from = locker(kwargs["config"],"default","003_from") ##input:type=text:name=003_from:label=Enter source phone number
    _to = locker(kwargs["config"],"default","003_to") ##input:type=text:name=003_to:label=What phone number should we send the message to?

    if not account_sid or not auth_token:
        logging.error("<account_sid> and <auth_token> is required")
        return False
    
    if not _from or not _to:
        logging.error("<from> and <to> is required")
        return False
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body=body,
            from_="+1{}".format(_from),
            to="+1{}".format(_to)
        )
    if message.sid.get("status") == "sent:
        logging.info("successfully sent the text message to {}".format(to))
    else:
        logging.warning("unable to send the text message. check the raw debug message)
    logging.debug("debug message from twilio:{}".format(str(message.sid)))
    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
