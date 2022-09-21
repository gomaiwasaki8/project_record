from django.contrib import admin
# 同じディレクトリのmodelsファイルのMealっていうのをインポート
from . models import Meal

admin.site.register(Meal)