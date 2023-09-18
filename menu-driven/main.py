from conn import client
from methods import *


while True:
    print("1 : Show Databases    |  2  : Switch Databases   |   3 :  Show Collections")
    print("4 : Create Collection |  5  : Drop Collection    |   6 : Rename Collection")
    print("7 : Insert data       |  8  : Update Collection  |   9 : Rename Collection")
    print("10 : exit             |  11 : Present Database")


    ch = int(input("\nEnter the Choice : "))

    if ch==1:
        list_dbs()
    elif ch==2:
        switch_database()
    elif ch==3:
        list_collections()
    elif ch==4:
        crate_colletion()
    elif ch==5:
        drop_collection()
    elif ch==6:
        rename_collection()
    elif ch==7:
        insert_data()
    elif ch==8:
        insert_data()
    elif ch==11:
        present_database()
    elif ch==10:
        exit()