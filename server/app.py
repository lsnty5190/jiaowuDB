'''
Author: your name
Date: 2021-12-14 14:19:03
LastEditTime: 2021-12-15 12:47:17
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS

import json


with open('MOCK\COURSES.json') as f:
    BOOKS = json.load(f)

with open('MOCK\STUDENTS.json') as f:
    STUDENTS = json.load(f)    

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
        BOOKS.append({
            'course_id': int(post_data.get('course_id')),
            'course_name': post_data.get('course_name'),
            'dept_id': post_data.get('dept_id'),
            'course_eng_name': post_data.get('course_eng_name'),
            'credit': post_data.get('credit')
        })
        # add it in database...
        response_object['message'] = 'Course added!'
    else:
        # search all...
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(book_id)
        remove_item(book_id, BOOKS, 'course_id')
        BOOKS.append({
            'course_id': int(post_data.get('course_id')),
            'course_name': post_data.get('course_name'),
            'dept_id': post_data.get('dept_id'),
            'course_eng_name': post_data.get('course_eng_name'),
            'credit': post_data.get('credit')
        })
        # update database...
        response_object['message'] = 'Course updated!'
    if request.method == 'DELETE':
        remove_item(book_id, BOOKS, 'course_id')
        # delete it in database...
        response_object['message'] = 'Course removed!'
    return jsonify(response_object)

@app.route('/courses/search', methods=['GET', 'POST'])
def search_courses():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_CO
    else:
        response_object['books'] = MOCK_CO

    return jsonify(response_object)

@app.route('/students', methods=['GET', 'POST'])
def all_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        STUDENTS.append({
            'student_id': int(post_data.get('student_id')),
            'student_name': post_data.get('student_name'),
            'dept_id': post_data.get('dept_id'),
            'tot_credits': post_data.get('tot_credits')
        })
        response_object['message'] = 'Student added!'
        print(STUDENTS)
    else:
        response_object['books'] = STUDENTS
    return jsonify(response_object)

@app.route('/students/<student_id>', methods=['PUT', 'DELETE'])
def single_student(student_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(student_id)
        remove_item(student_id, STUDENTS, 'student_id')
        STUDENTS.append({
            'student_id': int(post_data.get('student_id')),
            'student_name': post_data.get('student_name'),
            'dept_id': post_data.get('dept_id'),
            'tot_credits': post_data.get('tot_credits')
        })
        response_object['message'] = 'Student updated!'
        print(STUDENTS)
    if request.method == 'DELETE':
        remove_item(student_id, STUDENTS, 'student_id')
        print(STUDENTS)
        response_object['message'] = 'Student removed!'
    return jsonify(response_object)

@app.route('/students/search', methods=['GET', 'POST'])
def search_students():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_STU
    else:
        response_object['books'] = MOCK_STU

    return jsonify(response_object)

@app.route('/depts', methods=['GET', 'POST'])
def all_depts():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        DEPT.append({
            'dept_id': int(post_data.get('dept_id')),
            'dept_name': post_data.get('tot_credits')
        })
        response_object['message'] = 'Dept added!'
    else:
        response_object['books'] = DEPT
    return jsonify(response_object)

@app.route('/depts/<dept_id>', methods=['PUT', 'DELETE'])
def single_dept(dept_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(dept_id)
        remove_item(dept_id, DEPT, 'dept_id')
        DEPT.append({
            'dept_id': int(post_data.get('dept_id')),
            'dept_name': post_data.get('tot_credits')
        })
        response_object['message'] = 'Student updated!'
    if request.method == 'DELETE':
        remove_item(dept_id, DEPT, 'dept_id')
        response_object['message'] = 'Student removed!'
    return jsonify(response_object)

@app.route('/depts/search', methods=['GET', 'POST'])
def search_dept():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_DEPT
    else:
        response_object['books'] = MOCK_DEPT

    return jsonify(response_object)

@app.route('/sections', methods=['GET', 'POST'])
def all_sections():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        SECTION.append({
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
            'classroom_id': post_data.get('classroom_id'),
            'time_slot_id': post_data.get('time_slot_id'),
            'enrollment': post_data.get('enrollment')
        })
        response_object['message'] = 'Section added!'
    else:
        response_object['books'] = SECTION
    return jsonify(response_object)

@app.route('/sections/<sec_id>', methods=['PUT', 'DELETE'])
def single_section(sec_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(sec_id)
        remove_item(sec_id, SECTION, 'course_id')
        SECTION.append({
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
            'classroom_id': post_data.get('classroom_id'),
            'time_slot_id': post_data.get('time_slot_id'),
            'enrollment': post_data.get('enrollment')
        })
        response_object['message'] = 'Section updated!'
    if request.method == 'DELETE':
        remove_item(sec_id, SECTION, 'course_id')
        response_object['message'] = 'Section removed!'
    return jsonify(response_object)

@app.route('/sections/search', methods=['GET', 'POST'])
def search_sec():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_SEC
    else:
        response_object['books'] = MOCK_SEC

    return jsonify(response_object)

@app.route('/takes', methods=['GET', 'POST'])
def all_takes():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TAKES.append({
            'student_id': int(post_data.get('student_id')),
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
            'grade': post_data.get('grade')
        })
        response_object['message'] = 'Section added!'
    else:
        response_object['books'] = TAKES
    return jsonify(response_object)

@app.route('/takes/<take_id>', methods=['PUT', 'DELETE'])
def single_take(take_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(take_id)
        remove_item(take_id, TAKES, 'student_id')
        TAKES.append({
            'student_id': int(post_data.get('student_id')),
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
            'grade': post_data.get('grade')
        })
        response_object['message'] = 'Take updated!' 
    if request.method == 'DELETE':
        remove_item(take_id, TAKES, 'student_id')
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
        TEACHERS.append({
            "teacher_id": int(post_data.get("teacher_id")),
            "teacher_name": post_data.get("teacher_name"),
            "teacher_gender": post_data.get("teacher_gender"),
            "teacher_title": post_data.get("teacher_title"),
            "teacher_nation": post_data.get("teacher_nation"),
            "teacher_email": post_data.get("teacher_email"),
            "dept_id": post_data.get("dept_id")
        })
        response_object['message'] = 'Teacher added!'
    else:
        response_object['books'] = TEACHERS
    return jsonify(response_object)

@app.route('/teachers/<tea_id>', methods=['PUT', 'DELETE'])
def single_teacher(tea_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(tea_id)
        remove_item(tea_id, TEACHERS, 'teacher_id')
        TEACHERS.append({
            "teacher_id": int(post_data.get("teacher_id")),
            "teacher_name": post_data.get("teacher_name"),
            "teacher_gender": post_data.get("teacher_gender"),
            "teacher_title": post_data.get("teacher_title"),
            "teacher_nation": post_data.get("teacher_nation"),
            "teacher_email": post_data.get("teacher_email"),
            "dept_id": post_data.get("dept_id")
        })
        response_object['message'] = 'Teacher updated!'
    if request.method == 'DELETE':
        remove_item(tea_id, TEACHERS, 'teacher_id')
        response_object['message'] = 'Teacher removed!'
    return jsonify(response_object)

@app.route('/teachers/search', methods=['GET', 'POST'])
def search_teacher():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        print(MOCK_TEA)
        response_object['books'] = MOCK_TEA
    else:
        response_object['books'] = MOCK_TEA

    return jsonify(response_object)

@app.route('/teach', methods=['GET', 'POST'])
def all_teach():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        TEACH.append({
            "teacher_id": int(post_data.get("teacher_id")),
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
        })
        response_object['message'] = 'Teach added!'
    else:
        response_object['books'] = TEACH
    return jsonify(response_object)

@app.route('/teach/<teaa_id>', methods=['PUT', 'DELETE'])
def single_teach(teaa_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        print(teaa_id)
        remove_item(teaa_id, TEACH, 'teacher_id')
        TEACHERS.append({
            "teacher_id": int(post_data.get("teacher_id")),
            'course_id': int(post_data.get('course_id')),
            'sec_id': post_data.get('sec_id'),
            'year_semester': post_data.get('year_semester'),
        })
        response_object['message'] = 'Teach updated!'
    if request.method == 'DELETE':
        remove_item(teaa_id, TEACH, 'teacher_id')
        response_object['message'] = 'Teach removed!'
    return jsonify(response_object)

@app.route('/teach/search', methods=['GET', 'POST'])
def search_teach():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        # search... please replace MOCK with real data
        response_object['books'] = MOCK_TEAA
    else:
        response_object['books'] = MOCK_TEAA

    return jsonify(response_object)

if __name__ == '__main__':
    app.run()
