import random
import time
import json

class Restaurants:
    def __init__(self, name, type, distance):
        self.name = name
        self.type = type
        self.distance = distance
    
    def printJSON(self):
        return {"name": self.name,
                "type": self.type,
                "distance": self.distance}
    
    def toJSON(self):
        return json.dumps(self, default=lambda o:o.__dict__)
    
Chipotle = Restaurants("Chipotle", "Mexican", 3)
Burgerking = Restaurants("BurgerKing", "Fastfood", 1)
Mcdonalds = Restaurants("McDonalds", "Fastfood", 1)

restaurants = {"Mcdonalds": Mcdonalds.toJSON(), "Burgerking": Burgerking.toJSON(), "Chipotle": Chipotle.toJSON()}

def listRestaurant():
    print("\nHere is is the list of restaurants:")
    for res in restaurants:
        print(restaurants[res].name)

def add():
    
    name = input("Please enter the restaurant name you would like to add: ")
    type = input("What kind of restaurant is this: ")
    distance = input("How far away is it from you (miles): ")
    restaurants[name] = Restaurants(name, type, distance)
    print(name + " has been added")

def delete():

    name = input("Please enter the restaurant name you would like to delete: ")
    del restaurants[name]
    print(name + " has been removed")

def randomize():
    n = random.randint(0,len(restaurants)-1)
    resList = list(restaurants.keys())
    print(resList[n])

def filter():
    filt_type = input("Please enter the type of restaurant you want to filter for: ")
    f = open("filter-services.txt", "r+")

    f.seek(0)
    f.truncate()

    restaurants["filter"] = filt_type
    f.write(str(restaurants))
    #f.write(filt)
    print("filtering ....")
    #time.sleep(3)
    #f.seek(0)
    #res = f.read()
    #print(res)
    f.close()

def displayMenuOption():
    print("\n")
    print("To see the list of restaurants, type 'list'")
    print("To add a Restaurant, type 'add'")
    print("To delete a restaurant, type 'delete'")
    print("To have a random restaurant selected for you, type 'randomize'")
    print("To see restaurants with a filter, type 'filter': ")
    print("To quit, type 'quit'")

def menu():
    
    displayMenuOption()

    while True:

        choice = input("What would you like to do: ")

        if choice == "add":
            add()
        
        elif choice == "delete":
            delete()
        
        elif choice == "list":
            listRestaurant()
        
        elif choice == "randomize":
            randomize()
        
        elif choice == "filter":
            filter()

        elif choice == "quit":
            exit()

        else:
            print("That was not an option, please try again: ")

if __name__ == "__main__":
    while True:
        menu()