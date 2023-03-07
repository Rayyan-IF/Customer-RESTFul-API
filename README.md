# Customer-RESTFul-API

Techincal Test - Backend Engineer (Rayyan)

## Technology Stack :

- Python 3.10.10
- Flask
- MySQL
- SQLAlchemy

## Pre-Requisite Softwares

- Visual Studio Code
- XAMPP (Version = 8.2.0)
- Postman

## Installation Steps :

1. Create Program Directory

```bash
$ mkdir API
```

2. Install requirements.txt

```bash
$ pip install -r requirements.txt
```

3. Create a table by importing the .sql file that has been provided

```bash
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:@127.0.0.1:3306/store'
```

```bash
'mysql+pymysql://<mysql_username>:<mysql_password>@<mysql_host>:<mysql_port>/<mysql_db>
```

4. Finally use the command below to run the API

```bash
$ flask run
```
