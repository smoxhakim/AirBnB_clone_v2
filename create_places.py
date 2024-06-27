#!/usr/bin/python3
from models.place import Place
from models.city import City
from models.state import State
from models.user import User
from models import storage

Morocco = State(name="Morocco")
Morocco.save()

user = User(email="a@a.com", password="pwd")
user.save()

casa = City(name="casa", state_id = Morocco.id)
casa.save()
oujda = City(name="oujda", state_id = Morocco.id)
oujda.save()

place1 = Place(name="darna", city_id=oujda.id, user_id=user.id)
place1.save()
place2 = Place(name="dar smox", city_id=casa.id, user_id=user.id)
place2.save()

storage.save()
print(place1.name)
print(place2.name)



