'''
Author: your name
Date: 2021-12-14 14:19:03
LastEditTime: 2021-12-15 21:48:08
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

import json

from dbfunc import select_all, add, delete, update, select_sp, stu_schedule, start_course, tea_schedule


with open('MOCK\COURSES.json') as f:
    BOOKS = json.load(f)

# with open('MOCK\STUDENTS.json') as f:
#     STUDENTS = json.load(f)   
STUDENTS =  select_all('student')

with open('MOCK\MOCK_STU.json') as f:
    MOCK_STU = json.load(f) 

with open('MOCK\MOCK_CO.json') as f:
    MOCK_CO = json.load(f) 

with open('MOCK\DEPT.json') as f:
    DEPT = json.load(f) 

with open('MOCK\MOCK_DEPT.json') as f:
    MOCK_DEPT = json.load(f) 

with open('MOCK\SECTIONS.json') as f:
    SECTION = json.load(f) 

with open('MOCK\MOCK_SEC.json') as f:
    MOCK_SEC = json.load(f) 

with open('MOCK\TAKES.json') as f:
    TAKES = json.load(f) 

with open('MOCK\MOCK_TAK.json') as f:
    MOCK_TAK = json.load(f) 

with open('MOCK\TEACHERS.json') as f:
    TEACHERS = json.load(f) 

with open('MOCK\MOCK_TEA.json') as f:
    MOCK_TEA = json.load(f) 

with open('MOCK\TEACH.json') as f:
    TEACH = json.load(f) 

with open('MOCK\MOCK_TEAA.json') as f:
    MOCK_TEAA = json.load(f) 
    
# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_item(item_id, items, key):
    for item in items:
        if item[key] == int(item_id):
            items.remove(item)
            return True
    return False


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('course', post_data)
        # add it in database...
        response_object['message'] = 'Course added!'
    else:
        # search all...
        response_object['books'] = json.loads(select_all('course'))
    return jsonify(response_object)

@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(book_id)
        update('course', post_data, book_id)
        # update database...
        response_object['message'] = 'Course updated!'
    if request.method == 'DELETE':
        delete('course', book_id)
        # delete it in database...
        response_object['message'] = 'Course removed!'
    return jsonify(response_object)

@app.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = json.loads(select_sp('course', post_data))
    else:
        response_object['books'] = MOCK_CO

    return jsonify(response_object)

@app.route('/students', methods=['GET', 'POST'])
def all_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        print(post_data)
        add('student', post_data)
        response_object['message'] = 'Student added!'
    else:
        # select all students...
        response_object['books'] = json.loads(select_all('student'))

    return jsonify(response_object)

@app.route('/students/<student_id>', methods=['PUT', 'DELETE'])
def single_student(student_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(student_id)
        update('student', post_data, student_id)
        response_object['message'] = 'Student updated!'
    if request.method == 'DELETE':
        delete('student', student_id)
        response_object['message'] = 'Student removed!'

    return jsonify(response_object)

@app.route('/students/search', methods=['GET', 'POST'])
def search_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = json.loads(select_sp('student', post_data))
    else:
        response_object['books'] = MOCK_STU

    return jsonify(response_object)

@app.route('/depts', methods=['GET', 'POST'])
def all_depts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('department', post_data)
        response_object['message'] = 'Dept added!'
    else:
        response_object['books'] = json.loads(select_all('department'))
    return jsonify(response_object)

@app.route('/depts/<dept_id>', methods=['PUT', 'DELETE'])
def single_dept(dept_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(post_data)
        update('department', post_data, dept_id)
        response_object['message'] = 'Department updated!'
    if request.method == 'DELETE':
        remove_item(dept_id, DEPT, 'dept_id')
        response_object['message'] = 'Department removed!'
    return jsonify(response_object)

@app.route('/depts/search', methods=['GET', 'POST'])
def search_dept():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = json.loads(select_sp('department', post_data))
    else:
        response_object['books'] = MOCK_DEPT

    return jsonify(response_object)

@app.route('/sections', methods=['GET', 'POST'])
def all_sections():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('section', post_data)
        response_object['message'] = 'Section added!'
    else:
        response_object['books'] = json.loads(select_all('section'))
    return jsonify(response_object)

@app.route('/sections/<sec_id>', methods=['PUT', 'DELETE'])
def single_section(sec_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(sec_id)
        update('section', post_data, sec_id)
        response_object['message'] = 'Section updated!'
    if request.method == 'DELETE':
        delete('section', sec_id)
        response_object['message'] = 'Section removed!'
    return jsonify(response_object)

@app.route('/sections/search', methods=['GET', 'POST'])
def search_sec():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = json.loads(select_sp('section', post_data))
    else:
        response_object['books'] = MOCK_SEC

    return jsonify(response_object)

@app.route('/takes', methods=['GET', 'POST'])
def all_takes():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('takes', post_data)
        response_object['message'] = 'Section added!'
    else:
        response_object['books'] = json.loads(select_all('takes'))

    return jsonify(response_object)

@app.route('/takes/<take_id>', methods=['PUT', 'DELETE'])
def single_take(take_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(take_id)
        update('takes', post_data, take_id)
        response_object['message'] = 'Take updated!' 
    if request.method == 'DELETE':
        delete('takes', take_id)
        response_object['message'] = 'Take removed!'
    return jsonify(response_object)

@app.route('/takes/search', methods=['GET', 'POST'])
def search_take():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_TAK
    else:
        response_object['books'] = MOCK_TAK

    return jsonify(response_object)

@app.route('/teachers', methods=['GET', 'POST'])
def all_teachers():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('teacher', post_data)
        response_object['message'] = 'Teacher added!'
    else:
        response_object['books'] = json.loads(select_all('teacher'))
    return jsonify(response_object)

@app.route('/teachers/<tea_id>', methods=['PUT', 'DELETE'])
def single_teacher(tea_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(tea_id)
        update('teacher', post_data, tea_id)
        response_object['message'] = 'Teacher updated!'
    if request.method == 'DELETE':
        delete('teacher', tea_id)
        response_object['message'] = 'Teacher removed!'
    return jsonify(response_object)

@app.route('/teachers/search', methods=['GET', 'POST'])
def search_teacher():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        print(MOCK_TEA)
        response_object['books'] = json.loads(select_sp('teacher', post_data))
    else:
        response_object['books'] = MOCK_TEA

    return jsonify(response_object)

@app.route('/teach', methods=['GET', 'POST'])
def all_teach():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        add('teaches', post_data)
        response_object['message'] = 'Teach added!'
    else:
        response_object['books'] = json.loads(select_all('teaches'))
    return jsonify(response_object)

@app.route('/teach/<teaa_id>', methods=['PUT', 'DELETE'])
def single_teach(teaa_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(teaa_id)
        update('teaches', post_data, teaa_id)
        response_object['message'] = 'Teach updated!'
    if request.method == 'DELETE':
        delete('teaches', teaa_id)
        response_object['message'] = 'Teach removed!'
    return jsonify(response_object)

@app.route('/teach/search', methods=['GET', 'POST'])
def search_teach():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = json.loads(select_sp('teaches', post_data))
    else:
        response_object['books'] = MOCK_TEAA

    return jsonify(response_object)

@app.route('/stucourses/search', methods=['GET', 'POST'])
def search_stuschedule():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        print(post_data)
        response_object['books'] = json.loads(stu_schedule(post_data))
    else:
        response_object['books'] = MOCK_TEAA

    return jsonify(response_object)

@app.route('/startcourses/search', methods=['GET', 'POST'])
def search_start_course():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        print(post_data)
        response_object['books'] = json.loads(start_course(post_data))
    else:
        response_object['books'] = MOCK_TEAA

    return jsonify(response_object)

@app.route('/teacourses/search', methods=['GET', 'POST'])
def search_teaschedule():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        print(post_data)
        response_object['books'] = json.loads(tea_schedule(post_data))
    else:
        response_object['books'] = MOCK_TEAA

    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
