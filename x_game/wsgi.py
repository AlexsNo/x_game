import os
import sys
import platform

# путь к проекту
sys.path.insert(0, '/home/c/ce71998/django_0mwio/public_html')
# путь к фреймворку
sys.path.insert(0, '/home/c/ce71998/django_0mwio/public_html/x_game')
# путь к виртуальному окружению
python_version = ".".join(platform.python_version_tuple()[:2])
sys.path.insert(0, f"/home/c/ce71998/django_0mwio//django/lib/python{python_version}/site-packages")
os.environ["DJANGO_SETTINGS_MODULE"] = "x_game.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

