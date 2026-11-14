# Python3

**1. install (python install manager)**
- `py install [version]`
- `py list`
- `py uninstall [version]`
- `python --version`

**2. config (isolate local & global)**
- `python -m venv (--prompt=[venv name]) .venv` + `.gitignore`
- `source .venv/bin/activate` **(linux)**
`. .venv\Scripts\Activate.ps1` **(powershell)**
- `python [code].py`
- `deactivate`

**3. dependency (package manager)**
- `pip install [package name](==[version])`
- `pip list`
- `pip show [package name]`
- `pip uninstall [package name]`
- `pip freeze > requirements.txt`
- `pip install -r requirements.txt`

# DBMS - SQL

#### 0. Configuration
- manager, user
- DBeaver

#### 1. DDL - definition
**DATABASE / USER / TABLE (COLUMN) / VIEW / INDEX / PROCEDURE / FUNCTION (RETURN) / TRIGGER**
- `CREATE`
- `ALTER`: column name + type + constranint (PK / FK)
- `DROP`

#### 2. DML - manipulation
**CRUD TABLE (ROW)** 
- `INSERT`
- `SELECT`
- `UPDATE`
- `DELETE`

#### 3. DCL - control

- `GRANT`
- `REVOKE`