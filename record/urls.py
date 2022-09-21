from django.urls import path
from . import views
app_name = 'record'
urlpatterns = [
    path('', views.IndexView.as_view(), name = "index"),
    path('meal-list', views.MealListView.as_view(), name = 'meal_list'), # 記録一覧
    path('meal-create/', views.MealCreateView.as_view(), name = 'meal_create'), # 新規作成機能
    path('meal-detail/<int:pk>/', views.MealDetailView.as_view(), name = 'meal_detail'), # 記録詳細機能

]