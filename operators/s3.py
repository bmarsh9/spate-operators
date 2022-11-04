import boto3

aws_access_key_id: str = 'AKIA#####'
aws_secret_access_key: str = 'secret_key'
region: str = 'us-east-2'


class code:
    def __init__(self, aws_access_key_id, aws_secret_access_key, region):
        self.aws_access_key_id: str = aws_access_key_id
        self.aws_secret_access_key: str = aws_secret_access_key
        self.region: str = region

    def list_buckets(self):
        client = boto3.resource('s3',
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key
                                )
        for bucket in client.buckets.all():
            print(bucket.name)


if __name__ == "__main__":
    out = code(aws_access_key_id, aws_secret_access_key, region)
    out.list_buckets()
