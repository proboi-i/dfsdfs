#packages =['packages.lib.json']
import pickle as pkl
import json 
import os
import sys
import time
class Pydb:
    """Make Query DDL Functions"""
    def __init__(self):
        self.start = 0
        self.end = 0
    def tble(self,dbname,tablename,fieldntype):
        all = os.listdir('src/__pydb__')
        if tablename in all:
            self.start = time.time()
            self.end = time.time()
            print("Table already exists (query time: ",self.end-self.start," seconds)")
            return 1
        else:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'w') as f:
                value = {}
                value["base"] = []
                for i in fieldntype:
                    value["base"].append(i)
                    value["data"] = []
                json.dump(value,f)
            self.end = time.time()
            print("Table created in ",self.end-self.start," seconds")
            return 0
    def db(self,dbname):
        all = os.listdir('src/__pydb__')
        if dbname in all:
            self.start = time.time()
            self.end = time.time()
            print("Database already exists (query time: ",self.end-self.start," seconds)")
            return 1
        else:
            self.start = time.time()
            os.mkdir('src/__pydb__/{}'.format(dbname))
            self.end = time.time()
            print("Database created in ",self.end-self.start," seconds")
            return 0
    def alter(self,dbname,tablename,fieldntype):
        all = os.listdir('src/__pydb__')
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in fieldntype:
                    value["base"].append(i)
            with open('src/__pydb__/{}.json'.format(tablename),'w') as f:
                json.dump(value,f)
            self.end = time.time()
            print("Table altered in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def drop(self,dbname,tablename):
        all = os.listdir('src/__pydb__')
        if tablename in all:
            self.start = time.time()
            os.remove('src/__pydb__/{}.json'.format(tablename))
            self.end = time.time()
            print("Table dropped in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def dropdb(self,dbname):
        all = os.listdir('src/__pydb__')
        if dbname in all:
            self.start = time.time()
            os.rmdir('src/__pydb__/{}'.format(dbname))
            self.end = time.time()
            print("Database dropped in ",self.end-self.start," seconds")
            return 0
        else:
            print("Database does not exist")
            return 1
    def insert(self,dbname,tablename,fieldntype,replacement=False):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename+".json" in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                if len(fieldntype) != 1:
                    for i in fieldntype:
                        if i not in value["data"]:
                            value["data"].append(i)
                        else:
                            print("Data already exists")
                            if replacement:
                                value["data"].remove(i)
                                value["data"].append(i)
                                
                else:
                    value["data"].extend(fieldntype)
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'w') as f:
                json.dump(value,f)
            self.end = time.time()
            print("Data inserted in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def delete(self,dbname,tablename,fieldntype):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in value["data"]:
                    if i == fieldntype:
                        value["data"].remove(i)
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'w') as f:
                json.dump(value,f)
            self.end = time.time()
            print("Data deleted in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def update(self,dbname,tablename,fieldntype):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in value["data"]:
                    if i == fieldntype:
                        value["data"].remove(i)
                        value["data"].append(fieldntype)
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'w') as f:
                json.dump(value,f)
            self.end = time.time()
            print("Data updated in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def select(self,dbname,tablename,fieldntype):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in value["data"]:
                    if i == fieldntype:
                        print(i)
            self.end = time.time()
            print("Data selected in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def selectall(self,dbname,tablename):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in value["data"]:
                    print(i)
            self.end = time.time()
            print("Data selected in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def selectallfield(self,dbname,tablename):
        all = os.listdir('src/__pydb__/{}'.format(dbname))
        if tablename in all:
            self.start = time.time()
            with open('src/__pydb__/{}/{}.json'.format(dbname,tablename),'r') as f:
                value = json.load(f)
                for i in value["base"]:
                    print(i)
            self.end = time.time()
            print("Data selected in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Table does not exist (query time: ",self.end-self.start," seconds)")
            return 1
    def selectalltable(self,dbname):
        all = os.listdir('src/__pydb__')
        if dbname in all:
            self.start = time.time()
            for i in os.listdir('src/__pydb__/{}'.format(dbname)):
                print(i)
            self.end = time.time()
            print("Data selected in ",self.end-self.start," seconds")
            return 0
        else:
            self.start = time.time()
            self.end = time.time()
            print("Database does not exist (query time: ",self.end-self.start," seconds)")
            return 1
        
pydb = Pydb()
def mktable(dbname,tablename,fieldntype):
    pydb.tble(dbname, tablename, fieldntype)
def mkdb(dbname):
    pydb.db(dbname)
def insert(dbname,tablename,fieldntype):
    pydb.insert(dbname, tablename, fieldntype)
def delete(dbname,tablename,fieldntype):
    pydb.delete(dbname, tablename, fieldntype)
def update(dbname,tablename,fieldntype):
    pydb.update(dbname, tablename, fieldntype)
def select(dbname,tablename,fieldntype):
    pydb.select(dbname, tablename, fieldntype)
def selectall(dbname,tablename):
    pydb.selectall(dbname, tablename)
def selectallfield(dbname,tablename):
    pydb.selectallfield(dbname, tablename)
def selectalltable(dbname):
    pydb.selectalltable(dbname)
def dropdb(dbname):
    pydb.dropdb(dbname)
def droptable(dbname,tablename):
    pydb.drop(dbname, tablename)
def help():
    print("mktable(dbname,tablename,fieldntype) - Create a table")
    print("mkdb(dbname) - Create a database")
    print("insert(dbname,tablename,fieldntype) - Insert data into a table")
    print("delete(dbname,tablename,fieldntype) - Delete data from a table")
    print("update(dbname,tablename,fieldntype) - Update data in a table")
    print("select(dbname,tablename,fieldntype) - Select data from a table")
    print("selectall(dbname,tablename) - Select all data from a table")
    print("selectallfield(dbname,tablename) - Select all fields from a table")
    print("selectalltable(dbname) - Select all tables from a database")
    print("dropdb(dbname) - Drop a database")
    print("droptable(dbname,tablename) - Drop a table")
    print("help() - Show this help")
    print("exit() - Exit the program")
def exit():
    sys.exit()