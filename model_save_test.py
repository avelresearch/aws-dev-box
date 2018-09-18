import unittest
import boto3
from moto import mock_s3
from mymodule import MyModel


class TestS3Actor(unittest.TestCase):

    def test_my_model_save(self):
        mock = mock_s3()
        mock.start()

        conn = boto3.resource('s3', region_name='us-east-1')
        conn.create_bucket(Bucket='mybucket')

        model_instance = MyModel('steve', 'is awesome')
        model_instance.save()

        assert conn.Object('mybucket', 'steve').get()['Body'].read().decode() == 'is awesome'

        mock.stop()
