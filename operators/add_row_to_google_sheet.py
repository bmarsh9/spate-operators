def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''
    # https://github.com/nithinmurali/pygsheets
    secret_dict = locker(kwargs["config"],"default","004_secretdict") ##input:type=text:name=004_secretdict:label=Oauth credentials :placeholder=e.g. {}

    try:
        service_account_info = json.loads(secret_dict)
    except:
        logging.error("faile to load credentials")
        return False
    
    SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
    my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    gc = pygsheets.authorize(custom_credentials=my_credentials)
    
    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
