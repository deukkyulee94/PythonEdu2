from botocore.exceptions import BotoCoreError, ClientError
    
class AWSSES:
    def __init__(self, session):
        """
        SES 클라이언트를 생성합니다.
        :param session: Boto3 세션
        """
        try:
            self.__ses_client = session.client('ses')
        except (BotoCoreError, ClientError) as e:
            print(f"Failed to initialize AWS SES services: {e}")
            raise

    # SES 관련 메서드
    def send_email(self, source_email: str, to_emails: list, subject: str, body_text: str):
        """
        SES를 사용하여 이메일을 전송합니다.
        :param source_email: 발신자 이메일 주소
        :param to_emails: 수신자 이메일 주소 리스트
        :param subject: 이메일 제목
        :param body_text: 이메일 본문 텍스트
        :return: 메시지 ID
        """
        try:
            response = self.__ses_client.send_email(
                Source=source_email,
                Destination={'ToAddresses': to_emails},
                Message={
                    'Subject': {'Data': subject},
                    'Body': {'Text': {'Data': body_text}}
                }
            )
            return response['MessageId']
        except ClientError as e:
            print(f"Failed to send email to {to_emails}: {e}")
            raise