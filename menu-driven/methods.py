from conn import client
import json

def list_dbs():

    print("\nDatabases are : ")
    databases = client.list_database_names()
    for database in databases:
        print(database)
    print()

def switch_database():
    
    list_dbs()
    global database_name
    database_name = input("\nEnter the Database name : ")

    global db 
    db = client[database_name]
    print(f"Switched to {database_name} database\n")


def present_database():
    try:
        print(f"Presently working in {db.name} database")
    except:
        print("No present Working database! Swicth to the database\n")



def list_collections():

    print("\nCollections are : ")
    collections = db.list_collection_names()
    if len(collections)>0:
        for collection in collections:
            print(collection)
    else:
        print(f"No collections are there in the database {database_name}")
    print()

def crate_colletion():
    collection_name = input("\nEnter the collection name : ")
    try:
        db.create_collection(collection_name)
        print("Collection Created Succesfully\n")
    except:
        print(f"Collection named {collection_name} already present\n")


def drop_collection():
    collection_name = input("\nEnter the collection name : ")
    db.drop_collection(collection_name)
    print("Collection Dropped Succesfully\n")



def rename_collection():
    try:
        current_collection_name = input("Enter the existing collection name : ")
        new_collection_name = input("Enter the new collection name(to renmae) : ")

        db[current_collection_name].rename(new_collection_name)

        print(f'Collection "{current_collection_name}" renamed to "{new_collection_name}" successfully.')
    except:
        print(f"Collection named {new_collection_name} already present\n")

def ask_data_type(key):
    print(f"Enter the type value for {key} : ")
    print("1 : String 2 : Number 3 : Array ")
    ch = int(input("Enter the choice for type : "))
    value = []
    user_input={}
    if ch==1:
        temp = input(f"Enter value for key {key}: ")
        user_input.update({f'{key}': f'{temp}'})
        return user_input

    elif ch==2:
        temp = int(input(f"Enter value for key {key}: "))
        user_input.update({f'{key}': temp})
        return user_input

    elif ch==3:
        value=[]
        max = int(input("Enter the max limit : "))
        for i in range(max):
            print(f"\nEnter the type value : ")
            print("1 : String 2 : Number")
            ch = int(input("Enter the input : "))
            if ch==1:
                temp = input("Enter the value : ")
                value.append(temp)
                
            elif ch==2:
                temp = int(input("Enter the value : "))
                value.append(temp)
        user_input.update({f'{key}': value})
        return user_input
            


def insert_data():

    collection_name = input("Enter the Collection name : ")
    collection = db[collection_name]
    try:
        num_pairs = int(input("Enter the number of key-value pairs: "))
        print()
    except:
        pass
    

    result={}
    for i in range(num_pairs):
        key = input(f"\nEnter key {i + 1}: ")
        temp = ask_data_type(key)
        result.update(temp)
        print(result)

    inserted_document = collection.insert_one(result)
    print(f"Inserted document ID: {inserted_document.inserted_id}\n")



        
