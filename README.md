# Ninkey
Python source code for open-source datastore api.

#### Datastore guide
```python
from Ninkey import *
# Start the system
# Way one:
file = ds("my_ds",["sl","dstore"])
file.store("my_name","zack")              # Outputs to my_name.ds in the C:/sl/dstore folder.

# Way two:
ds("my_ds",["sl","dstore"]).store("my_name","zack")
```
