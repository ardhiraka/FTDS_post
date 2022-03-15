# Data definition language

Data definition language (DDL) describes the portion of SQL that creates, alters, and deletes database objects. These database objects include schemas, tables, views, sequences, catalogs, indexes, variables, masks, permissions, and aliases.

## Creating a schema

A schema provides a logical grouping of SQL objects. To create a schema, use the CREATE SCHEMA statement.

A schema consists of a library, a journal, a journal receiver, a catalog, and optionally, a data dictionary. Tables, views, and system objects (such as programs) can be created, moved, or restored into any system libraries. All system files can be created or moved into an SQL schema if the SQL schema does not contain a data dictionary. If the SQL schema contains a data dictionary then:

Source physical files or nonsource physical files with one member can be created, moved, or restored into an SQL schema.

- Logical files cannot be placed in an SQL schema because they cannot be described in the data dictionary.
- You can create and own many schemas.

You can create a schema using the CREATE SCHEMA statement. For example, create a schema called DBTEMP:

`CREATE SCHEMA DBTEMP`

## Creating a table

A table can be visualized as a two-dimensional arrangement of data that consists of rows and columns. To create a table, use the CREATE TABLE statement.

The row is the horizontal part containing one or more columns. The column is the vertical part containing one or more rows of data of one data type. All data for a column must be of the same type. A table in SQL is a keyed or non-keyed physical file.

You can create a table using the CREATE TABLE statement. You provide a name for the table. If the table name is not a valid system object name, you can use the optional FOR SYSTEM NAME clause to specify a system name.

The definition includes the names and attributes of its columns. The definition can include other attributes of the table, such as the primary key.

Example: Given that you have administrative authority, create a table named 'INVENTORY' with the following columns:

- Part number: Integer between 1 and 9999, and must not be null
- Description: Character of length 0 to 24
- Quantity on hand: Integer between 0 and 100000

The primary key is PARTNO.

```sql
CREATE TABLE INVENTORY
                 (PARTNO         SMALLINT     NOT NULL,
                  DESCR          VARCHAR(24 ),
                  QONHAND        INT,
                  PRIMARY KEY(PARTNO))
```

## Creating a table using LIKE

You can create a table that looks like another table. That is, you can create a table that includes all of the column definitions from an existing table.

The following definitions are copied:

- Column names (and system column names)
- Data type, length, precision, and scale
- CCSID
- FIELDPROC

If the LIKE clause immediately follows the table name and is not enclosed in parentheses, the following attributes are also included:

- Column text (LABEL ON)
- Column heading (LABEL ON)
- Default value
- Hidden attribute
- Identity attribute
- Nullability

If the specified table or view contains an identity column, you must specify the option INCLUDING IDENTITY on the CREATE TABLE statement if you want the identity column to exist in the new table. The default behavior for CREATE TABLE is EXCLUDING IDENTITY. There are similar options to include the default value, the hidden attribute, and the row change timestamp attribute. If the specified table or view is a non-SQL-created physical file or logical file, any non-SQL attributes are removed.

Create a table EMPLOYEE2 that includes all of the columns in EMPLOYEE:

`CREATE TABLE EMPLOYEE2 LIKE EMPLOYEE`

## Creating a table using AS

You can create a table from the result of a SELECT statement. To create this type of table, use the CREATE TABLE AS statement.

All of the expressions that can be used in a SELECT statement can be used in a CREATE TABLE AS statement. You can also include all of the data from the table or tables that you are selecting from.

For example, create a table named EMPLOYEE3 that includes a subset of column definitions and data from the EMPLOYEE table where the WORKDEPT = D11.

```sql
CREATE TABLE EMPLOYEE3 AS
   (SELECT EMPNO, LASTNAME, JOB
    FROM EMPLOYEE
    WHERE WORKDEPT = 'D11') WITH DATA
```

If the specified table or view contains an identity column, you must specify the option INCLUDING IDENTITY on the CREATE TABLE statement if you want the identity column to exist in the new table. The default behavior for CREATE TABLE is EXCLUDING IDENTITY. There are similar options to include the default value, the hidden attribute, and the row change timestamp attribute. The WITH NO DATA clause indicates that the column definitions are to be copied without the data. If you want to include the data in the new table EMPLOYEE3, include the WITH DATA clause. If the specified query includes a non-SQL-created physical file or logical file, any non-SQL result attributes are removed.

## Creating indexes

You can use indexes to sort and select data. In addition, indexes help the system retrieve data faster for better query performance.

Use the CREATE INDEX statement to create indexes. The following example creates an index over the column LASTNAME in the CORPDATA.EMPLOYEE table:

  `CREATE INDEX CORPDATA.INX1 ON CORPDATA.EMPLOYEE (LASTNAME)`

You can also create an index that does not exactly match the data for a column in a table. For example, you can create an index that uses the uppercase version of an employee name:

  `CREATE INDEX CORPDATA.INX2 ON CORPDATA.EMPLOYEE (UPPER(LASTNAME))`

Most expressions allowed by SQL can be used in the definition of the key columns.

You can create any number of indexes. However, because the indexes are maintained by the system, a large number of indexes can adversely affect performance. One type of index, the encoded vector index (EVI), allows for faster scans that can be more easily processed in parallel.

If an index is created that has exactly the same attributes as an existing index, the new index shares the existing indexes' binary tree. Otherwise, another binary tree is created. If the attributes of the new index are exactly the same as another index, except that the new index has fewer columns, another binary tree is still created. It is still created because the extra columns prevent the index from being used by cursors or UPDATE statements that update those extra columns.

Indexes are created with the sort sequence in effect at the time the CREATE INDEX statement is run. The sort sequence applies to all SBCS character fields, or UCS-2 or UTF-16 graphic fields of the index.
