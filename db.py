import sqlalchemy as db
#from sqlalchemy.orm import session,sessionmaker,mapper
#from sqlalchemy.ext.declarative import declarative_base

engine = db.create_engine('sqlite:///members-sqlalchemy.db')

connection = engine.connect()

metadata = db.MetaData()

#Base= declarative_base()

members = db.Table('members',metadata,
    db.Column('tg_id',db.String,primary_key=True),
    db.Column('gender',db.String),            
    db.Column('name',db.String),
    db.Column('age',db.Integer),    
    db.Column('tg_chat_id',db.String),
    db.Column('faculty',db.String),
    db.Column('networking',db.Boolean),
    db.Column('friendship',db.Boolean),
    db.Column('relationship',db.Boolean),
    db.Column('help',db.Boolean),
    db.Column('chatting',db.Boolean),
    db.Column('photo',db.BLOB),
    db.Column('bio',db.String)         
)

#class Members(object):
#    pass

#mapper(Members,members)
def start():
    metadata.create_all(engine)
start()
"""select_query= db.select(members).where(members.columns.tg_chat_id !=0)
select_result= connection.execute(select_query).fetchall()
print(select_result)

select_all_query= db.select(members)
select_all_result= connection.execute(select_all_query).fetchall()
print(select_all_result)"""


