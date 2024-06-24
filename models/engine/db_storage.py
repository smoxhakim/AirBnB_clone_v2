#!/usr/bin/python3

"""DB Storage Module"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base, BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "City": City, "Place": Place,
           "Review": Review, "State": State, "User": User}

class DBStorage:
    """DBStorage class"""

    __engine = None
    __session = None



    def __init__(self):
        """init dunder for DBStorage"""

        username = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')

        db_url = "mysql+mysqldb://{}:{}@{}/{}".format(username, password, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """return a dictionary
        """
        objs = {}
        if cls is None:
            for clas in Base.__subclasses__():
                table = self.__session.query(clas).all()
                for obj in table:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj
        else:
            if (cls == "State"):
                for obj in self.__session.query(classes["State\
"]).order_by(classes[cls].name.asc()).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj
            else:
                for obj in self.__session.query(classes[cls]).all():
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    objs[key] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()







