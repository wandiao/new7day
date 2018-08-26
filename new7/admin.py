# coding: utf-8

import inspect

from django.contrib import admin
import new7.models as app_models
# Register your models here.
for attr in dir(app_models):
    model = getattr(app_models, attr)
    if not inspect.isclass(model):
        continue

    try:
        admin.site.register(model)
    except:
        pass


