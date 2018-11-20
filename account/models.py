from django.db import models
from django.contrib.auth.hashers import make_password, check_password


# 加密  不可逆
#
class User(models.Model):
    username = models.CharField(max_length=64)
    _password = models.CharField(max_length=128)

    class Meta:
        db_table = 'user'

    # property  对数据进行计算 检验

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = make_password(password, 'pbkdf2_sha256')

    def verify_password(self, password):
        return check_password(password, self._password)
