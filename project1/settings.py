"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 2.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c7_h^z_hm5g=!2@j(vq2r+bl78-cd)h1obt+qxxa6$-vu=-q##'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',   #django restful框架
    'api',
    'app1',
    'app2',
]

REST_FRAMEWORK = {
    #这里配置了分页处理，每页最多10个项目
    #'DEFAULT_PAGINATION_CLASS':'api.custompagination.LimitOffsetPaginationWithUpperBound',
    'PAGE_SIZE': 10,
    'DEFAULT_FILTER_BACKENDS': (
        #这里配置了排序、过滤、搜索器
        #'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',
        'rest_framework.filters.SearchFilter',
    ),
    #这里配置了用户认证，管理员才可以更改内容，未登录不能更改
    'DEFAULT_AUTHENTICATION_CLASSES':(
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    #这里配置了访问次数限制，过多会返回429错误 too many requests
    'DEFAULT_THROTTLE_CLASSES': (
        'rest_framework.throttling.AnonRateThrottle',
        'rest_framework.throttling.UserRateThrottle',
    ),
    #这里配置了访问次数，anon代表匿名用户，user代表已登录用户，entries是我自己设置的作用域，300/hour代表最多300次每小时
    'DEFAULT_THROTTLE_RATES': {
        'anon': '300/hour',
        'user': '100/hour',
        'entries': '200/hour',
    },
    'DEFAULT_VERSIONING_CLASS':'rest_framework.versioning.NamespaceVersioning',
}

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, '/app1/templates'), os.path.join(BASE_DIR, '/app2/templates'), os.path.join(BASE_DIR, '/api/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project1.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST':'10.22.3.62',
        'PORT':'3306',
        'NAME': 'test',
        'USER': 'root',
        'PASSWORD': 'root123',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(BASE_DIR, '/app2/static/'),
)

#对密码进行加密
from hashlib import sha1
def hide_passwd(str):
    s = sha1()
    s.update(str.encode())
    return s.hexdigest()

#github
GITHUB_APP_ID = '4ed0674a23223f72a936'

GITHUB_KEY = '7b6af836aaaf2fe1253ffc6417aa06e95de8f55c'

GITHUB_CALLBACK_URL = 'http://127.0.0.1:8000/app1/git_check'  #填写你的回调地址

#QQ
QQ_APP_ID = ''

QQ_KEY = ''

QQ_CALLBACK_URL = 'http://127.0.0.1:8000/app1/qq_check'    #填写你的回调地址


