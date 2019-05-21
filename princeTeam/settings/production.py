import os
# from django.conf import settings
from django.conf import settings
from decouple import config

DEBUG = True

DATABASES = settings.DATABASES

# Parse database configuration from $DATABASE_URL
import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['carlosgonzalez.pro']

# EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME')
# EMAIL_HOST= 'smtp.sendgrid.net'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD')

EMAIL_HOST = config('EMAIL_HOST')
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_USE_TLS = config('EMAIL_USE_TLS', cast=bool)
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')#'Onetown Team <noreply@townresidential.com>'
EMAIL_SUBJECT_PREFIX = '[338w15th.com] '
EMAIL_HOST_USER = config('SENDGRID_USERNAME')
EMAIL_HOST_PASSWORD = config('SENDGRID_PASSWORD')