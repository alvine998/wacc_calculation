import sys

sys.path.insert(0, "/home/piranti1/appku/demo_pro")

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'mainmenu.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()