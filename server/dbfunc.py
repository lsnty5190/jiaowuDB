'''
Author: your name
Date: 2021-12-15 14:46:51
LastEditTime: 2021-12-16 17:22:24
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \jiaowuDB\server\dbconnect.py
'''

from typing import List
import pymysql
import json
import decimal

# STUDENTS_KEYS = ['student_id', 'student_name', 'dept_id', 'tot_credits']

class DecimalEncoder(json.JSONEncoder):

    def default(self, data):

        if isinstance(data, decimal.Decimal):

            return float(data)

        super(DecimalEncoder, self).default(data)

def list2json(data_list, key_list):
    raw_json = []
    for data in data_list:
        tmp_json = {}
        for d, k in zip(data, key_list):
            tmp_json[k] = d
        raw_json.append(tmp_json)

    return json.dumps(raw_json, cls=DecimalEncoder)

def find_keys(table_name):

    with open('server\key\KEYS.JSON', 'r') as f:
        key_list = json.load(f)[table_name]

    return key_list

def select_all(table_name):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    sql = "select * from %s" % table_name

    print(sql)

    key_list = find_keys(table_name)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return list2json(results, key_list)
    except:
        raise NotImplementedError

def select_sp(table_name, data):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    sql = "select * from %s " % table_name

    key_list = find_keys(table_name)

    conditions = "where "

    for k in data:
        if data[k] != "":
            conditions += "%s = \"%s\" and " % (k, data[k])

    conditions = list(conditions)[:-5]
    conditions = ''.join(conditions)

    sql +=  conditions

    print(sql)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return list2json(results, key_list)
    except:
        raise NotImplementedError

def add(table_name, data):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    sql = "insert into %s values" % table_name

    key_list = find_keys(table_name)

    value = '('
    for k in key_list:
        value = value + '\"' + data[k] + "\"" + ','
    value = list(value)
    value[-1] = ')'
    value = ''.join(value)

    sql += value

    print(sql)
    
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def delete(table_name, id):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    key_list = find_keys(table_name)

    sql = "delete from %s where %s = %s" % (table_name, key_list[0], id)

    print(sql)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def update(table_name, data, id):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    sql = "update %s set " % table_name

    key_list = find_keys(table_name)

    changes = ""
    
    for k in data:
        if k == key_list[0]: continue
        changes += "%s = \"%s\"," % (k, data[k])
    
    changes = list(changes)[:-1] # delete last ','
    changes = ''.join(changes)

    sql += changes
    sql += " where %s = %s" % (key_list[0], id)

    print(sql)

    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()

    db.close()

def stu_schedule(data):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    student_id, year_semester = data['student_id'], data['year_semester']

    key_list = find_keys('stu_schedule')

    sql = "select course.course_name, section.sec_id, classroom.address, section.time_slot_id \
            from takes, section, classroom, course \
            where takes.student_id = \"%s\" and takes.year_semester = \"%s\" and takes.course_id = course.course_id \
            and section.course_id = takes.course_id and classroom.classroom_id = section.classroom_id " % (student_id, year_semester)

    print(sql)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return list2json(results, key_list)
    except:
        raise NotImplementedError

def start_course(data):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    course_id = data['course_id']

    sql = "select section.sec_id, section.year_semester, section.enrollment, classroom.address, section.time_slot_id, teacher.teacher_name \
            from section, classroom, teaches, teacher \
            where section.course_id = '%s' and teaches.course_id = section.course_id and classroom.classroom_id = section.classroom_id and teacher.teacher_id = teaches.teacher_id and teaches.sec_id = section.sec_id" % course_id

    print(sql)

    key_list = find_keys('start_course')

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return list2json(results, key_list)
    except:
        raise NotImplementedError

def tea_schedule(data):

    db = pymysql.connect(host='192.168.1.166',
                         port=3306,
                         user='lisn',
                         passwd='123456',
                         database='jiaowuDB')

    cursor = db.cursor()

    teacher_id, year_semester = data['teacher_id'], data['year_semester']

    key_list = find_keys('stu_schedule')

    sql = "select course.course_name, section.sec_id, classroom.address, section.time_slot_id \
            from teaches, section, classroom, course \
            where teaches.teacher_id = '%s' and teaches.year_semester = '%s' and teaches.course_id = course.course_id \
            and section.course_id = teaches.course_id and classroom.classroom_id = section.classroom_id" % (teacher_id, year_semester)

    print(sql)

    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        return list2json(results, key_list)
    except:
        raise NotImplementedError

if __name__ == '__main__':
    db = pymysql.connect(host='192.168.1.166',
                     port=3306,
                     user='lisn',
                     passwd='123456',
                     database='jiaowuDB')

    cursor = db.cursor()

    # json_data = dbfunc()    

    db.close()