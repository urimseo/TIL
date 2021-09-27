from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model  

User = get_user_model() # 현재 프로젝트에서 활성화된 사용자 모델을 반환. 

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name'] # 수정 시 필요한 필드만 선택해서작성

# update에서 UserChangeForm을 CustomUserChangeForm으로 변경하여 작성 