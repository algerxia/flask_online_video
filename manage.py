# -*- coding: utf-8 -*-
__author__ = 'Alan'
from movie import app
from movie.models import db
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from movie.models import User


def make_shell_context():
    return dict(app=app, db=db, User=User)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('runserver', Server(host="127.0.0.1", port='9000'))


if __name__ == '__main__':
    manager.run(default_command='runserver')
