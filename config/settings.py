INSTALLED_APPS = [
    ...
    'rest_framework',
    'apps.content',
    'apps.analytics',
    'apps.llm_engine',
    'apps.reports',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'content_db',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
