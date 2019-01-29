# -*- coding: utf-8 -*-
__author__ = 'Alan'

from flask import Flask, render_template
import os
import pymysql


# 全局的Flask核心对象
app = Flask(__name__)

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:root@localhost:3306/movies"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = "38069eb3191dg8r2w9ln5n2l34n64"
app.config['UP_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/")
app.config['IMG_DIR'] = os.path.join(os.path.abspath(os.path.dirname(__file__)), "static/uploads/users/")

app.debug = False


# 蓝图注册
from movie.home import home as home_blueprint
from movie.admin import admin as admin_blueprint
app.register_blueprint(home_blueprint)
app.register_blueprint(admin_blueprint, url_prefix='/admin')


@app.errorhandler(404)
def page_not_found(e):
    return render_template("home/404.html"), 404


