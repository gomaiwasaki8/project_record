import os
from django import forms
from django.core.mail import EmailMessage
from .models import Meal

# class RecordListForm(forms.form):

class InquiryForm(forms.Form):
    name = forms.CharField(label = 'お名前', max_length = 30)
    email = forms.EmailField(label = 'メールアドレス')
    title = forms.CharField(label = 'タイトル', max_length = 30)
    message = forms.CharField(label = 'メッセージ', widget = forms.Textarea)

    # 無くても動くが、placeholderは初期値を設定している。入力欄に薄い字が表示される。classはデザインの設定
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # classはデザインの設定。
        self.fields['name'].widget.attrs['class'] = 'form-control'
        self.fields['name'].widget.attrs['placeholder'] = 'お名前をここに入力してください。'

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスをここに入力してください。'

        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs['placeholder'] = 'タイトルをここに入力してください。'

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージをここに入力してください。'

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        title = self.cleaned_data['title']
        message = self.cleaned_data['message']

        subject = 'お問い合わせ {}'.format(title)
        message = '送信者名：{0}\nメールアドレス：{1}\nメッセージ：\n{2}'.format(name, email, message)
        from_email = os.environ.get('FROM_EMAIL') # environとは環境って意味なので環境変数を使っている！
        to_list = [
            os.environ.get('FROM_EMAIL')
        ]
        cc_list = [
            email
        ]
        # ↑の色々を全部messageに集約して送信している
        message = EmailMessage(subject = subject, body = message, from_email = from_email, to = to_list, cc = cc_list)
        message.send()

class MealCreateForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ('title', 'content', 'photo1', 'photo2', 'photo3',)

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'