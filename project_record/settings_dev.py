# 仮想環境用
from.settings_common import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(2vi+8dq_n7a1e&2xu9z1cdos*s$@ihm8@tr0tmj37%*swz092'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# ロギング設定
LOGGING = {
    'version':1, # 固定
    'disable_existing_loggers': False,

    # ロガーの設定
    'loggers': {
        # Djangoが利用するロガー
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        # diaryアプリケーションが利用するロガー
        'record': {
            'handlers':['console'],
            'level': 'DEBUG',
        },
    },

    # ハンドラの設定
    'handlers': {
        'console' :{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        },
    },

    # フォーマッタの設定
    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '[%(levelname)s]',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s'
            ])
        },
    }
}

# メール処理で使うバックエンドを定義（開発時のメール配信先設定）つまり入力されたものがコンソールに表示される
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# メディアファイルの配置場所を指定
MEDIA_ROOT = os.path.join(BASE_DIR, 'media') # BASE_DIRはsettings_commonで定義されている