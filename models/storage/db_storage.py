from models.base import Base
from models.user import User
from models.survey import Survey
from models.response import Response
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import config
from os import getenv


DB_USER = config.get('db_user') or 'root'
DB_PWD = getenv('DB_PWD') or 'iyanu'
DB_HOST = config.get('db_host') or '0.0.0.0'
DB_PORT = config.get('db_port') or '3306'
DB_NAME = config.get('db_name')

url = 'mysql+mysqldb://{}:{}@{}/{}'.format(DB_USER,
                                  DB_PWD,
                                  DB_HOST,
                                  DB_NAME)

classes = {'User': User, 'Survey': Survey, 'Response': Response}


class Storage:
    """Database storage class
    """
    __engine = None
    __session = None

    def __init__(self):
        """Initialize the database
        """
        self.__engine = create_engine(url)
        Base.metadata.create_all(bind=self.__engine)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

