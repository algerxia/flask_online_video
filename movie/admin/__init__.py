# -*- coding: utf-8 -*-
__author__ = 'Alan'

from flask import Blueprint


admin = Blueprint('admin', __name__)
import movie.admin.views
