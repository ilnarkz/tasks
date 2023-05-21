from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

from lab3 import Task, Category

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilnar:123@localhost:5432/new_db'
db = SQLAlchemy(app)


@app.route("/", methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        status = request.form['status']
        name = request.form['name']
        description = request.form['description']
        difficult = request.form['difficult']
        category = request.form['category']
        if status and name and description and difficult and category:
            try:
                task = Task(status=int(status), name=name, description=description, difficult=int(difficult), category=Category(name=category))
                db.session.add(task)
                db.session.commit()
            except:
                print('Ошибка записи')
        else:
            print('Ошибка ввода данных')
    return render_template('add_task.html')


if __name__ == '__main__':
    app.run(port=8888)
