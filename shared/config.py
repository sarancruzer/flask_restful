# config.py
class MYSQL:
    PORT = 3306
    HOST = '0.0.0.0'
    USER = 'root'
    PASS = 'root'
    DATABASE = 'aianr'
    
# config.py
class Config:
    APP_NAME = 'myapp'
    SECRET_KEY = 'secret-key-of-myapp'
    ADMIN_NAME = 'administrator'

    AWS_DEFAULT_REGION = 'ap-northeast-2'
    
    STATIC_PREFIX_PATH = 'static'
    ALLOWED_IMAGE_FORMATS = ['jpg', 'jpeg', 'png', 'gif']
    MAX_IMAGE_SIZE = 5242880 # 5MB

    
class DevelopmentConfig(Config):
    #DEBUG = True
    DATABASE_URI = 'mysql://root:root@localhost/aianr'    
    SERVER_NAME = '0.0.0.0'
    
class TestConfig(Config):
    DEBUG = True
    TESTING = True
    
    AWS_ACCESS_KEY_ID = 'aws-access-key-for-test'
    AWS_SECERT_ACCESS_KEY = 'aws-secret-access-key-for-test'
    AWS_S3_BUCKET_NAME = 'aws-s3-bucket-name-for-test'
    
    DATABASE_URI = 'database-uri-for-dev'
  

class ProductionConfig(Config):
    DEBUG = False

    AWS_ACCESS_KEY_ID = 'aws-access-key-for-prod'
    AWS_SECERT_ACCESS_KEY = 'aws-secret-access-key-for-prod'
    AWS_S3_BUCKET_NAME = 'aws-s3-bucket-name-for-prod'

    DATABASE_URI = 'database-uri-for-dev'


class CIConfig:
    SERVICE = 'travis-ci'
    HOOK_URL = 'web-hooking-url-from-ci-service'
   
