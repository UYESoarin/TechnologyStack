## MySQL

**link DB:** mysql -u[username] -p[password] (-h127.0.0.1)

### 1. database

|   op   |             code             |
| :----: | :---------------------------: |
| create | `create database [DB name]` |
| check |      `show databases`      |
| locate |       `use [DB name]`       |

### 2. table

**CRUD**

|                op                |                                                                                                                   code                                                                                                                   |                                   note                                   |
| :------------------------------: | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: | :-----------------------------------------------------------------------: |
|         **table**         |                                                                                                                                                                                                                                          |                                                                          |
|              create              |                                                                                     `create table [TB name] ([D name] [D type] [constraint], ...)`                                                                                     |                         `default charset=utf8`                         |
|            constraint            | `(constraint [PK name]) primary key ([D name])`  `unique`  `not null`  `default [val]`  `auto_increment`  `constraint [FK name] foreign key ([D name]) references [TB name] ([RK name])`  `check([D name] = [val1] or ...)` |                             append definition                             |
|              index              |                                                                                                       `index [Idx name] (D name)`                                                                                                       |                                  create                                  |
|              check              |                                                                                                              `show tables`                                                                                                              |                                                                          |
|               read               |                                                                                        `describe [TB name]`  `show create table [TB name] \G`                                                                                        |                                                                          |
|            del table            |                                                                                                         `drop table [TB name]`                                                                                                         |                                                                          |
|           rename table           |                                                                                                `alter table [TB name] rename [new name]`                                                                                                |                                                                          |
| **field (col) with alter** |                                                                                                                                                                                                                                          |                                                                          |
|         change field def         |                                                                                       `alter table [TB name] change [D name] [new name] [D type]`                                                                                       |                                                                          |
|         modify field seq         |                                                                              `alter table [TB name] modify [D name] [new type] (first / after [RD name])`                                                                              |                                                                          |
|            add field            |                                                                          `alter table [TB name] add [D name] [D type] [constraint] (first / after [RD name])`                                                                          |             `add constraint [PK name] primary key (D name)`             |
|            del field            |                                                                                                  `alter table [TB name] drop [D name]`                                                                                                  |                                                                          |
|              del FK              |                                                                                           `alter table [TB name] drop foreign key [FK name]`                                                                                           |                                                                          |
|           constranint           |                                                                                      `alter table [TB name] add constraint [C name] [C sentence]`                                                                                      |                                                                          |
|          **row**          |                                                                                                                                                                                                                                          |                                                                          |
|              insert              |                                                                                     `insert into [TB name]([D name1], ...) values(val1, ...), ...`                                                                                     |                                                                          |
|              update              |                                                                                             `update [TB name] set [D name1] = [val1], ...`                                                                                             |                                 `where`                                 |
|             del row             |                                                                                                 `delete [alias] from [TB name] [alias]`                                                                                                 |                     `where exists (select(select))`                     |
|             del all             |                                                                                                       `truncate table [TB name]`                                                                                                       |                                                                          |
|          **view**          |                                                                                                                                                                                                                                          |                                                                          |
|              create              |                                                                                         `create view [V name]([D name], ...) as select(table)`                                                                                         |                                                                          |
|               del               |                                                                                                          `drop view [V name]`                                                                                                          |                                                                          |
|         **index**         |                                                                                                                                                                                                                                          |                                                                          |
|              create              |                                                  `create (unique) index [Idx name] on [Tb name](D name1, ...)`  `alter table [TB name] add index / unique [Idx name](D name1, ...)`                                                  | `create table TB (id int(11) not null auto_increment, primary key(id))` |
|               del               |                                                                          `drop index [Idx name] on [TB name]`  `alter table [Tb name] drop index [Idx name]`                                                                          |                                                                          |
|               read               |                                                                                                       `show index from [TB name]`                                                                                                       |                                                                          |

###### `with tmp as(select)`

### 3. select

* **flow:** from / join - where - group by - aggregate func - having - select - order by - limit

```
select (distinct) [fields] as [alias]
from [tables] [alias]
[left / right / inner] join [tables] on [conds]
where [conds]
group by [fields - index]
having [conds]
order by [field] [asc / desc]
limit [offset], [row num]
(union (all) / intersect / except select)
```

|        flag        |                                                        code                                                        |
| :-----------------: | :----------------------------------------------------------------------------------------------------------------: |
|  **select**  |                                                                                                                    |
|     `[field]`     |                   `*` `[D name1], ...` `if([cond], '[name1]', [name2])` `[val]` `case`                   |
|     `[table]`     |                                             `[TB name]` `(select)`                                             |
| **subselect** |                                                                                                                    |
|      `[val]`      |                                            `select [aggregate func]`                                            |
|      `[col]`      |                                                 `select [field]`                                                 |
|     `[table]`     |                                               `select [field(s)]`                                               |
|     `[page]`     | `select [id] from [table] where id >= (select [id] from [table] limit [offset], 1) order by id limit [row num];` |

|                               cond                               |                                                                     note                                                                     |
| :---------------------------------------------------------------: | :------------------------------------------------------------------------------------------------------------------------------------------: |
|                    `if` `ifnull` `case`                    | `if([cond], [v1], [v2])` - `[cond]?[v1]:[v2]`  `ifnull(a, b)` - `a != NULL?a:b`  `case when [cond1] then [v1], ..., else [vn] end` |
| `in` (or)  `between and` (range)  `like`  `is (not) null` |                     `in ([vals]: [val1], [val2], ...)`  `in ([cols]: [TB1].[D1], [TB1].[D2], ..)`  `like [% / _]`                     |
|                      `and` `or` `not`                      |                                                                                                                                              |
|                      `op: > < >= <= <> !=`                      |                                                                                                                                              |
|                          `all` `any`                          |                                               `(not) ([op] / in) (all / any) [(col / set)]`                                               |
|                            `exists`                            |                                                  `not exists (select 1 where not exists)`                                                  |

|                             func                             |                                                                                          note                                                                                          |
| :----------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------: |
|                   **aggregate func**                   |                                                                                                                                                                                        |
|                          `count`                          |                                                                        `* / 1`, `if([cond], 1, null) / case`                                                                        |
|                       `sum` `avg`                       |                                                                    `* / [digit]`, `if([cond], [num], 0) / case`                                                                    |
|                       `max` `min`                       |                                                                                                                                                                                        |
|                    **string func**                    |                                                                                                                                                                                        |
|                          `length`                          |                                                                                  `length('str')` - 3                                                                                  |
|                  `concat`  `concat_ws`                  |                                                    `concat(s1, s2, ...)` - s1 + s2  `concat('f', 's1', 's2', ...)` - 's1-s2-...'                                                    |
|              `left`  `right`  `substring`              | `left('string', 3)` - 'str'  `right('string', 3)` - 'ing'  `substring('12345', 3, 5)` - '345'  `substring('12345', 3)` - '345'  `substring_index('11-22-33', '-', -1)` - '33' |
|                `trim`  `ltrim`  `rtrim`                |                                             `trim(' 1 2 3 ')` - '1 2 3'  `ltrim(' 1 2 3 ')` - '1 2 3 '  `rtrim(' 1 2 3 ')` - ' 1 2 3'                                             |
|                         `replace`                         |                                                       `replace('123', '23', '')` - '1'  `replace('123', '23', '45') - '145'`                                                       |
|                     `lower` `upper`                     |                                                                                                                                                                                        |
|                    **digital func**                    |                                                                                                                                                                                        |
|          `ceil` `floor`  `round` `truncate`          |                                                  `round(3.1415, 3)` - 3.142  `round(3.1415)` - 3  `truncate(3.1415, 3)` - 3.141                                                  |
|                  `power` `sqrt` `abs`                  |                                                                                                                                                                                        |
|          `div` (c - `/`)  `mod` (c -`fmod`)          |                                                           `3 / 4` - 0.75, `3 div 4` - 0  `5 % 3` - 2, `5.2 % 3` - 2.2                                                           |
|                     **time func**                     |                                                                                                                                                                                        |
| `now` `curdate` `curtime`  `year` `month` `week` |                                                                                                                                                                                        |
|                  `date_add`  `datediff`                  |                                  `date_add('xxxx-xx-xx', interval + / - n year / months / week / day)`  `datediff('2026-10-01', '2026-09-30')` - 1                                  |
| `date_format('xxxx-xx-xx', %m / %d / %Y) - mm / dd / yyyy` |                                                                                     `%H %h %s %T`                                                                                     |

### 4. user

|op|code|
|create|`create user '[uname]'@'[IP]' identified by '[password]'`|
|del|`drop user '[uname]'@'[IP]'`|
|rename|`rename user '[uname]'@'[IP]' to '[new name]'@'[IP]'`|
|reset password|`set password for '[uname]'@'[IP]' = Password('[new password]')`|
|check grants|`show grants for '[uname]'@'[IP]'`|
|grant|`grant [all / select / insert / update]([D names]) on [DB].[TB] to '[uname]'@'[IP]' identified by '[password]'`  `flush privileges`|
|revoke|`revoke [list] on [DB].[TB] from '[uname]'@'[IP]'`|

**function**

```
delimiter // -- end flag
[global var]
create [function / procedure] [func name]([params name] [params type]) returns [ret type]
begin
    [var op]
    return [ret val]
end;
//
delimiter ;
```

|          op          |                                               code                                               |
| :------------------: | :----------------------------------------------------------------------------------------------: |
|    def global var    |                                 `set @g_user_var := init_val`                                 |
|    def local var    |                      `declare [var name] [var type] (default [init val])`                      |
| create one line func |                   `create funcion [FN]([DN] [DT]) returns [RT] return [RV];`                   |
|       del func       |                                      `drop function [FN]`                                      |
|         call         |                                       `call [proc name]`                                       |
|        check        | `show procedure status where db = '[DB name]`  `show create procedure [DB name].[proc name]` |
|       del proc       |                             `drop procedure [DB name].[proc name]`                             |