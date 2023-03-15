
import os

from django.core.wsgi import get_wsgi_application

path = '/home/test/taskmanager/taskmanager/mysite'
if path not in sys.path:
sys.path.append(path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'taskmanager.settings')

application = get_wsgi_application()
