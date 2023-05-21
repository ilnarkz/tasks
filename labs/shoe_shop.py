from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilnar:123@localhost:5432/shoe_shop'
db = SQLAlchemy(app)

section_shoe = db.Table('section_shoe',
                        db.Column('section_id', db.Integer, db.ForeignKey('section.id')),
                        db.Column('shoe_id', db.Integer, db.ForeignKey('shoe.id'))
                        )


class Section(db.Model):
    __tablename__ = 'section'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(127), nullable=False)

    def __repr__(self):
        return '<Section %r>' % self.name


class Shoe(db.Model):
    __tablename__ = 'shoe'
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Integer, nullable=False)
    articul = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    colour = db.Column(db.String(32), nullable=False)
    style = db.Column(db.String(32), nullable=False)
    season = db.Column(db.String(32), nullable=False)
    made_in = db.Column(db.String(32), nullable=False)
    sections = db.relationship('Section', secondary=section_shoe, backref='shoe')
    sold_out = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return '<Shoe %r>' % self.name


with app.app_context():
    db.create_all()
