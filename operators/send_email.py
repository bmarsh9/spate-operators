def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    gmail_user = locker(kwargs["config"],"default","002_guser") ##input:type=text:name=002_guser:label=Enter Gmail email username
    gmail_password = locker(kwargs["config"],"default","002_gpassword") ##input:type=text:name=002_gpassword:label=Enter Gmail password
    to_address = locker(kwargs["config"],"default","002_toaddress") ##input:type=text:name=002_toaddress:label=Where should we send the email? (comma separated)
    subject = locker(kwargs["config"],"default","002_subject") ##input:type=text:name=002_subject:label=Enter the subject of the email
    body = locker(kwargs["config"],"default","002_body") ##input:type=text:name=002_body:label=Enter the body of the email

    sent_from = gmail_user
    if not to_address:
        logging.error("to_address parameter is empty! Exiting...")
        return False
    to_address = to_address.split(",")

    message = 'Subject: {}\n\n{}'.format(subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_address, message)
        server.close()
        logging.info("Email was successfully sent to {}".format(to_address))
    except Exception as e:
        logging.error("Failed to send email to {}. Error:{}".format(to_address,str(e)))
        return False

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
