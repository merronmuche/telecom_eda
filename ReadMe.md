

# how to run the Project

clone the project 
```
git clone git@github.com:merronmuche/eda.git
```
then create a virtual environment
```virtualenv venv
source venv/bin/activate
```
then run the requirements

```
pip install -r requirements.txt
```
add the data to your database

```
psql -U postgres -d telecom -h localhost -p 5434 -f telecom.sql
postgres = user_name
telecom = database_name
telecom.sql = path of sql file
```