from enum import Enum, auto
from botocore.exceptions import BotoCoreError, ClientError

class S3PreSignedURLOpType(Enum):
    GET = auto()
    PUT = auto()
    
class AWSS3:
    def __init__(self, session):
        """
        S3 클라이언트를 생성합니다.
        :param session: Boto3 세션
        """
        try:
            self.__s3_client = session.client('s3')
        except (BotoCoreError, ClientError) as e:
            print(f"Failed to initialize AWS S3 services: {e}")
            raise
    
    # S3 관련 메서드
    def list_s3_buckets(self) -> list:
        """
        S3 버킷 목록을 반환합니다.
        :return: 버킷 이름 리스트
        """
        try:
            response = self.__s3_client.list_buckets()
            return [bucket['Name'] for bucket in response.get('Buckets', [])]
        except ClientError as e:
            print(f"Failed to list S3 buckets: {e}")
            raise
    # S3 관련 메서드
    def __create_presigned_url(self, bucket_name: str, object_key: str, 
                             url_type: S3PreSignedURLOpType = S3PreSignedURLOpType.GET, 
                             expiration: int = 3600) -> str:
        """
        버킷에 있는 객체를 공유하기 위한 서명된 URL을 생성한다.
        :param region: 버킷의 리전
        :param url_type: Pre Signed URL 생성시 줄수 있는 권한 GET, PUT
        :param bucket_name: 버킷명
        :param object_key: 서명된 URL 대상 객체 키
        :param expiration: 서명된 URL의 만료 시간
        :return: 문자열인 서명된 URL. 오류가 발생하면 None을 리턴.
        """
        # s3_client = _find_client_from_cache_for_put(region)

        try:
            presigned_url = self.__s3_client.generate_presigned_url(
                ClientMethod=f'{url_type.name.lower()}_object',
                Params={'Bucket': bucket_name,
                        'Key': object_key},
                ExpiresIn=expiration,
                HttpMethod=url_type.name)
        except ClientError as e:
            print(f"Failed to create S3 {url_type.name.upper} presigned url: {e}")
            raise
        return presigned_url
    
    def create_get_presigned_url(self, bucket_name: str, object_key: str, expiration: int = 3600) -> str:
        """
        버킷에 있는 객체를 공유하기 위한 서명된 URL을 생성한다.
        :param region: 버킷의 리전
        :param url_type: Pre Signed URL 생성시 줄수 있는 권한 GET, PUT
        :param bucket_name: 버킷명
        :param object_key: 서명된 URL 대상 객체 키
        :param expiration: 서명된 URL의 만료 시간
        :return: 문자열인 서명된 URL. 오류가 발생하면 None을 리턴.
        """
        return self.__create_presigned_url(bucket_name, object_key, S3PreSignedURLOpType.GET, expiration)
    
    
    def create_put_presigned_url(self, bucket_name: str, object_key: str, expiration: int = 3600) -> str:
        """
        버킷에 있는 객체를 공유하기 위한 서명된 URL을 생성한다.
        :param region: 버킷의 리전
        :param url_type: Pre Signed URL 생성시 줄수 있는 권한 GET, PUT
        :param bucket_name: 버킷명
        :param object_key: 서명된 URL 대상 객체 키
        :param expiration: 서명된 URL의 만료 시간
        :return: 문자열인 서명된 URL. 오류가 발생하면 None을 리턴.
        """
        return self.__create_presigned_url(bucket_name, object_key, S3PreSignedURLOpType.PUT, expiration)
    