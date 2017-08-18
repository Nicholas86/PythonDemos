# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

from django.conf.urls import url,include
from . import views


urlpatterns = [
    # url(r'^register/$',views.StudentRegistrationView.as_view(),name='student_registration'),
]