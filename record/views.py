from django.views import generic
import logging
from django.urls import reverse_lazy
from .forms import MealCreateForm
logger = logging.getLogger(__name__)
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from . models import Meal
from django.shortcuts import get_object_or_404

class OnlyYouMixin(UserPassesTestMixin):  # 日記作成者のみ閲覧できる機能
    raise_exception = True

    def test_func(self):
        # URLに埋め込まれた主キーから日記データを1件取得。取得できなかった場合は404エラー
        meal = get_object_or_404(Meal, pk = self.kwargs['pk'])
        # ログインユーザと日記の作成ユーザを比較し、異なればraise_exeptionの設定に従う
        return self.request.user == meal.user

class IndexView(generic.TemplateView):
    template_name = "index.html"

# 日記一覧表示。LoginRequiredMixinはログインしているユーザじゃないと見れないって設定
class MealListView(LoginRequiredMixin, generic.ListView):
    model = Meal
    template_name = 'meal_list.html'
    paginate_by = 2 # 数字は多分表示する数

    # メソッドのオーバーライド。filterとは抽出。自分が登録した日記を自分だけが見れるという前提だからこうなっている。order_byは表示する順番。
    def get_queryset(self):
        diaries = Meal.objects.filter(user = self.request.user).order_by('-created_at')
        return diaries


# 日記詳細表示のクラス
class MealDetailView(LoginRequiredMixin, OnlyYouMixin, generic.DetailView):
    # 詳細画面を表示するにはモデル（データベースと連携させるモデル）が必要
    model = Meal
    template_name = 'meal_detail.html'

class MealCreateView(LoginRequiredMixin, generic.CreateView):
    model = Meal
    template_name = 'meal_create.html'
    form_class = MealCreateForm
    success_url = reverse_lazy('record:meal_list')

    def form_valid(self, form): # 登録が成功した時の処理。formはユーザが入力したのが入っている
        meal = form.save(commit = False) # 日記をセーブ（登録）する。commit=Falseはまだすべての情報が入っていないからコミットしないって意味
        meal.user = self.request.user # ユーザ名を入れている（ユーザが入力しないでいいようにこっちでユーザ名をセットする）
        meal.save()
        messages.success(self.request, "日記を作成しました。")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "日記の作成に失敗しました。")
        return super().form_invalid(form)

class MealUpdateView(LoginRequiredMixin, OnlyYouMixin, generic.UpdateView): # UpdateViewクラスを継承している
    model = Meal
    template_name = 'meal_update.html'
    form_class = MealCreateForm # 記録作成機能にも使ったフォームを使いまわしてる。

    def get_success_url(self): # オーバーライド
        return reverse_lazy('record:meal_detail', kwargs = {'pk': self.kwargs['pk']})

    def form_valid(self, form): # 更新が成功した時の処理。formはユーザが入力したのが入っている。オーバーライド。
        messages.success(self.request, "日記を更新しました。")
        return super().form_valid(form)

    def form_invalid(self, form): # オーバーライド
        messages.error(self.request, "日記の更新に失敗しました。")
        return super().form_invalid(form)

