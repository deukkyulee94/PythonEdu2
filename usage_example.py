from utils.aws_utils import AWSServiceManager

# 프로필과 리전을 지정하여 매니저 생성
aws = AWSServiceManager(profile_name="itm", region_name="ap-northeast-2")

# S3 사용 예제
buckets = aws.s3.list_s3_buckets()
presigned_url = aws.s3.create_get_presigned_url(
    bucket_name='sury-flutter', 
    object_key='assets/assets/images/todos.jpg'
)
print(f'presiged_url : {presigned_url}')
# uri = presiged_url.split('?')
# print(f'uri : {uri[0]}')
# params = uri[1].split('&')
# [print(f'param={param}') for param in params]


# SSM 사용 예제
ssm_params = ['JWT_SECRET_KEY','JWT_SECRET_KEY1']
[print (f'{param} : {aws.ssm.get_ssm_parameter(param)}') for param in ssm_params]


# SES 사용 예제
aws.ses.send_email(
    source_email="sender@example.com",
    to_emails=["recipient@example.com"],
    subject="테스트",
    body_text="테스트 메일입니다."
) 