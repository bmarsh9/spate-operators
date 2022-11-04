import boto3

aws_access_key_id: str = 'access_key'
aws_secret_access_key: str = 'secret_key'
region: str = 'us-east-2'


# documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/logs.html

class code(object):
    def __init__(self, access_key_id, secret_access_key, aws_region):
        self.aws_access_key_id: str = access_key_id
        self.aws_secret_access_key: str = secret_access_key
        self.region: str = aws_region

    def all_log_groups(self):
        self.log_groups = self.list_log_groups()
        return self.log_groups

    def connect(self):
        return boto3.client('logs', aws_access_key_id=aws_access_key_id,
                            aws_secret_access_key=aws_secret_access_key,
                            region_name=region)

    def list_log_groups(self):
        client = self.connect()
        log_groups = client.describe_log_groups()
        for log_group in log_groups['logGroups']:
            yield log_group['logGroupName']

    def list_log_streams(self, log_group_name):
        client = self.connect()
        return client.describe_log_streams(logGroupName=log_group_name)

    def get_log_group_fields(self, log_group_name):
        client = self.connect()
        return client.describe_log_groups(logGroupNamePrefix=log_group_name)

    def get_log_streams_for_all_log_groups(self):
        log_groups = self.list_log_groups()
        for log_group in log_groups:
            log_streams = self.list_log_streams(log_group)
            if log_streams['logStreams']:
                for log_stream in log_streams['logStreams']:
                    yield log_group, log_stream['logStreamName']

    def get_log_events(self, log_group_name, log_stream_name):
        client = self.connect()
        return client.get_log_events(logGroupName=log_group_name, logStreamName=log_stream_name)


if __name__ == "__main__":
    client = code(aws_access_key_id, aws_secret_access_key, region)

    # print all log groups
    print(list(client.all_log_groups()))

    ### get all log events for a log group and log stream
    # cloudwatch_logs_group_list = list(client.list_log_groups())  # list of log groups
    # log_group_name = cloudwatch_logs_group_list[0]  # get the first log group name
    # log_stream_name = client.list_log_streams(log_group_name)['logStreams'][0]['logStreamName']  # get the first log stream name
    # print("group name: " + log_group_name + "log stream name:" + log_stream_name)
    # print(client.get_log_events(log_group_name, log_stream_name))

    ### list fields in log group
    # log_group = '/aws/kinesis-analytics/wildrydes'
    # get_log_group_fields = client.get_log_group_fields(log_group)
    # print(get_log_group_fields)
