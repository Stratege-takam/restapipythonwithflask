#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskdbexemple/")

from flaskdbexemple import init_app as application
application.app.secret_key = 'Exemple apikey'