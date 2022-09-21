from django.urls import path
from . import views
app_name = 'record'
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('aaaaaaaa/', views.Index2View.as_view(), name = "index2"),
    # path('record-list', views.RecordListView.as_view(), name = 'record_list') # 記録一覧
]