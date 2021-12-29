# Rush-db

## NO-SQL Packages Built upon SQLite

### rush-db makes working with data base easy by taking all the heavy stuff

## Usage :



> Install :
```

pip3 install Rush_db

```
> import :
```

from Rush_db import Rush_db

```


> initializing the database 

```

db = Rush_db.DBConnect(FN = 'sample.db', TN = 'Table_name',TC = '(cloumn1 text,column2 varchr)')

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
