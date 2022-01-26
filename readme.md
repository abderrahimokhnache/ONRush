# ONRush

## NO-SQL Package Built upon SQLite

## Usage :


> Install :
```

pip install ONRush

```

> import :
```

from ONRush import Rush

```


> initializing the database 

```

db = Rush.DBConnect(FN = 'sample.db', TN = 'Table_name',TC = '(cloumn1 text,column2 varchr)')

```

> this method for inserting self.data into specific table

```

db.Add(TN = 'Tablename', VL = '(?,?)',Data = ( data1,data2 ))

```

> this method returns the table as Dictionary 

```

db.Listrequest(TN ='Tablename')

```

> this for deleting items 

```

db.DeleteRecord(Table_Name,ID,item)

```

> this method returns the specified item 

```

db.Listrequest2(Table_Name,ID,item)

```

> this method for updating items 

```

db.Update(Table_Name , Column , VL1 , Column1 ,VL2)

```
PYPI : https://pypi.org/project/ONRush/

### i have made ONRush first for my Green-Hole project it's named as ``SQL.py``` 

Check here : https://github.com/astroxiii/GREEN-HOLE 
