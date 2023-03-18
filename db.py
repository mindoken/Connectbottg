import sqlalchemy as db
#from sqlalchemy.orm import session,sessionmaker,mapper
#from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///members-sqlalchemy.db')

connection = engine.connect()

metadata = db.MetaData()

#Base= declarative_base()

members = db.Table('members',metadata,
    db.Column('tg_id',db.String),
    db.Column('gender',db.String),            
    db.Column('name',db.String),
    db.Column('age',db.Integer),    
    db.Column('tg_chat_id',db.String,primary_key=True),
    db.Column('faculty',db.String),
    db.Column('networking',db.Boolean),
    db.Column('friendship',db.Boolean),
    db.Column('relationship',db.Boolean),
    db.Column('help',db.Boolean),
    db.Column('chatting',db.Boolean),
    db.Column('photo',db.String),
    db.Column('bio',db.String)         
)

#class Members(object):
#    pass

#mapper(Members,members)
metadata.create_all(engine)
connection.commit()
