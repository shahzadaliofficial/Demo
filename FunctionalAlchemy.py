# Step 2: Create an SQLite Database with SQLAlchemy

from sqlalchemy  import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Step 2.1: Create the SQLite database and engine
engine=create_engine('sqlite:///test.db',echo=True)

# Step 2.2: Define the Base class
Base=declarative_base()


# Step 2.3: Define a Table (Mapped Class)

class User(Base):
    __tablename__='users'
    id=Column(Integer, primary_key=True, unique=True, autoincrement=True)
    name=Column(String, nullable=False)
    age=Column(Integer, nullable=False)

# Step 2.4: Create the table in the database
Base.metadata.create_all(engine)

# Step 3: Create a Session
# Step 3.1: Create a session factory
Session=sessionmaker(bind=engine)

# Step 3.2: Create a session
session=Session()

# Step 4: Insert Data
# Step 4.1: Create a new user instance
user1=User(name='John Doe', age=30)
user2=User(name='Jane Smith', age=25)


# Step 4.2: Add the user to the session
session.add(user1)
session.add(user2)

# Step 4.3: Commit the transaction
session.commit()

# Step 5: Query Data
# Retrieve data from the table using SQLAlchemy's query system.

#step 5.1: Query all users
users=session.query(User).all()

#Print the results
for user in users:
    print(f'Id: {user.id}, Name: {user.name}, Age: {user.age}')

#Step 5.2: Query a specific user
user=session.query(User).filter_by(name='John Doe').first()
if user:
    print(f'Found user: Id: {user.id}, Name: {user.name}, Age: {user.age}')
else:
    print('User not found of name "John Doe"')    

#step 5.3: Query users with id:
user = session.query(User).filter_by(id=2).first()
if user:
    print(f"found user: Id: {user.id}, Name: {user.name}, Age: {user.age}")
else:
    print('User not found with id 2')

# Using filter() to query users with age >= 25, 
# filter_by() is used to filter by a specific column by keyword arguments
users = session.query(User).filter(User.age >= 25).all()
if users:
    for user in users:
        print(f"found user: Id: {user.id}, Name: {user.name}, Age: {user.age}")
else:
    print('User not found with age >= 25')

#step 6: Update Data
# Step 6.1: Update a user's age
user = session.query(User).filter_by(name='John Doe').first()
if user: 
    user.age=29
    session.commit()
    print(f'Updated user: Id: {user.id}, Name: {user.name}, Age: {user.age}')
else:
    print('User not found of name "John Doe"')          

# Step 7: Delete Data
# Step 7.1: Delete a user by id
user=session.query(User).filter_by(id=3).first()
if user: 
    session.delete(user)
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker


#Creating DB with engine
engine=create_engine("sqlite:///usersf.db", echo=True)
Base=declarative_base()

class User(Base):
    __tablename__="users"
    id=Column(Integer, primary_key=True, autoincrement=True)
    name=Column(String, nullable=False)
    age = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

Session=sessionmaker(bind=engine)
session=Session()

#Functions
def getAllUsers():
    users=session.query(User).all()
    return users

def displayAllUsers(users):
    users=getAllUsers()
    if users:
        for user in users:
            print(user.id, user.name, user.age)
    else:
        print("No Users Found!")

def addNewUser(name,age):
    """
    Adds a new user to the database with the specified name and age.
    
    Args:
        name: The name of the user to add.
        age: The age of the user to add.
    """
    user=User(name=name, age=age)
    newUser=session.add(user)

    session.commit()
    print(f'Deleted user: Id: {user.id}, Name: {user.name}, Age: {user.age}')
else:
    print('User not found with id 3')
# Step 7.2: Delete all users
users=session.query(User).all()
if users:
    for user in users:
        session.delete(user)
    session.commit()
    print('Deleted all users')
else:
    print('No users to delete')


# Step 8: Close the session
session.close()
# Step 9: Close the engine
engine.dispose()
