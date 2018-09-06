# from django.conf.urls.defaults import *
from django.contrib import admin
from django.urls import path

admin.autodiscover()

urlpatterns = ['',
    path('', 'example_app.views.display_my_config'),
    path('admin/', admin.site.urls),
]
