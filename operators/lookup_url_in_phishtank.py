def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    headers = {
        'format': 'json',
        'app_key': '',
    }

    pt_api_key = locker(kwargs["config"],"default","006_ptapikey") ##input:type=text:name=006_ptapikey:label=Set Phishtank API Key:placeholder=Input API key for Phishtank
    if not pt_api_key:
        pt_api_key = ""
        logging.warning("<pt_api_key> is empty. You may hit a lower rate limit.")
    headers["app_key"] = pt_api_key
    domain_to_lookup = None # update
    if not domain_to_lookup:
        logging.error("<domain_to_lookup> is empty")
        return False
    phishtank_url = "http://checkurl.phishtank.com/checkurl/"
    new_check_bytes = domain_to_lookup.encode()
    base64_bytes = base64.b64encode(new_check_bytes)
    base64_new_check = base64_bytes.decode('ascii')
    phishtank_url += base64_new_check
    response = requests.post(url=phishtank_url, headers=headers)
    
    # phishtank API returns data in XML
    results = ET.ElementTree(ET.fromstring(response.text))
    return results

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
