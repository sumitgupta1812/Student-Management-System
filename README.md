# Student-Management-System

### Libraries used - 
```
1. Tkinter.
2. SQLite3.
```

#### Tkinter Code Sample 

```
root=tk.Tk()
root.title("Management System")

appLabel=tk.Label(root,text="Management System",width=20)
appLabel.config(font=("Sylfean",30))
```

#### Sqlite Code Sample

```

create_table_query= " CREATE TABLE IF NOT EXISTS " + TABLE_NAME + "( " + EMP_ID + " INTEGER PRIMARY KEY AUTOINCREMENT, " + EMP_NAME + " TEXT," + EMP_ADDRESS + " TEXT," + EMP_PHONE +" INTEGER );"
connection.execute(create_table_query)
print("Table created successfully.")
```

#### Screenshots 

##### 1. Home page
![alt home](https://github.com/sumitgupta1812/Student-Management-System/blob/master/Home.png)

##### 2. Display Records
![alt records](https://github.com/sumitgupta1812/Student-Management-System/blob/master/display_record.png)
