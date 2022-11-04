import boto3

aws_access_key_id: str = 'AKIA#####'
aws_secret_access_key: str = 'secret_key'
aws_region: str = 'us-east-2'


class code:
    aws_access_key_id = locker(
        kwargs["config"], "default", "009_aws_access_key_id"
    )  ##input:type=text:name=009_aws_access_key_id:label=Set AWS Access Key ID:placeholder=Input AWS Access Key ID
    aws_secret_access_key = locker(
        kwargs["config"], "default", "009_aws_secret_access_key"
    )  ##input:type=text:name=008_maingundomain:label=Set mailgun domain:placeholder=Input mailgun domain
    region = locker(
        kwargs["config"], "default", "009_aws_region"
    )  ##input:type=text:name=009_maingunfromemail:label=Set mailgun from email:placeholder=Input mailgun from email

    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region):
        self.aws_access_key_id: str = aws_access_key_id
        self.aws_secret_access_key: str = aws_secret_access_key
        self.region: str = aws_region

    def connect(self):
        client = boto3.resource('s3',
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key
                                )
        return client

    def list_buckets(self):
        """
        List all buckets
        access needed: s3:ListAllMyBuckets
        """
        client = self.connect()
        for bucket in client.buckets.all():
            print(bucket.name)


if __name__ == "__main__":
    out = code(aws_access_key_id, aws_secret_access_key, aws_region)
    out.list_buckets()

