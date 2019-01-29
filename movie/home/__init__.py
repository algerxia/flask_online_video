# -*- coding: utf-8 -*-
__author__ = 'alan'

from flask import Blueprint

home = Blueprint("home", __name__)
import movie.home.views
