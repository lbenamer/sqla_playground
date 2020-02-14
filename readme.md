# SQL Alchemy Postgres Playground

### Requirements
- python 2.7
- virtualenv
- Docker

### Install

```bash
$ git clone git@github.com:lbenamer/sqla_playground.git sqlapp
$ cd sqlapp
$ bash install.sh
```

### Launch
```bash
$ bash launch.sh
```

### Uninstall
```bash
$ bash uninstall.sh
```

---

## SqlApp Module
```python

from sqlapp import SqlApp

s = SqlApp()
s.connect('postgresql://postgres@localhost:5532/sqlapp')
```

### Declare and create a model

```python
from sqlalchemy import Column, Integer, String

Base = s.Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,
        primary_key=True,
        nullable=False,
    )
    name = Column(String(), nullable=False)
    city = Column(String(), nullable=False)

# Create user table in db
s.create_models(Base)
```

### Create record

```python
user = User(name='player', city='paris')

s.create(user)
```

You also create multiple records with the `populate()` method :  
```python
ROWS = [
    { 'name': 'Walid', 'city': 'Djerba' },
    { 'name': 'Mathias', 'city': 'Tours' },
]

s.populate(User, ROWS)
```

### Query

```python
player = s.session.query(User).filter_by(name='player').first()

player.city
```

### Delete a record
```python
player = s.session.query(User).filter_by(name='player').first()

s.delete(player)
```

## The SQL inner class
This inner class contain methods to directly interact with the database

### List all tables in db
```python
s.sql.tables
```

### Drop Tables
``` python
# Drop a table
s.sql.drop_table('user')

## Drop all tables
s.sql.drop_all_table()
```
