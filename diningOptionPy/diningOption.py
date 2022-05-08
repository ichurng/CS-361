import random
import time
import json

class Restaurants:
    def __init__(self, name, type):
        self.name = name
        self.type = type
    
    def printJSON(self):
        return {"name": self.name,
                "type": self.type,}
    
Chipotle = Restaurants("Chipotle", "Mexican")
Burgerking = Restaurants("BurgerKing", "Fastfood")
Mcdonalds = Restaurants("McDonalds", "Fastfood")

restaurants = [Mcdonalds, Burgerking, Chipotle]

def listRestaurant():
    print("\nHere is is the list of restaurants:")
    for res in restaurants:
        print(res.name)

def add():
    
    name = input("Please enter the restaurant name you would like to add: ")
    type = input("What kind of restaurant is this: ")
    restaurants.append(Restaurants(name, type)) 
    print(name + " has been added")

def delete():

    name = input("Please enter the restaurant name you would like to delete: ")
    for i, res in enumerate(restaurants):
        if res.name == name:
            del restaurants[i]
    print(name + " has been removed")

def randomize():
    n = random.randint(0,len(restaurants)-1)
    print(restaurants[n].name)

def filter():
    filt_type = input("Please enter the type of restaurant you want to filter for: ")
    f = open("filter-services.txt", "r+")

    send = ""
    for res in restaurants:
        send += res.name + ";" + res.type + ","
    send += "filter;" + filt_type
    send += ",run"

    f.seek(0)
    f.truncate()
    f.write(send)
    f.close()

    f = open("filter-services.txt", "r+")
    print("filtering ....")
    time.sleep(3)
    f.seek(0)
    res = f.read()
    print(res)
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