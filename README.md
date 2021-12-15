<!--
 * @Author: your name
 * @Date: 2021-12-15 14:02:08
 * @LastEditTime: 2021-12-15 23:01:36
 * @LastEditors: Please set LastEditors
 * @Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 * @FilePath: \jiaowuDB\README.md
-->
# jiaowuDB

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

![image](https://github.com/lsnty5190/jiaowuDB/client/src/assets/front/ER.jpg)