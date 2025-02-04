from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute, BooleanAttribute

class TodoModel(Model):
    class Meta:
        table_name = "evan_todo_model"
        region = "ap-northeast-2"

    todo_id = UnicodeAttribute(hash_key=True)
    email = UnicodeAttribute(range_key=True)
    todo = UnicodeAttribute()
    state = BooleanAttribute(default=False)
    created = UnicodeAttribute()

    def to_dict(self):
        return {
            'todo_id': self.todo_id,
            'email': self.email,
            'todo': self.todo,
            'state': self.state,
            'created': self.created
        }

# KST 기준 시간 저장

# 테이블이 존재하지 않으면 생성
if not TodoModel.exists():
    TodoModel.delete_table()
    TodoModel.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
