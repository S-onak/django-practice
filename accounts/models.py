from django.db import models
from django.contrib.auth.models import(
    AbstractBaseUser, BaseUserManager, AbstractUser
)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, password, staff=False, admin=False, active=True):  # create_user를 바꾸면 동작 안함
        if not email:
            raise ValueError('이메일을 입력해주세요!')
        if not password:
            raise ValueError('비밀번호를 입력해주세요!')
# user = UserManager.create_user(email='example@example.com, password="password")
# => 정상적으로 작동함. 이유는 함수 내부에 email과 password가 아닌 나머지 필드는 기본값을 설정했기 때문
        
        user = self.model(email = self.normalize_email(email))
        user.set_password(password)     # password를 난수화해서 저장해주는 함수
        user.staff = staff
        user.admin = admin
        user.active = active
        user.save(using=self._db)
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password,
            staff = True,
            admin = True
        )
        return user
    

class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique = True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    active = models.BooleanField(default=True)  # 로그인 할 수 있는가? (휴면계정 여부)
    staff = models.BooleanField(default=False)  # superuser가 아닌 staff
    admin = models.BooleanField(default=False)  # superuser
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()
        
    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_superuser(self):
        return self.admin
    
    def has_perm(self, perm, obj=None):
        return self.admin
    
    def has_module_perms(self, app_label):
        return self.admin