# -*- coding: utf-8 -*-

VERSION = "1.0dev"

import sys
import os
preloaded_models = set()

def setup_paths():
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    sys.path.insert(0, os.path.join(BASE_DIR, 'packages'))
    sys.path.append(BASE_DIR)
    sys.path.append(os.path.dirname(BASE_DIR))
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

def preload_models():
    from django.conf import settings
    from django.utils.importlib import import_module

    for app_name in settings.INSTALLED_APPS:
        app_module = import_module(app_name)

        try:
            models = import_module('.models', app_name)
        except ImportError:
            continue
        
        preloaded_models.add(models)
 
