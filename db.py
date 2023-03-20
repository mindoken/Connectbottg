import sqlalchemy as db

engine = db.create_engine('sqlite:///members-sqlalchemy.db') #создание БД

connection = engine.connect() #подключение к БД

metadata = db.MetaData()

members = db.Table('members',metadata, #создание таблицы
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

metadata.create_all(engine)
connection.commit()
