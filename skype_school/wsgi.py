"""
WSGI config for skype_school project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""
import os
import sys
#import site

sys.path.append('/var/www/python/skype_school/')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "skype_school.settings")
#site.addsitedir('/home/arkhangl/python27/lib/python2.7/site-packages')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
