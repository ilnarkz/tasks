from shoe_shop import app, Section, Shoe, db

with app.app_context():
    section1 = Section(name='kids')
    section2 = Section(name='women')
    shoe1 = Shoe(size=25, articul=134679, price=4000, colour='red', style='sport', season='summer', made_in='Poland', sold_out='2022-01-01')
    shoe2 = Shoe(size=38, articul=623282, price=3500, colour='magenta', style='shoes', season='summer', made_in='Russia', sold_out='2022-10-01')
    db.session.add(section1)
    db.session.add(section2)
    db.session.add(shoe1)
    db.session.add(shoe2)
    db.session.commit()
