#!/usr/bin/env python
import os
import sys

import dotenv

# allow setup.py to be run from any path
# os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))
dotenv_path = os.path.join(str(os.path.expanduser('~')), '.gargantula')
dotenv.load_dotenv(dotenv_path=dotenv_path)

if __name__ == "__main__":
    ENVIRONMENT = os.getenv('ENVIRONMENT')

    if ENVIRONMENT == 'STAGING':
        settings = 'staging'
    elif ENVIRONMENT == 'PRODUCTION':
        settings = 'production'
    else:
        settings = 'development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scrapersite.settings')
    os.environ.setdefault('DJANGO_CONFIGURATION', settings.title())

    from configurations.management import execute_from_command_line

    execute_from_command_line(argv=sys.argv)
