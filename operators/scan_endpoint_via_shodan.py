def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''

    shodan_api_key = locker(kwargs["config"],"default","007_shodanapikey") ##input:type=text:name=007_shodanapikey:label=Set Shodan API Key:placeholder=Input API key for Shodan
    if not shodan_api_key:
        shodan_api_key = ""
        logging.warning("<shodan_api_key> is empty")
        return False
    ip_to_lookup = None # update
    if not ip_to_lookup:
        logging.error("<ip_to_lookup> is empty")
        return False

    api = shodan.Shodan(shodan_api_key)

    # Lookup the host
    host = api.host(ip_to_lookup)

    # Print general info
    results = {
      "IP":host['ip_str'],
      "Organization":host.get('org', 'n/a'),
      "Operating System":host.get('os', 'n/a')
    }
    return results

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
