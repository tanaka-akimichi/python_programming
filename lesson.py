import sqlalchemy
import sqlalchemy.ext.declarative
import sqlalchemy.orm

engine = sqlalchemy.create_engine('sqlite:///:memory:', echo=True)

Base = sqlalchemy.ext.declarative.declarative_base()

class Person(Base):
    __tablename__ = 'persons'
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String(14))

Base.metadata.create_all(engine)

Session = sqlalchemy.orm.sessionmaker(bind=engine)
session = Session()

p1 = Person(name='Mike')
session.add(p1)
p2 = Person(name='Nancy')
session.add(p2)
p3 = Person(name='Jun')
session.add(p3)
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)

p4 = session.query(Person).filter_by(name='Mike').first()
p4.name = 'Michael'
session.commit()

persons = session.query(Person).all()
for person in persons:
    print(person.id, person.name)


