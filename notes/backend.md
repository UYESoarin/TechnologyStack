# Python3

**1. install (python install manager)**
- `py install [version]`, `-i https://pypi.tuna.isinghua.edu.cn/simple`
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

# HTTP

#### 1. Request

|part|note|
|:-|:-|
|request line|**method**: `GET`/`POST` (`-d`)/`PUT`/`PATCH`/`DELETE`/`HEAD`/`OPTIONS` <br> **path**: `api/[api name]`<br> version: `HTTP/2`/`HTTP/1.1`|
|request header|instructions (`[name]: [val]`)<br> `Host`/`User-Agent`/`Accept`/`Accpet-language`/`Content-Type`/`Content-Length`/`Authorization`/`Cookie`|
|blank line||
|request body||

#### 2. Response

|part|note|
|:-|:-|
|state line|version <br> **code**:`2xx`/`4xx`/`5xx`|
|response header|instructions: `[name]: [val]` <br> **`Content-Type`**/`Content-Length`/`Server`/`Date`/`Cache-Control`/`Set-Cookie`/`Location`/`Access-Control=Allow-Origin`|
|blank line||
|response body||

# FastAPI

#Framework

#### 1. Configuration

- **install:** `pip install "fastapi[standard]"`
- **router:** `@[var name].[method type]([path])` (`@app.get("/api/profile")`)
- **dev (hot update)**
`uvicorn [doc name]:[var name] --reload` / `fastapi dev`
`.gitignore`: `__pycache__/` + `*.py[cod]`
- **API docs:** `http://localhost:8000/docs`
#### 2. Integration

- **CORS - cross origin (F/B port) resources sharing**
`Origin: http://localhost:[frontend port]` - `Access-Control-Allow-Origin: http://localhost:[frontend port]`

```python
# GET permission
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
)
```

- **CORS - OPTIONS preflight to POST fetch**

```python
# POST permission
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["GET", "POST"],
)
```
- **.env.local:** api addr

- **flow:** Browser POST + OPTIONS Preflight - Request FastAPI - Python - FastAPI Response JSON - Frontend Refresh Page

# SQLite

#EmbeddedDatabase

#### 1. DataType

|type|MySQL|PostgreSQL|SQLite|
|:-|:-|:-|:-|
|Integer|INT, BIGINT|INTEGER, BIGINT|INTEGER|
|Decimal|DECIMAL, FLOAT, DOUBLE|NUMERIC, REAL|REAL|
|Text|VARCHAR, TEXT|VARHCAR, TEXT|TEXT|
|DateTime|DATE, DATETIME, TIMESTAMP|DATE, TIMESTAMP|\ (TEXT)|
|Boolean|TINYINT(1), BOOLEAN|BOOLEAN|\ (INTEGER 0/1)|

#### 2. Python REPL / Script 

- **connect db + cmd cursor**

```py
import sqlite3
conn = sqlite3.connect("[db name].db") # create if not exists
cur = conn.cursor()
```
- **autocommit (DDL: CREATE/ALTER/DROP)**

```py
cur.execute("""
CREATE TABLE tb(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    ...
)
""")
```

- **mannual commit (transaction)**

```py
cur.execute("[INSERT/UPDATE/DELETE]")
...
conn.commit()
```

- **query snapshot:** `cur.execute("[SELECT]")` + `.fetchall()` / `fecthone()` / `fetchmany()`

- **SQL injection defense (sql uses `?` placeholders for parameters):** `cur.execute(sql, ("v1", "v2", ...))`

#### 3. Structure

- **controller layer (HTTP API):** `@app.[api]`
- **service layer** 
- **mapper layer (SQL/ORM CRUD):** `import sqlite3` 
- **storage layer (DB + GUI):** `*.db` (`.gitignore`) + DB Browser for SQLite

# SQL

#RDBMS

#### 0. Configuration
- manager / user
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