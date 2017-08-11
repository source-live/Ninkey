import os


print("Ninkey datastore system.")

class Datastore:  # Used Datastore("myds",["my","path"])
  ds_path = ""
  def __init__(ds,path):
    s_path = "/".join(path)
    f_path = "".join(["C:/",s_path])                # e.g. Datastore("myds",['super','path'])  =  C:/super/path
    os.mkdirs(f_path)
    ds_path = f_path
    print("".join(["Successfully created datastore path ",f_path])) #e.g. Datastore.name("myds",['super','path'])  =  Successfully created datastore path C:/super/path
    
  def store(name,data):
    if ds_path == None:
      print("No specified datastore.")
    else:
      data = data.format(n=name) # So you can use the ds name in the content, e.g. Datastore.store("Datastore name: {n}","my_datastore")
      path = os.path.join(ds_path, "".join([name,".ds"]))
      f = open(filepath, "w+")
      f.write(data)
      
  def get(name):
    if ds_path == None:
      print("No specified datastore.")
    else:
      path = os.path.join(ds_path, "".join([name,".ds"]))
      f = open(filepath, "r")
      return f
