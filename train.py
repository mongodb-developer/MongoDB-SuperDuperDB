from superduperdb import superduper 
from superduperdb.mongodb import Collection 
import pymongo 
  
my_db = superduper(pymongo.MongoClient().my_db) 
r = my_db.execute(
    Collection('docs')
        .like({'txt': 'similar to this'})
        .find_one()
)
