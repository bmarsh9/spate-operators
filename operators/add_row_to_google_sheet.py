def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''
    # https://github.com/nithinmurali/pygsheets
    secret_dict = locker(kwargs["config"],"default","004_secretdict") ##input:type=text:name=004_secretdict:label=Oauth credentials:placeholder=e.g. {}
    sheet_key = locker(kwargs["config"],"default","004_sheetkey") ##input:type=text:name=004_sheetkey:label=Enter the key of the Google sheet:placeholder=Enter sheet key

    try:
        service_account_info = json.loads(secret_dict)
    except:
        logging.error("failed to load credentials")
        return False
    if not sheet_name:
        logging.error("<sheet_name> is required")
        return False
    
    SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
    my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    gc = pygsheets.authorize(custom_credentials=my_credentials)
    
    sheet = gc.open_by_key(sheet_key)
    
    
    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
