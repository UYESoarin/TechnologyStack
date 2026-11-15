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

**1. install:** `pip install "fastapi[standard]"`
**2. router:** `@[var name].[method type]([path])` (`@app.get("/api/profile")`)
**3. dev (hot update):** `uvicorn [doc name]:[var name] --reload` / `fastapi dev` + `.gitignore`: `__pycache__/`, `*.py[cod]`
**4. APIdocs:** `http://localhost:8000/docs`

# DBMS - SQL

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