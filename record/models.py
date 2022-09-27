from accounts.models import CustomUser
from django.db import models

class Meal(models.Model):
    ''' モデル '''
    # 下のようなテーブル作成
    user = models.ForeignKey(CustomUser, verbose_name = 'ユーザ', on_delete = models.PROTECT) # 外部キー。
    title = models.CharField(verbose_name = 'タイトル', max_length = 40)
    content = models.TextField(verbose_name = 'コメント', blank = True, null = True)
    photo1 = models.ImageField(verbose_name ='写真1', blank=True, null=True)
    photo2 = models.ImageField(verbose_name ='写真2', blank=True, null=True)
    photo3 = models.ImageField(verbose_name ='写真3', blank=True, null=True)
    photo4 = models.ImageField(verbose_name='写真4', blank=True, null=True)
    # rank = models.
    created_at = models.DateTimeField(verbose_name = '作成日時', auto_now_add = True)
    updated_at = models.DateTimeField(verbose_name = '更新日時', auto_now = True)

    class Meta:
        verbose_name_plural = 'Meal'

    def __str__(self):
        return self.title