#  python3 script to initialize the Entry Camera Module table.

from sqlalchemy import Column, Integer, String, create_engine, Date, Boolean, LargeBinary, FLOAT
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.types import TypeDecorator, CHAR
from sqlalchemy.dialects.postgresql import DOUBLE_PRECISION


from psycopg2.extensions import adapt, register_adapter, AsIs
import rootpath
import sys

path = rootpath.detect()
sys.path.append(path)
from db_helper import DB_Helper
import datetime
engine = DB_Helper().db_connect_sql_alchemy()
print("engine", engine)
Base = declarative_base(bind = engine)

class EntryCameraTable(Base):
    """ Declaring store_entry_table table
    """
    
    __tablename__ = 'entry_table2'
    __table_args__ = ({"schema": 'public'})
    
    animal_name = Column(String)
    animal_image = Column(LargeBinary)
    total_time = Column(DOUBLE_PRECISION)
    
    __mapper_args__ = {
        'primary_key':[total_time]
    }
    
    
    def __hash__(self):
        return hash(self.name)
    
    
