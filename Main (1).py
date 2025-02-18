from animal_shelter import AnimalShelter
from bson.objectid import ObjectId

animals = AnimalShelter("aacuser", "aacuser")

#Valid document create
print(animals.create ({ 
 'age_upon_outcome': "3 years",
 'animal_id': "test",
 'animal_type': "Cat",
 'breed': "British Blue",
 'color': "Gray",
 'date_of_birth': "2021-05-27",
 'datetime': "2021-05-27 12:00:00",
 'monthyear': "2021-05-27T12:00:00",
 'name': "Oscar",
 'outcome_subtype': "",
 'outcome_type': 'Adoption',
 'sex_upon_outcome': "Spayed Male",
 'location_lat': 30.6525984560228,
 'location_long': -97.7419963476444,
 'age_upon_outcome_in_weeks': 156.9}))

#Invalid Document
print(animals.create({0:0}))

#Valid query
query = animals.read({"name": "Oscar"})
for animal in query:
    print(animal)
    
#Invalid query
print(list(animals.read({0:0})))

updateAnimal = animals.update({"name": "Oscar"}, {"age_upon_outcome": "4 years"})
print(updateAnimal)

deleteAnimal = animals.delete({"name": "Oscar"})
print(delteAnimal)
