#todo:
#  БД "Система проверки задач"
# Описание предметной области. БД создается для информационного обслуживания учебного процесса.
# Преподаватель каждый урок выдает некоторое количество задач в качестве домашнего задания.
# Каждый ученик решает задачи и переводит ее в статус решенную выкладывая ее на Git
# Система, забирает задачу с Git'а и проверяет каждую задачу прогоняя ее через тесты и запуская ее в виртульном окружении
# и либо подтверждает ее статус как решенную либо возвращает сообщение об ошибки ( меняя ее статус как не решенную.)
#
#
# Разработайте систему с учетом бизнес сущностей:
# Группа, Преподаватель, Студент, Занятие, Задача
#
# Запросы:
# 1. Выдавать список задач по категории (категориями являются темы занятий)
# 2. Выдавать список задач по уровню сложности
# 3. Выдавать список решенных и не решенных задач для слушателя
# 4. Выдавать весь список задач выданный слушателю
# 5. Выдавать список группы по преподавателю
# 6. Предусмотреть возможность изменения статуса задачи для конкретного слушателя
# 7. Выдавать процент решенных задач. (Соотношение между общим кол-вом и решенным)
# 8. Выдавать процент успеваемости по всей группе.
#
# Система:
# 1. Написать утилиту которая генерирует файлы taskN.py в папке classwork по номеру задачи.
# Задачи все храняться в БД.
import psycopg

'''
https://editor.ponyorm.com/user/ilnar/project/designer
'''


with psycopg.connect('dbname=new_db user=ilnar') as conn:
    with conn.cursor() as cur:
        print('Список задач по категории c id=1')
        cur.execute('''
        SELECT * FROM task WHERE category=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Список задач по сложности c id=1')
        cur.execute('''
        SELECT * FROM task WHERE difficult=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Список решенных задач для студента c id=1')
        cur.execute('''
        SELECT * FROM task JOIN task_student ON task.id = task_student.tasks_id WHERE status=1 AND task_student.students_id=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Список нерешенных задач для студента c id=1')
        cur.execute('''
        SELECT * FROM task JOIN task_student ON task.id = task_student.tasks_id WHERE status=0 AND task_student.students_id=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Список всех задач для студента c id=1')
        cur.execute('''
        SELECT * FROM task JOIN task_student ON task.id = task_student.tasks_id WHERE task_student.students_id=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Список группы по преподавателю c id=1')
        cur.execute('''
        SELECT * FROM student JOIN students_group ON student.group_id = students_group.id JOIN teacher_group ON students_group.id = teacher_group.groups JOIN teacher ON teacher_group.teachers = teacher.id WHERE teacher.id=1
        ''')
        result = cur.fetchall()
        print(result)
        print('Изменение статуса задачи c id=1 на "выполнено" для студента c id=1')
        cur.execute('''
        UPDATE task SET status=1 FROM task_student WHERE task_student.students_id=1 AND task_student.tasks_id=1
        ''')
        conn.commit()
        cur.execute('''
        SELECT COUNT(id) FROM task JOIN task_student ON task.id = task_student.tasks_id WHERE task_student.students_id=1 AND status=1
        ''')
        result = cur.fetchall()
        print(result)
