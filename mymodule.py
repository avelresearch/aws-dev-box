import boto3


class MyModel(object):


    def __init__(self, name, value):
        self.s3 = boto3.resource('s3')
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)

    def scan_path(self):
        bucket = self.s3.Bucket('mybucket')
        objects = bucket.objects.filter(Prefix=self.name)
        return objects
