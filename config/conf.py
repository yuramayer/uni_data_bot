from dotenv import load_dotenv
import os

load_dotenv(override=True)

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
ADMINS = str(os.getenv('ADMINS'))
OPENAI_API_KEY = str(os.getenv('OPENAI_API_KEY'))
CLOUD_S3_ID_KEY = str(os.getenv('CLOUD_S3_ID_KEY'))
CLOUD_S3_SECRET_KEY = str(os.getenv('CLOUD_S3_SECRET_KEY'))
BUCKET_NAME = str(os.getenv('BUCKET_NAME'))


admins_ids = [int(admin_id) for admin_id 
              in ADMINS.split(',')]
