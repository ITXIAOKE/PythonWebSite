##1，创建项目test03

进入虚拟环境py3_space01。

>workon  py3_space01

创建项目test03。

django-admin startproject test03

![这里写图片描述](http://img.blog.csdn.net/20170627091746977?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

打开test03/settings.py文件，找到DATABASES项，默认使用SQLite3数据库

![这里写图片描述](http://img.blog.csdn.net/20170627091759020?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##2，mysql数据库创建及配置
修改为使用MySQL数据库，代码如下:

>将引擎改为mysql，提供连接的主机HOST、端口PORT、数据库名NAME、用户名USER、密码PASSWORD。

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'test03', #数据库名字，
        'USER': 'root', #数据库登录用户名
        'PASSWORD': 'xiaoke', #数据库登录密码,我自己修改了
        'HOST': 'localhost', #数据库所在主机（公司中写真实主机地址）
        'PORT': '3306', #数据库端口
    }
}
```

>注意：数据库test2 Django框架不会自动生成，需要我们自己进入mysql数据库去创建。

下面是手动创建数据库，打开新终端，在命令行登录mysql，创建数据库test2。

>注意：设置字符集为utf8
create database test2 charset=utf8;

![这里写图片描述](http://img.blog.csdn.net/20170627093006455?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##3，创建booktest应用

进入test03目录，创建应用booktest

> cd test03
python manage.py startapp booktest

![这里写图片描述](http://img.blog.csdn.net/20170627103749374?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##4，注册booktest应用
将应用booktest注册到项目中：打开test03/settings.py文件，找到INSTALLED_APPS项，加入如下代码：

![这里写图片描述](http://img.blog.csdn.net/20170627103733431?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##5,定义模型类
+ 模型类被定义在“应用/models.py”文件中，此例中为“booktest/models.py”文件。
+ 模型类必须继承自Model类，位于包django.db.models中。
+ 对于重要数据使用逻辑删除。

##6,具体模型代码

```
# 定义图书模型类BookInfo
class BookInfo(models.Model):
    # 图书名称，唯一
    btitle = models.CharField(max_length=50, unique=True)
    bpub_date = models.DateField()
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    # 逻辑删除，默认不删除
    idDelete = models.BooleanField(default=False)

# 定义英雄模型类HeroInfo
class HeroInfo(models.Model):
    # 英雄姓名，不唯一，可以有重名的英雄
    hname=models.CharField(max_length=50,unique=False)
    # 英雄性别，默认False为男性，也可以设为Integer类型，0或者1
    hgender=models.BooleanField(default=False)
    isDelete=models.BooleanField(default=False)
    # 英雄的描述
    hcontent=models.CharField(max_length=500)
    # 图书与英雄的关系为一对多的关系，所以属性定义在英雄的模型类中
    hbook=models.ForeignKey('BookInfo')
    
```

##7,迁移
生成迁移文件。

>python manage.py makemigrations

执行迁移。

>python manage.py migrate

![这里写图片描述](http://img.blog.csdn.net/20170627152254047?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

打开数据库的命令行，查看当前所有表如下图：

![这里写图片描述](http://img.blog.csdn.net/20170627152311509?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

表booktest_bookinfo结构如：

>默认值并不在数据库层面生效，而是在django创建对象时生效。

![这里写图片描述](http://img.blog.csdn.net/20170627152609153?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

表booktest_heroinfo结构如下：

>Django框架会根据关系属性生成一个关系字段，并创建外键约束。

![这里写图片描述](http://img.blog.csdn.net/20170627152622929?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##8,建立测试数据
+ 在数据库命令行中，复制如下语句执行，向booktest_bookinfo表中插入测试数据：

```
insert into booktest_bookinfo(btitle,bpub_date,bread,bcomment,isDelete) values
('射雕英雄传','1980-5-1',12,34,0),
('天龙八部','1986-7-24',36,40,0),
('笑傲江湖','1995-12-24',20,80,0),
('雪山飞狐','1987-11-11',58,24,0);
```
![这里写图片描述](http://img.blog.csdn.net/20170627153247617?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

+ 再复制如下语句执行，向booktest_heroinfo表中插入测试数据：

```

insert into booktest_heroinfo(hname,hgender,hbook_id,hcontent,isDelete) values
('郭靖',1,1,'降龙十八掌',0),
('黄蓉',0,1,'打狗棍法',0),
('黄药师',1,1,'弹指神通',0),
('欧阳锋',1,1,'蛤蟆功',0),
('梅超风',0,1,'九阴白骨爪',0),
('乔峰',1,2,'降龙十八掌',0),
('段誉',1,2,'六脉神剑',0),
('虚竹',1,2,'天山六阳掌',0),
('王语嫣',0,2,'神仙姐姐',0),
('令狐冲',1,3,'独孤九剑',0),
('任盈盈',0,3,'弹琴',0),
('岳不群',1,3,'华山剑法',0),
('东方不败',0,3,'葵花宝典',0),
('胡斐',1,4,'胡家刀法',0),
('苗若兰',0,4,'黄衣',0),
('程灵素',0,4,'医术',0),
('袁紫衣',0,4,'六合拳',0);

```
![这里写图片描述](http://img.blog.csdn.net/20170627153300631?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

##9,定义视图
+ 打开booktest/views.py文件，定义视图代码如下：

```
from datetime import date
from django.shortcuts import render,redirect
from booktest.models import BookInfo

# 查询所有图书并显示的视图函数
def index(request):
    books=BookInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books})

# 新增图书视图视图函数
def addBook(request):
    book=BookInfo()
    book.btitle='晓可自传'
    book.bpub_date=date(2017,6,27)
    book.save()
    # return HttpResponse('ok') 
    # 重定向跳转到首页
    return redirect('/index/')

# 根据图书id删除一本书的视图函数
def delBook(request,bid):
    # 查询出图书
    b=BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index/')


```

##10,配置url
打开test03/urls.py文件，配置url如下：

```
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # 配置成功之后去booktest的urls文件中找对应的视图函数
    url(r'^',include('booktest.urls'))
]
```

在booktest应用下创建urls.py文件，代码如下：

```
from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^index/$',views.index),
    url(r'^addBook/$',views.addBook),
    url(r'^delBook/$',views.delBook)
]

```

##11,创建模板

+ 打开test03/settings.py文件，配置模板查找目录TEMPLATES的DIRS。

>'DIRS': [os.path.join(BASE_DIR,'templates')],

+ 模板代码如下：

```
<html>
<head>
    <title>Python-晓可的图书网站</title>
</head>
<body>
<a href="/addBook/">创建</a>
<ul>
{%for book in books%}

<li>{{book.btitle}}--<a href="/delBook{{book.id}}/">删除</a></li>

{%endfor%}
</ul>
</body>
</html>
```

##12,运行

+ 运行服务器

> python manage.py runserver

+ 运行结果如下：（截取一部分图片）

![这里写图片描述](http://img.blog.csdn.net/20170627163258178?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)

+ 查看booktest_bookinfo表信息，可以得知增加和删除图书信息

![这里写图片描述](http://img.blog.csdn.net/20170627163242801?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvdTAxNDc0NTE5NA==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/SouthEast)


