from pymongo import MongoClient
from bson.objectid import ObjectId
    
class AnimalShelter (object):
    
    def __init__(self, username, password):
        # Initializing the MongoClient. This helps to access the MongoDB databases and collections. 
        self.client = MongoClient('mongodb://%s:%s@localhost:31830/test?authSource=AAC'%("aacuser", "aacuser"))
        self.database = self.client['AAC']
    
    #Create for the C in CRUD
    def create(self, data):
        if data is not None:
            insert = self.database.animals.insert(data)  
            if insert!=0:
                return True
            else:
                return False    
        else:
            raise Exception("Cannot save, because the data parameter is empty")           

#CREATE FOR THE R IN crud
    def read(self, criteria=None):
        if criteria is not None:
            data = self.database.animals.find(criteria,{"_id": False})
            for document in data:
                print(document)
        else:
            data = self.database.animals.find({},{"_id": False})
        
        return data
        
#Update for CRUD
def update(self, updateData):
	if updateData is not None:
		if updateData:
			result = self.database.animals.insert_one(updateData)
		return result;
	else:
		raise Exception("Cannot update, updateData parameter is empty")
		
		
#Delete for CRUD
def delete(self, deleteData):
	if deleteData is not None:
		if deleteData:
			result = self.database.animals.delete_one(deleteData)
		return result
	else
		raise Exception("Nothing to delete, deleteData parameter is empty")
		
