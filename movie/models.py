# -*- coding: utf-8 -*-
from movie import app
from werkzeug.security import check_password_hash, generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy(app)

# 用户
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String(255))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(80), unique=True)
    info = db.Column(db.Text)
    img = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True)
    uuid = db.Column(db.String(255), unique=True)
    userlogs = db.relationship('UserLog', backref='user')
    comment = db.relationship('Comment', backref='user')
    movie_fav = db.relationship('MovieFavorite', backref='user')

    # 用于调试
    def __repr__(self):
        return '<User %r>' % self.name

    def check_pwd(self, pwd):
        return check_password_hash(self.pwd, pwd)


# 用户登录日志
class UserLog(db.Model):
    __tablename__ = "userlogs"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<UserLog %r>" % self.id
#
#
# # 标签
class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    movie = db.relationship('Movie', backref='tag')

    def __repr__(self):
        return "<Tag %r>" % self.name


# 电影
class Movie(db.Model):
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(255), unique=True)
    description = db.Column(db.Text)
    logo = db.Column(db.String(255), unique=True)
    star = db.Column(db.SmallInteger)
    play_num = db.Column(db.BigInteger)
    comment_num = db.Column(db.BigInteger)
    area = db.Column(db.String(100))
    release_time = db.Column(db.String(100))
    length = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'))
    comment = db.relationship('Comment', backref='movie')
    movie_fav = db.relationship('MovieFavorite', backref='movie')

    def __repr__(self):
        return "<Movie %r>" % self.title


# 轮播图
class Preview(db.Model):
    __tablename__ = "previews"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), unique=True)
    logo = db.Column(db.String(255), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Preview %r>" % self.title


# 影评
class Comment(db.Model):
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __repr__(self):
        return "<Comment %r>" % self.id


# 收藏
class MovieFavorite(db.Model):
    __tablename__ = "moviefav"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<MovieFavorite %r>" % self.id


# 权限
class Auth(db.Model):
    __tablename__ = "auth"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=True)
    url = db.Column(db.String(100), unique=True)
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Auth %r>" % self.name


# 角色
class Role(db.Model):
    __tablename__ = "roles"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    auths = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    admin = db.relationship('Admin', backref='role')

    def __repr__(self):
        return "<Role %r>" % self.name


# 管理员
class Admin(db.Model):
    __tablename__ = 'admins'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    pwd = db.Column(db.String(255))
    is_super = db.Column(db.SmallInteger)  # 0为管理员
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    admin_log = db.relationship('AdminLog', backref='admin')
    operate_log = db.relationship('OperateLog', backref='admin')

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)


# 管理员登录日志
class AdminLog(db.Model):
    __tablename__ = "adminlogs"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    ip = db.Column(db.String(100))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)


    def __repr__(self):
        return "<AdminLog %r>" % self.id


# 操作日志
class OperateLog(db.Model):
    __tablename__ = "operatelogs"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admins.id'))
    reason = db.Column(db.String(600))
    add_time = db.Column(db.DateTime, index=True, default=datetime.now)
    ip = db.Column(db.String(100))

    def __repr__(self):
        return "<OperateLog %r>" % self.id

# 添加 初始管理员 账号密码权限
if __name__ == '__main__':
    admin = Admin()
    admin.name = 'admin'
    admin.pwd = generate_password_hash('admin123')
    admin.is_super = 1
    db.session.add(admin)
    db.session.commit()



