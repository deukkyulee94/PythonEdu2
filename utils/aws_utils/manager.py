from botocore.exceptions import BotoCoreError, ClientError
import boto3

from .exceptions import AWSServiceInitError
from .services import AWSS3, AWSSES, AWSSSM

class AWSServiceManager:
    """AWS 서비스들을 관리하는 통합 매니저 클래스"""

    def __init__(self, profile_name: str = None, region_name: str = None):
        """
        AWS 세션을 초기화하고 필요한 AWS 서비스들을 생성합니다.
        
        Args:
            profile_name: AWS CLI 프로필 이름 (선택사항)
            region_name: AWS 리전 이름 (선택사항)
        
        Raises:
            AWSServiceInitError: AWS 서비스 초기화 실패시
        """
        try:
            self.__session = boto3.Session(
                profile_name=profile_name,
                region_name=region_name
            )
            self.s3 = AWSS3(self.__session)
            self.ssm = AWSSSM(self.__session)
            self.ses = AWSSES(self.__session)
        except (BotoCoreError, ClientError) as e:
            raise AWSServiceInitError(f"AWS 서비스 초기화 실패: {str(e)}") 