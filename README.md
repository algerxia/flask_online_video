# flask_online_video
  该项目是基于flask+fembed(第三方免费视频托管服务)搭建的一个在线电影网站。
##### Dependencies
  python3.6 +  
  mysql 5.7 +  
  jwplayer(option)  
  fembed(账号)

##### 主界面  
<img src="./screenshots/Screenshot from 2018-07-14 19-25-49.png" alt="主界面" title="主界面" width="100%" height="100%" />

##### 视频播放页面   
<img src="./screenshots/Screenshot from 2018-07-15 10-36-31.png" alt="主界面" title="主界面" width="100%" height="100%" />

##### 用户中心界面   
<img src="./screenshots/Screenshot from 2018-07-14 19-29-00 - 1.png" alt="主界面" title="主界面" width="100%" height="100%" />  

##### 使用说明  

1. git clone https://github.com/moleen/flask_online_video.git
2. cd flask_online_video
3. pipenv install(没有安装pipenv的) -> `pip install pipenv`
4. 创建数据库movies, 命令行执行`python manage.py shell` 在python shell中创建表`db.create_all()`, 执行models.py, 初始化管理员
5. python manage.py
6. enjoy it !

##### 第三方嵌入式视频服务
- [fembed](http://www.fembed.com)(An amazing video sharing platform - Free - Fast - Friendly.)
- [openload](https://openload.co)
- [streamcherry](https://streamcherry.com)
 上面三个都提供非常友好的API, 有兴趣的同学可以把它们的上传API集成到后台管理系统。 其中，fembed除了可以上传视频，转换视频外，还有一个非常nice的torrent模块，支持bt下载(下载速度相当可观哦)

