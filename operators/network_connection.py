def code(input, **kwargs):
    '''Place your custom code below.
    Must be indented under this function.'''
    url = locker(kwargs["config"],"default","url_host") ##input:type=text:name=url_host:label=Enter the hostname for the URL connection:placeholder="e.g http://test.com"
    r = request.get(url)
    if r.ok:
        return r.json()
    else:
        logging.warning("network request to {} failed".format(url))

    '''Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed.'''
    return input
