from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilnar:123@localhost:5432/new_db'
db = SQLAlchemy(app)

teacher_group = db.Table('teacher_group',
                         db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id')),
                         db.Column('group_id', db.Integer, db.ForeignKey('group.id'))
                         )

task_student = db.Table('task_student',
                        db.Column('task_id', db.Integer, db.ForeignKey('task.id')),
                        db.Column('student_id', db.Integer, db.ForeignKey('student.id'))
                        )


class Task(db.Model):
    __tablename__ = 'task'
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String, nullable=False)
    difficult = db.Column(db.String, nullable=False)
    id_category = db.Column(db.ForeignKey('category.id'))

    def __repr__(self):
        return '<Task %r>' % self.name


class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    tasks = db.relationship('Task', backref='category')

    def __repr__(self):
        return '<Category %r>' % self.name


class Student(db.Model):
    __tablename__ = 'student'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    tasks = db.relationship('Task', secondary=task_student, backref='student')
    id_group = db.Column(db.ForeignKey('group.id'))

    def __repr__(self):
        return '<Student %r>' % self.name


class Teacher(db.Model):
    __tablename__ = 'teacher'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)
    groups = db.relationship('Group', secondary=teacher_group, backref='teacher')

    def __repr__(self):
        return '<Teacher %r>' % self.name


class Group(db.Model):
    __tablename__ = 'group'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False)
    students = db.relationship('Student', backref='group')

    def __repr__(self):
        return '<Group %r>' % self.number


with app.app_context():
    db.create_all()
