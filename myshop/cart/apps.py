# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
from django.apps import AppConfig


class CartConfig(AppConfig):
    name = 'cart'
