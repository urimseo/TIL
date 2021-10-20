from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model  # 현재 활성화된 유저 모델을 찾아오는 것 

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = get_user_model()  # 현재 meta 클래스에서 찾는거고
        fields = UserCreationForm.Meta.fields

        # 나머지는 상속받은 (부모)의 UserCreationForm.Meta
