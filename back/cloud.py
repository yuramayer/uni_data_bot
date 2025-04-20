import boto3
from botocore.config import Config
import json
from config.conf import CLOUD_S3_ID_KEY, CLOUD_S3_SECRET_KEY, BUCKET_NAME


s3 = boto3.client(
        aws_access_key_id=CLOUD_S3_ID_KEY,
        aws_secret_access_key=CLOUD_S3_SECRET_KEY,
        service_name='s3',
        endpoint_url='https://storage.yandexcloud.net',
        region_name='ru-central1',
        config=Config(signature_version='s3v4') 
)


def get_key(timestamp: str, user_id: int) -> str:
    date, time_str = timestamp.split('T')
    hour = time_str[:2]
    key = f"chat_logs/date={date}/hour={hour}/{user_id}_{timestamp}.json"
    return key


def send_logs(logs_json: dict, key: str):

    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=key,
        Body=json.dumps(logs_json, 
                        ensure_ascii=False).encode('utf-8')
    )
