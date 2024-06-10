# Database Cheatsheet

These are based on MySQL and Postgres.

_Note that most databases have a slightly different syntax._

## 1.Based on MYSQL

## DDL

### CREATE Clause

```sql
CREATE TABLE table_name (
    column_name1 datatype(size),
    column_name2 datatype(size),
    ...,
    column_name3 datatype(size),
    any constraints
);
```

Size and constraints are optional. For example:

```sql
CREATE TABLE drink (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(100),
    type VARCHAR(100),
    temperature VARCHAR(100),
    PRIMARY KEY(id)
);
```

### ALTER Clause

```sql
ALTER TABLE table_name
  ADD column_name column_definition;
```

```sql
ALTER TABLE table_name
  MODIFY column_name column_type;
```

For Example:

```sql
ALTER TABLE supplier ADD supplier_name char(50);
```

```sql
ALTER TABLE supplier MODIFY supplier_name VARCHAR(100) NOT NULL;
```

Follow this for more: [alter command](https://www.techonthenet.com/sql/tables/alter_table.php)

### DROP Clause

```sql
DROP TABLE table_name
```

For Example:

```sql
DROP TABLE drink
```

### Useful commands:

```sql
show databases

use database_name

describe table_name
```

## DML

### SELECT Clause

```sql
SELECT * FROM drink WHERE type='tea' ORDER BY temperature DESC
```

### INSERT Clause

```sql
INSERT INTO table_name (column1, column2,...columne_n) 
    VALUES (value1, value2,.. value_n)
```

For Example:

If `id` is not auto-generated

```sql
INSERT INTO drink (id, name, type, temperature) 
    VALUES (123, 'americano', 'coffee', 'hot')
```

If `id` is auto-generated

```sql
INSERT INTO drink (name, type, temperature) 
    VALUES ('americano', 'coffee', 'hot')
```

### UPDATE Clause

```sql
UPDATE table_name
SET column1 = value1, column2 = value2, ...
WHERE condition;
```

For Example:

```sql
UPDATE drink SET temperature = 'cold' WHERE type = 'tea'
```

### DELETE Clause

```sql
DELETE FROM table_name WHERE condition
```

For Example:

```sql
DELETE FROM drink WHERE type = 'tea'
```

## 2.Based on Postgres SQL

## DDL

### CREATE Clause

```sql
CREATE TABLE drink (
    id INTEGER GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(100),
    type VARCHAR(100),
    temperature VARCHAR(100),
    PRIMARY KEY(id)
);
```

### ALTER Clause

```sql
ALTER TABLE drink ADD milky TINYINT;
```

### DROP Clause

```sql
DROP TABLE drink
```

### Useful commands:

```sql
show databases

use database

describe table
```

## DML

### SELECT Clause

```sql
SELECT * FROM drink WHERE type='tea' ORDER BY temperature DESC
```

### INSERT Clause

If `id` is not auto-generated

```sql
INSERT INTO drink (id, name, type, temperature) 
    VALUES (123, 'americano', 'coffee', 'hot')
```

If `id` is auto-generated

```sql
INSERT INTO drink (name, type, temperature) 
    VALUES ('americano', 'coffee', 'hot')
```

### UPDATE Clause

```sql
UPDATE drink SET temperature = 'cold' WHERE type = 'tea'
```

### DELETE Clause

```sql
DELETE FROM drink WHERE type = 'tea'
```
