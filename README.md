# FastAPI-PostgreSQL Basic API

### Modules:
- Authentication
- Users
- Configurations 

## File Structure
```
project/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py
│   ├── db/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── session.py
│   │   └── init_db.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── user.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── misc.py
│   │   ├── sms.py
│   │   ├── email.py
│   │   └── security.py
│   └── api/
│       ├── __init__.py
│       └── routes_user.py
├── .env
├── requirements.txt
└── README.md
```

## Run on Windows

### Prerequisite
- Pip 3
- Python 3
- PgAdmin 4

### Setup Database
- Open pgAdmin4, login, then create database
- Open the project in your IDE, then change the **.env.example** to **.env**
- Open the **.env** file and update database credentials
    ```bash
    DATABASE_URL=postgresql+asyncpg://db_username:db_password@localhost:5432/db_name
    SECRET_KEY=mysecretkey 
    ```
    - change **localhost** to your posgresql server ip address, (dont change it if its on your computer)
    - change **5432** to your posgresql server port, (dont change it if its on your computer or have no issues)
    - change **db_username** to your posgresql server username
    - change **db_username** to your posgresql server password
    - change **db_name** to your posgresql database name
    - change **mysecretkey** if you have your own secret key

### Run the App
- Open terminal, then change directory to project path
```bash 
cd <project_path> 
``` 
- Create virtual environment
```bash
py -3 -m venv .venv
```
- Activate vitrual environment
```bash
.venv\Scripts\activate
```
- Upgrade pip (to lessen package error)
```bash
python -m pip install --upgrade pip
```
- Install packages from **requirements.txt**
```bash
pip install -r requirements.txt
```
- Auto generate database tables
```bash
python -m app.db.init_db
```
- Run app using uvicorn
```bash
uvicorn app.main:app --reload
```
- You can now open the [docs](http://127.0.0.1:8000/docs) to test the APIs
