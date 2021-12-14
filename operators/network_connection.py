def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''
    url = locker(kwargs["config"],"default","url_host") ##input:type=text:name=url_host:label=Enter the hostname for the URL connection:placeholder=Enter the host with http
    verify = locker(kwargs["config"],"default","verify") ##input:type=checkbox:name=verify:label=Verify TLS connection
    headers = locker(kwargs["config"],"default","headers") or {} ##input:type=text:name=headers:label=Set headers:placeholder=Dictionary of headers for the request
    
    # format headers for the request
    try:
        headers = json.loads(headers)
    except:
        logging.warning("Invalid header format. Must be type <dict>")
        headers = {}
    
    # execute the request
    request = requests.get(url,verify=verify,headers=headers)
    if request.ok:
        return request.json()
    else:
        logging.warning("Non 200 status code returned from {}".format(url))
        return None

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
