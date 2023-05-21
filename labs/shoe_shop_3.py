from flask import Flask, render_template, request, flash, session
from flask_sqlalchemy import SQLAlchemy

from shoe_shop import Shoe

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://ilnar:123@localhost:5432/shoe_shop'
db = SQLAlchemy(app)


@app.route("/", methods=('GET', 'POST'))
def hello_world():
    if request.method == 'POST':
        size = request.form['size']
        articul = request.form['articul']
        colour = request.form['colour']
        style = request.form['style']
        price = request.form['price']
        season = request.form['season']
        made_in = request.form['made_in']
        sold_out = request.form['sold_out']
        if size and style and articul and colour and price and season and made_in and sold_out:
            try:
                shoe = Shoe(size=size, articul=articul, colour=colour, style=style, price=price, season=season,
                            made_in=made_in, sold_out=sold_out)
                db.session.add(shoe)
                db.session.commit()
            except:
                print('Ошибка записи')
        else:
            print('Ошибка ввода данных')
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=5555)
