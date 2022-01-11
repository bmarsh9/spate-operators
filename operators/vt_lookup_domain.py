def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    vt_api_key = locker(kwargs["config"],"default","005_vtapikey") ##input:type=text:name=005_vtapikey:label=Set VT API key:placeholder=Input API key for VirusTotal
    if not vt_api_key:
        logging.error("<vt_api_key> is empty")
        return False
    
    domain_to_lookup = None # update
    if not domain_to_lookup:
        logging.error("<domain_to_lookup> is empty")
        return False
    client = vt.Client(vt_api_key)
    url_id = vt.url_id(domain_to_lookup)
    results = client.get_object("/urls/{}".format(url_id))
    
    #see vars(results) to view all attributes
    return results.last_analysis_stats
    
    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
