# Ninkey
Python source code for open-source datastore api.

### Setting up Ninkey for use
In the clone or download button by the top right corner of the screen, click Download ZIP.  Once you do that, rename ```Ninkey-ninkey``` to ```ninkey```, then.  Now you will have to start coding.

Create a new Python file.  It can be called anything as long as it is not inside of the ```ninkey``` folder.

Type this code at the top of the ```Python``` script:
```python
from ninkey import *
```

This will import all the ninkey files.

### Creating and Using Datastores
Under the ```from ninkey import *```, you can start to code your datastore.
To start you will have to create a new datastore object.  This is how:
```python
ds1 = Datastore("ds1",['array','of','folders'])
```
This will create a directory here: C:/array/of/folders.  For each string in the array seperate it with a comma.  Each string will create a new folder, meaning ```['folder','1']``` will create ```C:/folder/1```.

Good job now we can add to the datastore!  First we should review everything...  your code should look like this:
```python
from ninkey import *
ds1 = Datastore("ds1",['array','of','folders'])
```

It doesn't have to be the same.  Just make sure you use an apostraphe to tell Python where the string is.
Anywho, lets start with adding data.
```python
ds1.store('datastore_1','Hello the name of this datastore is {n}')
```
The ```{n}``` will return ```datastore_1```, as a predefined variable when you create the datastore.  So now you want to get the data.  Do it this way:
```python
ds1.get('datastore_1')
```
Or even better, do this:
```python
print(ds1.get('datastore_1'))
```
Which will output ```Hello the name of this datastore is datastore_1```!  Congrats you have done it!  Your code should look like this:
```python
from ninkey import *
ds1 = Datastore("ds1",['array','of','folders'])
ds1.store('datastore_1','Hello the name of this datastore is {n}')
print(ds1.get('datastore_1'))
```

Good you are done!
