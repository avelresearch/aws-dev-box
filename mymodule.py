import boto3


class MyModel(object):


    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key=self.name, Body=self.value)

    def scan(self):
        s3 = boto3.client('s3', region_name='us-east-1')
        s3.put_object(Bucket='mybucket', Key='tests/a.txt', Body='BodyA')
        s3.put_object(Bucket='mybucket', Key='tests/b.txt', Body='BodyB')

        _s3 = boto3.resource('s3')
        bucket = _s3.Bucket('mybucket')

        objects = bucket.objects.all()


        return objects
