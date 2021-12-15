# 数据库导入说明

进入mysql command line Client,新建数据库：

```
create database $你的名字;
```

打开`sqltxt.py`脚本，修改第三行

```python
conn=pymysql.connect(host="localhost",user='root',passwd='root',database='jwsys',port=3306,use_unicode=True, charset="utf8")
```

user,passwd和database分别改成自己的名称和密码，database是你刚才新建的数据库名。

然后注释掉倒数第三行的`conn.commit()`代码，试运行一下。

如果没有抛出异常，表示可以通过，直接加上`conn.commit()`运行即可。

然后你去自己数据库上查查看看有没有成功导入。

中途控制台输出的都是导入失败的，没有关系，能用就行。

# 后端Django使用说明

如果电脑里没装libnum,建议先装一下：

```shell
pip install libnum 
```

修改`./settings.py`的这个部分：

```python
DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '***',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

name和user和password和上面一样，改成你的。

在shell里运行，查看是否报错

```shell
python manage.py makemigrations
python manage.py migrate
```

`/admin`路由 账户名：fyhssgss， 密码：123456，在这里可以查看数据库连接，并查看所有模型是否导入。

检查无误后运行

```shell
python manager.py runserver
```

建立了一个叫做`eduadmin`的应用，所有请求需要在`/edu`路由下进行转发。

具体位置：

- 应用内部路由：`/eduadmin/urls.py`
- 实现所有功能：`/eduadmin/views.py`

