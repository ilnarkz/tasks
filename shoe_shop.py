import psycopg

'''
----------------------------------
https://editor.ponyorm.com/user/ilnar/shoe_shop/designer
----------------------------------
'''


with psycopg.connect('dbname=shoe_shop user=ilnar') as conn:
    with conn.cursor() as cur:
        cur.execute('''
        SELECT COUNT(*) FROM shoe WHERE colour=%(colour)s
        ''', {'colour': 'black'})
        result = cur.fetchall()
        print(result)
        cur.execute('''
        SELECT COUNT(*) FROM shoe WHERE size=42
        ''')
        result = cur.fetchall()
        print(result)
        cur.execute('''
        SELECT COUNT(*) FROM shoe WHERE article=100000
        ''')
        result = cur.fetchall()
        print(result)
        cur.execute('''
        SELECT * FROM shoe JOIN section_shoe ON shoe.id = section_shoe.shoes WHERE section_shoe.sections = 1
        ''')
        result = cur.fetchall()
        print(result)
        cur.execute('''
        SELECT * FROM shoe WHERE season=%(season)s
        ''', {'season': 'black'})
        result = cur.fetchall()
        print(result)
        cur.execute('''
        SELECT price, made_in FROM shoe WHERE id = 1
        ''')
        result = cur.fetchone()
        print(result)
        cur.execute('''
        UPDATE shoe SET sold_out=NOW() WHERE sold_out = NULL AND id = 1
        ''')
        print(result)
        cur.execute('''
        SELECT * FROM shoe WHERE sold_out BETWEEN '2022-01-01' AND '2022-10-05'
        ''')
        result = cur.fetchall()
        print(result)
