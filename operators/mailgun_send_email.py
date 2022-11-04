def code(input, **kwargs):
    """Place your custom code below.
    Must be indented under this function."""
    """
    class to send email via mailgun
    """
    mailgun_api_key = locker(
        kwargs["config"], "default", "008_maingunapikey"
    )  ##input:type=text:name=007_maingunapikey:label=Set mailgun API Key:placeholder=Input API key for mailgun
    mailgun_domain = locker(
        kwargs["config"], "default", "008_maingundomain"
    )  ##input:type=text:name=008_maingundomain:label=Set mailgun domain:placeholder=Input mailgun domain
    from_email = locker(
        kwargs["config"], "default", "008_maingunfromemail"
    )  ##input:type=text:name=009_maingunfromemail:label=Set mailgun from email:placeholder=Input mailgun from email

    """Default return is True. If you want to return something else, do so above.
    If the return is False, the workflow will NOT proceed."""

    if not mailgun_api_key:
        logging.error("mailgun_api_key is empty")
        return False

    if not mailgun_domain:
        logging.error("mailgun_domain is empty")
        return False

    if not from_email:
        logging.error("from_email is empty")
        return False

    if not attachments:
        return requests.post(
            "https://api.mailgun.net/v3/{0}/messages".format(mailgun_domain),
            auth=("api", mailgun_api_key),
            data={
                "from": from_email,
                "to": [to_email],
                "subject": subject,
                "text": text,
            },
        )

    else:
        return requests.post(
            "https://api.mailgun.net/v3/{0}/messages".format(self.mailgun_domain),
            auth=("api", self.api_key),
            files=[("attachment", open(attachment))],
            data={
                "from": self.from_email,
                "to": [to_email],
                "cc": [cc_email],
                "subject": subject,
                "text": text,
                "html": html,
            },
        )
    return input
