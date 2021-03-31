#  python3 script to insert entry camera module data to Data base.

import numpy as np
from psycopg2.extensions import adapt, register_adapter, AsIs
import rootpath
import sys
from sqlalchemy import Sequence

path = rootpath.detect()
sys.path.append(path)
from entry_table import EntryCameraTable


class EntryCamera():
    """ To store all the data in DB for Entry Camera Module.
    """
    
    def __init__(self):
        
        pass
        
    def adapt_numpy_int64(self, numpy_int64):
        """ Adapting numpy.int64 type to SQL-conform int type 
            using psycopg extension, see [1]_ for more info.
            References
            ----------
            .. [1] http://initd.org/psycopg/docs/advanced.
                html#adapting-new-python-types-to-sql-syntax
        """
        return AsIs(numpy_int64)
    
    def insert_entry_cam_data(self, session, cropped_image, animal_name, t_time):
        """ get the data from entry camera module and insert it into
            the DB.
            
            Arguments :
                entry_data : Entry camera module Data that need to be 
                            inserted into the table .
                session : Connection with DB.
            
            Return :
                insert_entry_data : sqlAlchemy inserted entry camera 
                                    module  data.
        """
        cropped_image = np.ascontiguousarray(cropped_image)
        register_adapter(np.int64, self.adapt_numpy_int64)
        # insert query for entry camera module.
        insert_entry_query = EntryCameraTable(animal_name = animal_name,
                                            animal_image = cropped_image, 
                                            total_time = t_time)
        insert_entry_data = session.add(insert_entry_query)

        session.commit()
      
        return insert_entry_data
        
        
        
    
    