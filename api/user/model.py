from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute

# <HomeDir>/.aws/credentials에 default profile이 설정되어 있어야 함
# IAM에서 액세스키를 발급받아 설정
class UserModel(Model):
    class Meta:
        table_name = "evan_user_model"
        region = "ap-northeast-2"

    email = UnicodeAttribute(hash_key=True)
    name = UnicodeAttribute()
    password = UnicodeAttribute()

if not UserModel.exists():
    UserModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)