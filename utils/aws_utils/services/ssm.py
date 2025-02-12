from botocore.exceptions import BotoCoreError, ClientError
    
class AWSSSM:
    def __init__(self, session):
        """
        SSM 클라이언트를 생성합니다.
        :param session: Boto3 세션
        """
        try:
            self.__ssm_client = session.client('ssm')
        except (BotoCoreError, ClientError) as e:
            print(f"Failed to initialize AWS SSM services: {e}")
            raise
    
    # SSM 관련 메서드
    def get_ssm_parameter(self, parameter_name: str, with_decryption: bool = True):
        """
        SSM 파라미터 값을 가져옵니다.
        :param parameter_name: 가져올 파라미터 이름
        :param with_decryption: 암호화된 값을 복호화할지 여부
        :return: 파라미터 값
        """
        try:
            response = self.__ssm_client.get_parameter(
                Name=parameter_name,
                WithDecryption=with_decryption
            )
            return response['Parameter']['Value']
        except ClientError as e:
            if e.response['Error']['Code'] == 'ParameterNotFound':
                return ''
            print(f"Failed to get SSM parameter '{parameter_name}': {e}")
            raise