import os

import psycopg

counter = 1
while True:
    answer = input('Create task? (y/n)')
    if answer == 'n':
        break
    elif answer == 'y':
        file_name = f'task{counter}.py'
        file_path = os.path.join(os.getcwd(), file_name)
        with open(file_path, 'w') as f:
            f.write('')
        with psycopg.connect('dbname=new_db user=ilnar') as conn:
            with conn.cursor() as cur:
                cur.execute(f'''
                INSERT INTO task (id,  category, status, name, description, difficult) VALUES ({counter}, 1, 0, %(name)s, %(description)s, 5)
                ''', {'name': f'task{counter}', 'description': f'task{counter}'})
                conn.commit()
        counter += 1
    else:
        continue
