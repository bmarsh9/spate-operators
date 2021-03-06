def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''
    # https://github.com/nithinmurali/pygsheets
    secret_dict = locker(kwargs["config"],"default","004_secretdict") ##input:type=text:name=004_secretdict:label=Oauth credentials:placeholder=e.g. {}
    spreadsheet_key = locker(kwargs["config"],"default","004_sheetkey") ##input:type=text:name=004_sheetkey:placeholder=Key is found in the gsheet url:label=Enter the key of the Google spreadsheet, case sensitive
    sheet_name = locker(kwargs["config"],"default","004_sheetname") ##input:type=text:name=004_sheetname:label=Enter the name of the Google sheet tab, case sensitive
    values = locker(kwargs["config"],"default","004_values") ##input:type=text:name=004_values:label=Enter the values to append to the google sheet, comma separated

    try:
        service_account_info = json.loads(secret_dict)
    except:
        logging.error("failed to load credentials")
        return False
    if not sheet_name or not spreadsheet_key:
        logging.error("<sheet_name> and <spreadsheet_key> is required")
        return False
    
    SCOPES = ('https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive')
    my_credentials = service_account.Credentials.from_service_account_info(service_account_info, scopes=SCOPES)
    gc = pygsheets.authorize(custom_credentials=my_credentials)
    
    sheet = gc.open_by_key(spreadsheet_key)
    wks = sheet.worksheet_by_title(sheet_name)
    cells = wks.get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
    wks.insert_rows(row=len(cells), number=1, values=values.split(","))
    logging.info("added row to the spreadsheet:{}".format(sheet_name))
    
    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
