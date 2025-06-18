from pathlib import Path

# BASE_DIR = racine du projet (où se trouve manage.py)
BASE_DIR = Path(__file__).resolve().parent.parent

# 🔐 Clé secrète (ne jamais publier en production)
SECRET_KEY = 'django-insecure-eu24a8pvctzr_019&94&#6y=n5((@zynz&b1_wv*2=e%gc14nb'

# 🐞 Mode debug activé pour le développement
DEBUG = True

# 🌐 Hôtes autorisés (vide = développement local uniquement)
ALLOWED_HOSTS = []

# 📦 Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 🔧 Tes apps à toi
    'accueil',
    'reservation',
    'pokemon',  # ton app Pokédex
]

# 🧱 Middleware de Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# 🌐 Fichier de configuration principal des URLs
ROOT_URLCONF = 'DjangoProject3.urls'

# 📁 Configuration des templates HTML
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Templates globaux (optionnel)
        'APP_DIRS': True,  # Active les templates dans chaque app
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',  # ⚠️ nécessaire pour certains composants
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# 🚀 Application WSGI
WSGI_APPLICATION = 'DjangoProject3.wsgi.application'

# 💾 Base de données SQLite par défaut
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 🔐 Validation des mots de passe
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

# 🌍 Paramètres de localisation
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Indian/Antananarivo'  # ou 'UTC' si tu préfères
USE_I18N = True
USE_TZ = True

# 🎨 Fichiers statiques (CSS, images, JS)
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# 📦 Fichiers uploadés (optionnel pour images à l’avenir)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# 🆔 Type de champ auto par défaut
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
