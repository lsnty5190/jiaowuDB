import pymysql

<<<<<<< HEAD
# conn=pymysql.connect(host="localhost",user='root',passwd='root',database='jwsys',port=3306,use_unicode=True, charset="utf8")
conn = pymysql.connect(host='192.168.1.166',
                       port=3306,
                       user='lisn',
                       passwd='123456',
                       database='jiaowuDB',
                       use_unicode=True, 
                       charset="utf8")
=======
conn=pymysql.connect(host="localhost",user='root',passwd='root',database='jwsys',port=3306,use_unicode=True, charset="utf8")
>>>>>>> caff29c300df1d4b1326fb7840f4aca6946cc463
cursor = conn.cursor()


def sql_process(sql):
    cursor.execute(sql)
    data = cursor.fetchall()
    return data

def insert_teacher():
    basesql = "Insert into teacher (teacher_id,teacher_name,teacher_gender,teacher_title,teacher_nation,teacher_phone,teacher_email, dept_id) values %s;"
    for line in teacher_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        sql_process(sql)


def insert_course():
    basesql = "Insert into course (course_id, course_name, course_english_name,course_information_link, dept_id, credits) values %s;"
    for line in course_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        sql_process(sql)

def insert_class():
    basesql = "Insert into class (course_id,teacher_id,class_time) values %s;"
    for line in class_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        sql_process(sql)

def insert_department():
    basesql = "Insert into department (dept_id, dept_name) values ('%s');"
    for line in depart_fin.readlines():
        line = line.replace('\n', '')
        if len(line) == 0:
            continue
        sql = basesql % line
        try:
            sql_process(sql)
        except pymysql.err.IntegrityError:
            print('[*] ', sql)

def insert_classroom():
    basesql = "Insert into classroom (classroom_id, address, capacity) values %s;"
    for line in classroom_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        sql_process(sql)

def insert_time_slot():
    basesql = "Insert into time_slot (time_slot_id, day, start_time, end_time) values %s;"
    for line in time_slot_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        sql_process(sql)


def insert_section():
    basesql = "Insert into section (course_id, year_semester, sec_id, classroom_id, time_slot_id, enrollment) values %s;"
    cnt = 0
    for line in section_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        # sql_process(sql)

        try:
            sql_process(sql)
        except pymysql.err.IntegrityError:
            print('[*] ', sql)
            cnt += 1
    print(cnt)

def insert_teaches():
    basesql = "Insert into teaches (teacher_id, course_id, sec_id, year_semester) values %s;"
    cnt = 0
    for line in teaches_fin.readlines():
        line = line.replace('\n', '')
        sql = basesql % line
        # sql_process(sql)
        try:
            sql_process(sql)
        except:
            cnt += 1
            print(sql)
    print(cnt)

def insert_student():
    for line in student_fin.readlines():
        line = line.replace('\n', '')
        try:
            sql_process(line)
        except:
            print(line)


def insert_takes():
    cnt = 0
    for line in takes_fin.readlines():
        line = line.replace('\n', '')
        # sql_process(line)
        try:
            sql_process(line)
        except:
            cnt += 1
            print(line)
    print(cnt)

depart_fin = open('数据库导入以及说明/data/department.txt', 'r', encoding='utf-8')
insert_department()
teacher_fin = open('数据库导入以及说明/data/teacher.txt', 'r')
insert_teacher()
classroom_fin = open('数据库导入以及说明/data/classroom.txt', 'r')
insert_classroom()
time_slot_fin = open('数据库导入以及说明/data/time_slot.txt', 'r')
insert_time_slot()
course_fin = open('数据库导入以及说明/data/course.txt', 'r')
insert_course()
section_fin = open('数据库导入以及说明/data/section.txt', 'r')
insert_section()
teaches_fin = open('数据库导入以及说明/data/teaches.txt', 'r')
insert_teaches()
student_fin = open('数据库导入以及说明/data/stu_empty_credits.txt', 'r')
insert_student()
takes_fin = open('数据库导入以及说明/data/takes_sql.txt', 'r')
insert_takes()
conn.commit()
cursor.close()
conn.close()