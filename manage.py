#!/usr/bin/env python

import os
import sys
import re
from intelectual import connect_db, setup_paths
setup_paths()

os.environ['DJANGO_SETTINGS_MODULE'] = 'intelectual.settings'
__import__(os.environ['DJANGO_SETTINGS_MODULE'])
settings = sys.modules[os.environ['DJANGO_SETTINGS_MODULE']]
connect_db()

if __name__ == "__main__":
    from django.core.management import execute_manager
    execute_manager(settings)