'''
Author: your name
Date: 2021-12-15 16:56:35
LastEditTime: 2021-12-15 21:31:24
LastEditors: Please set LastEditors
Description: 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
FilePath: \jiaowuDB\server\prokey.py
'''

import json

KEYS = {
    "course": ['course_id', 'course_name', 'dept_id', 'course_english_name', 'course_information_link', 'credits'],
    "student": ['student_id', 'student_name', 'dept_id', 'tot_credits'],
    "department": ["dept_id", "dept_name"],
    "section": ["course_id", "sec_id", "year_semester", "classroom_id", "time_slot_id", "enrollment"],
    "takes": ["student_id", "course_id", "sec_id", "year_semester", "grade"],
    "teacher": ["teacher_id", "teacher_name", "teacher_gender", "teacher_title", "teacher_nation", "teacher_email", "dept_id"],
    "teaches": ["teacher_id", "course_id", "sec_id", "year_semester"],
    "stu_schedule": ["course_name", "sec_id", "classroom_address", "time_slot"],
    "start_course": ["sec_id", "year_semester", "enrollment", "address", "time_slot", "teacher"],
    "tea_schedule": ["course_name", "sec_id", "classroom_address", "time_slot"]
}

with open('server\key\KEYS.JSON', 'w') as f:
    json.dump(KEYS, f)


