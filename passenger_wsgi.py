import sys

sys.path.insert(0, "/home/piranti1/<app_name>")

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'demo_pro.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()