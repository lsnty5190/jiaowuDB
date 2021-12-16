<!--
 * @Author: your name
 * @Date: 2021-12-15 14:02:08
 * @LastEditTime: 2021-12-16 13:21:34
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \jiaowuDB\README.md
-->
# jiaowuDB

Thanks for the contributions of Yunhao Fu, Haoran Zhao and Xiaoyu Liang to this project.
This project is based on DBMS 2021 Fall taught by Tongge XU, BUAA.
Last version is done on Dec. 16, 2021.

## Build SetUp

Vue3 + bootstrap + element-ui + flask + mysql

```bash

git clone https://github.com/lsnty5190/jiaowuDB.git

cd jiaowuDB

# client
cd client

npm install

npm run dev

# server
cd server

# preprocess necessary keys for database
python prokey.py

python app.py
```

visit [http://localhost:9528](http://localhost:9528)

MOCK is the fake json data to test client. It is consistent with the database schema.


## Project Structure
```
jiaowuDB
├─ client
│  ├─ .editorconfig
│  ├─ .env.development
│  ├─ .env.production
│  ├─ .env.staging
│  ├─ .eslintignore
│  ├─ .eslintrc.js
│  ├─ .travis.yml
│  ├─ babel.config.js
│  ├─ build
│  │  └─ index.js
│  ├─ jest.config.js
│  ├─ jsconfig.json
│  ├─ LICENSE
│  ├─ mock
│  │  ├─ index.js
│  │  ├─ mock-server.js
│  │  ├─ table.js
│  │  ├─ user.js
│  │  └─ utils.js
│  ├─ package-lock.json
│  ├─ package.json
│  ├─ postcss.config.js
│  ├─ public
│  │  ├─ favicon.ico
│  │  └─ index.html
│  ├─ README-zh.md
│  ├─ src
│  │  ├─ api
│  │  │  ├─ table.js
│  │  │  └─ user.js
│  │  ├─ App.vue
│  │  ├─ assets
│  │  │  ├─ 404_images
│  │  │  │  ├─ 404.png
│  │  │  │  └─ 404_cloud.png
│  │  │  ├─ front
│  │  │  │  └─ ER.jpg
│  │  │  └─ scss
│  │  │     └─ vendors
│  │  │        └─ bootstrap-vue
│  │  │           ├─ index.scss
│  │  │           └─ _custom.scss
│  │  ├─ components
│  │  │  ├─ Alert.vue
│  │  │  ├─ Breadcrumb
│  │  │  │  └─ index.vue
│  │  │  ├─ Hamburger
│  │  │  │  └─ index.vue
│  │  │  └─ SvgIcon
│  │  │     └─ index.vue
│  │  ├─ icons
│  │  │  ├─ index.js
│  │  │  ├─ svg
│  │  │  │  ├─ dashboard.svg
│  │  │  │  ├─ example.svg
│  │  │  │  ├─ eye-open.svg
│  │  │  │  ├─ eye.svg
│  │  │  │  ├─ form.svg
│  │  │  │  ├─ link.svg
│  │  │  │  ├─ nested.svg
│  │  │  │  ├─ password.svg
│  │  │  │  ├─ table.svg
│  │  │  │  ├─ tree.svg
│  │  │  │  └─ user.svg
│  │  │  └─ svgo.yml
│  │  ├─ layout
│  │  │  ├─ components
│  │  │  │  ├─ AppMain.vue
│  │  │  │  ├─ index.js
│  │  │  │  ├─ Navbar.vue
│  │  │  │  └─ Sidebar
│  │  │  │     ├─ FixiOSBug.js
│  │  │  │     ├─ index.vue
│  │  │  │     ├─ Item.vue
│  │  │  │     ├─ Link.vue
│  │  │  │     ├─ Logo.vue
│  │  │  │     └─ SidebarItem.vue
│  │  │  ├─ index.vue
│  │  │  └─ mixin
│  │  │     └─ ResizeHandler.js
│  │  ├─ main.js
│  │  ├─ permission.js
│  │  ├─ plugins
│  │  │  └─ bootstrap-vue.js
│  │  ├─ router
│  │  │  └─ index.js
│  │  ├─ settings.js
│  │  ├─ store
│  │  │  ├─ getters.js
│  │  │  ├─ index.js
│  │  │  └─ modules
│  │  │     ├─ app.js
│  │  │     ├─ settings.js
│  │  │     └─ user.js
│  │  ├─ styles
│  │  │  ├─ element-ui.scss
│  │  │  ├─ index.scss
│  │  │  ├─ mixin.scss
│  │  │  ├─ sidebar.scss
│  │  │  ├─ transition.scss
│  │  │  └─ variables.scss
│  │  ├─ utils
│  │  │  ├─ auth.js
│  │  │  ├─ get-page-title.js
│  │  │  ├─ index.js
│  │  │  ├─ request.js
│  │  │  └─ validate.js
│  │  └─ views
│  │     ├─ 404.vue
│  │     ├─ dashboard
│  │     │  └─ index.vue
│  │     ├─ form
│  │     │  └─ index.vue
│  │     ├─ function
│  │     │  ├─ menu1
│  │     │  │  └─ index.vue
│  │     │  ├─ menu2
│  │     │  │  └─ index.vue
│  │     │  ├─ menu3
│  │     │  │  └─ index.vue
│  │     │  └─ menu4
│  │     │     └─ index.vue
│  │     ├─ login
│  │     │  └─ index.vue
│  │     ├─ nested
│  │     │  ├─ menu2
│  │     │  │  └─ index.vue
│  │     │  ├─ menu3
│  │     │  │  └─ index.vue
│  │     │  ├─ menu4
│  │     │  │  └─ index.vue
│  │     │  ├─ menu5
│  │     │  │  └─ index.vue
│  │     │  ├─ menu6
│  │     │  │  └─ index.vue
│  │     │  ├─ menu7
│  │     │  │  └─ index.vue
│  │     │  └─ menu8
│  │     │     └─ index.vue
│  │     ├─ table
│  │     │  └─ index.vue
│  │     └─ tree
│  │        └─ index.vue
│  ├─ tests
│  │  └─ unit
│  │     ├─ .eslintrc.js
│  │     ├─ components
│  │     │  ├─ Breadcrumb.spec.js
│  │     │  ├─ Hamburger.spec.js
│  │     │  └─ SvgIcon.spec.js
│  │     └─ utils
│  │        ├─ formatTime.spec.js
│  │        ├─ param2Obj.spec.js
│  │        ├─ parseTime.spec.js
│  │        └─ validate.spec.js
│  └─ vue.config.js
├─ db_schema
│  └─ schema_jiaowu.sql
├─ MOCK
│  ├─ COURSES.JSON
│  ├─ DEPT.JSON
│  ├─ MOCK_CO.JSON
│  ├─ MOCK_DEPT.JSON
│  ├─ MOCK_SEC.JSON
│  ├─ MOCK_STU.JSON
│  ├─ MOCK_TAK.JSON
│  ├─ MOCK_TEA.JSON
│  ├─ MOCK_TEAA.JSON
│  ├─ SECTIONS.JSON
│  ├─ STUDENTS.JSON
│  ├─ TAKES.JSON
│  ├─ TEACH.JSON
│  └─ TEACHERS.JSON
├─ README.md
├─ server
│  ├─ app.py
│  ├─ dbfunc.py
│  ├─ key
│  │  └─ KEYS.JSON
│  ├─ prokey.py
│  ├─ requirements.txt
│  └─ __pycache__
│     └─ dbfunc.cpython-37.pyc
└─ 数据库导入以及说明
   ├─ data
   │  ├─ classroom.txt
   │  ├─ course.txt
   │  ├─ department.txt
   │  ├─ section.txt
   │  ├─ stu_empty_credits.txt
   │  ├─ takes_sql.txt
   │  ├─ teacher.txt
   │  ├─ teaches.txt
   │  └─ time_slot.txt
   ├─ readme.md
   └─ sqltxt.py

```