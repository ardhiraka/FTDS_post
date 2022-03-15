# Data manipulation language

Data manipulation language (DML) describes the portion of SQL that manipulates or controls data.

## Retrieving data using the SELECT statement

The SELECT statement tailors your query to gather data. You can use the SELECT statement to retrieve a specific row or retrieve data in a specific way.

### Basic SELECT statement

A SELECT statement can include the following:

- The name of each column you want to include in the result.
- The name of the table or view that contains the data.
- A search condition to identify the rows that contain the information you want.
- The name of each column used to group your data.
- A search condition that uniquely identifies a group that contains the information you want.
- The order of the results.
- An offset into the result set to enable skipping a number of rows.
- The number of rows to return.

A SELECT statement looks like this:

```sql
   SELECT column names
     FROM table or view name
     WHERE search condition
     GROUP BY column names
     HAVING search condition
     ORDER BY column-name
     OFFSET number of rows
     FETCH FIRST n ROWS ONLY
```

The SELECT and FROM clauses must be specified. The other clauses are optional.

### Specifying a search condition using the WHERE clause

The WHERE clause specifies a **search condition** that identifies the row or rows that you want to retrieve, update, or delete.

The number of rows you process with an SQL statement then depends on the number of rows that satisfy the WHERE clause search condition. A search condition consists of one or more **predicates**. A predicate specifies a test that you want SQL to apply to a specified row or rows of a table.

In the following example, WORKDEPT = 'C01' is a predicate, WORKDEPT and 'C01' are expressions, and the equal sign (=) is a comparison operator. Note that character values are enclosed in apostrophes ('); numeric values are not. This applies to all constant values wherever they are coded within an SQL statement. For example, to specify that you are interested in the rows where the department number is C01, issue the following statement:

`... WHERE WORKDEPT = 'C01'`

In this case, the search condition consists of one predicate: WORKDEPT = 'C01'.

To further illustrate WHERE, put it into a SELECT statement. Assume that each department listed in the CORPDATA.DEPARTMENT table has a unique department number. You want to retrieve the department name and manager number from the CORPDATA.DEPARTMENT table for department C01. Issue the following statement:

```sql
SELECT DEPTNAME, MGRNO
       FROM CORPDATA.DEPARTMENT
       WHERE DEPTNO = 'C01'
```

### Expressions in the WHERE clause

An expression in a WHERE clause names or specifies something that you want to compare to something else.

The expressions you specify can be:

A column name names a column. For example:

`... WHERE EMPNO = '000200'`

`... WHERE INTEGER(PRENDATE - PRSTDATE) > 100`

`... WHERE 40000 < SALARY`

`... WHERE DUE_DATE IS NULL`

You can precede a predicate with the NOT keyword to specify that you want the opposite of the predicate's value (that is, TRUE if the predicate is FALSE).

NOT applies only to the predicate it precedes, not to all predicates in the WHERE clause. For example, to indicate that you are interested in all employees except those working in the department C01, you can say:

`... WHERE NOT WORKDEPT = 'C01'`

which is equivalent to:

`... WHERE WORKDEPT <> 'C01'`

### GROUP BY clause

The GROUP BY clause allows you to find the characteristics of groups of rows rather than individual rows.

When you specify a GROUP BY clause, SQL divides the selected rows into groups such that the rows of each group have matching values in one or more columns or expressions. Next, SQL processes each group to produce a single-row result for the group. You can specify one or more columns or expressions in the GROUP BY clause to group the rows. The items you specify in the SELECT statement are properties of each group of rows, not properties of individual rows in a table or view.

Without a GROUP BY clause, the application of SQL aggregate functions returns one row. When GROUP BY is used, the function is applied to each group, thereby returning as many rows as there are groups.

For example, the CORPDATA.EMPLOYEE table has several sets of rows, and each set consists of rows describing members of a specific department. To find the average salary of people in each department, you can issue:

```sql
SELECT WORKDEPT, DECIMAL (AVG(SALARY),5,0)
       FROM CORPDATA.EMPLOYEE
       GROUP BY WORKDEPT
```

### HAVING clause

The HAVING clause specifies a search condition for the groups selected by the GROUP BY clause.

The HAVING clause says that you want only those groups that satisfy the condition in that clause. Therefore, the search condition you specify in the HAVING clause must test properties of each group rather than properties of individual rows in the group.

The HAVING clause follows the GROUP BY clause and can contain the same kind of search condition as you can specify in a WHERE clause. In addition, you can specify aggregate functions in a HAVING clause. For example, suppose that you want to retrieve the average salary of women in each department. To do this, use the AVG aggregate function and group the resulting rows by WORKDEPT and specify a WHERE clause of SEX = 'F'.

To specify that you want this data only when all the female employees in the selected department have an education level equal to or greater than 16 (a college graduate), use the HAVING clause. The HAVING clause tests a property of the group. In this case, the test is on MIN(EDLEVEL), which is a group property:

```sql
SELECT WORKDEPT, DECIMAL(AVG(SALARY),5,0) AS AVG_WAGES, MIN(EDLEVEL) AS MIN_EDUC
       FROM CORPDATA.EMPLOYEE
       WHERE SEX='F'
       GROUP BY WORKDEPT
       HAVING MIN(EDLEVEL)>=16
```

### ORDER BY clause

The ORDER BY clause specifies the particular order in which you want selected rows returned. The order is sorted by ascending or descending collating sequence of a column's or an expression's value.

For example, to retrieve the names and department numbers of female employees listed in the alphanumeric order of their department numbers, you can use this select-statement:

```sql
SELECT LASTNAME,WORKDEPT
       FROM CORPDATA.EMPLOYEE
       WHERE SEX='F'
       ORDER BY WORKDEPT
```

The column specified in the ORDER BY clause does not need to be included in the SELECT clause. For example, the following statement will return all female employees ordered with the largest salary first:

```sql
SELECT LASTNAME,FIRSTNME
       FROM CORPDATA.EMPLOYEE
       WHERE SEX='F'
       ORDER BY SALARY DESC
```

### Handling null values

A null value indicates the absence of a column value in a row. A null value is an unknown value; it is not the same as zero or all blanks.

Null values can be used as a condition in the WHERE and HAVING clauses. For example, a WHERE clause can specify a column that, for some rows, contains a null value. A basic comparison predicate using a column that contains null values does not select a row that has a null value for the column. This is because a null value is not less than, equal to, or greater than the value specified in the condition. The IS NULL predicate is used to check for null values. To select the values for all rows that contain a null value for the manager number, you can specify:

```sql
SELECT DEPTNO, DEPTNAME, ADMRDEPT
  FROM CORPDATA.DEPARTMENT
  WHERE MGRNO IS NULL
```

### Casting data types

Sometimes you need to cast or change the type of an expression to a different data type or to the same data type with a different length, precision, or scale.

For example, if you want to compare two columns of different types, such as a user-defined type based on a character and an integer, you can change the character to an integer or the integer to a character to make the comparison possible. A data type that can be changed to another data type is castable from the source data type to the target data type.

You can use cast functions or CAST specification to explicitly cast a data type to another data type. For example, if you have a column of dates (BIRTHDATE) defined as DATE and want to cast the column data type to CHARACTER with a fixed length of 10, enter the following:

```sql
SELECT CHAR (BIRTHDATE,USA)
   FROM CORPDATA.EMPLOYEE
```

You can also use the CAST specification to cast data types directly:

```sql
SELECT CAST(BIRTHDATE AS CHAR(10))
   FROM CORPDATA.EMPLOYEE
```

### Handling duplicate rows

When SQL evaluates a select-statement, several rows might qualify to be in the result table, depending on the number of rows that satisfy the search condition of the select-statement. Some of the rows in the result table might be duplicate.

You can specify that you do not want any duplicates by using the DISTINCT keyword, followed by the list of expressions:

```sql
SELECT DISTINCT JOB, SEX
...
```

DISTINCT means that you want to select only the unique rows. If a selected row duplicates another row in the result table, the duplicate row is ignored (it is not put into the result table). For example, suppose you want a list of employee job codes. You do not need to know which employee has what job code. Because it is probable that several people in a department have the same job code, you can use DISTINCT to ensure that the result table has only unique values.

The following example shows how to do this:

```sql
  SELECT DISTINCT JOB
      FROM CORPDATA.EMPLOYEE
      WHERE WORKDEPT = 'D11'
```

### Defining complex search conditions

In addition to the basic comparison predicates, such as = and >, a search condition can contain any of these predicates: BETWEEN, IN, EXISTS, IS NULL, and LIKE.

A search condition can include a scalar fullselect.

For character, or UCS-2 or UTF-16 graphic column predicates, the sort sequence is applied to the operands before evaluation of the predicates for BETWEEN, IN, EXISTS, and LIKE clauses.

You can also perform multiple search conditions.

- **BETWEEN ... AND ...** is used to specify a search condition that is satisfied by any value that falls on or between two other values. For example, to find all employees who were hired in 1987, you can use this:

`... WHERE HIREDATE BETWEEN '1987-01-01' AND '1987-12-31'`

The BETWEEN keyword is inclusive. A more complex, but explicit, search condition that produces the same result is:

`... WHERE HIREDATE >= '1987-01-01' AND HIREDATE <= '1987-12-31'`

- **IN** says you are interested in rows in which the value of the specified expression is among the values you listed. For example, to find the names of all employees in departments A00, C01, and E21, you can specify:

`... WHERE WORKDEPT IN ('A00', 'C01', 'E21')`

- **EXISTS** says you are interested in testing for the existence of certain rows. For example, to find out if there are any employees that have a salary greater than 60000, you can specify:

`EXISTS (SELECT * FROM EMPLOYEE WHERE SALARY > 60000)`

- **IS NULL** says that you are interested in testing for null values. For example, to find out if there are any employees without a phone listing, you can specify:

`... WHERE EMPLOYEE.PHONE IS NULL`

- **LIKE** says you are interested in rows in which an expression is similar to the value you supply. When you use LIKE, SQL searches for a character string similar to the one you specify. The degree of similarity is determined by two special characters used in the string that you include in the search condition:

**_**\
An underline character stands for any single character.

**%**\
A percent sign stands for an unknown string of 0 or more characters. If the percent sign starts the search string, then SQL allows 0 or more character(s) to precede the matching value in the column. Otherwise, the search string must begin in the first position of the column.

Use the underline character or percent sign either when you do not know or do not care about all the characters of the column's value. For example, to find out which employees live in Minneapolis, you can specify:

`... WHERE ADDRESS LIKE '%MINNEAPOLIS%'`

SQL returns any row with the string MINNEAPOLIS in the ADDRESS column, no matter where the string occurs.

In another example, to list the towns whose names begin with 'SAN', you can specify:

`... WHERE TOWN LIKE 'SAN%'`

If you want to find any addresses where the street name isn't in your master street name list, you can use an expression in the LIKE expression. In this example, the STREET column in the table is assumed to be upper case.

`... WHERE UCASE (:address_variable) NOT LIKE '%'||STREET||'%'`

If you want to search for a character string that contains either the underscore or percent character, use the ESCAPE clause to specify an escape character. For example, to see all businesses that have a percent in their name, you can specify:

`... WHERE BUSINESS_NAME LIKE '%@%%' ESCAPE '@'`

The first and last percent characters in the LIKE string are interpreted as the normal LIKE percent characters. The combination '@%' is taken as the actual percent character.

### Multiple search conditions within a WHERE clause

You can qualify your request further by coding a search condition that includes several predicates.

The search condition you specify can contain any of the comparison operators or the predicates BETWEEN, DISTINCT, IN, LIKE, EXISTS, IS NULL, and IS NOT NULL.

You can combine any two predicates with AND and OR. In addition, you can use the NOT keyword to specify that the search condition that you want is the negated value of the specified search condition. A WHERE clause can have as many predicates as you want.

- **AND** says that, for a row to qualify, the row must satisfy both predicates of the search condition. For example, to find out which employees in department D21 were hired after December 31, 1987, specify:

```sql
...
  WHERE WORKDEPT = 'D21' AND HIREDATE > '1987-12-31'
```

- **OR** says that, for a row to qualify, the row can satisfy the condition set by either or both predicates of the search condition. For example, to find out which employees are in either department C01 or D11, you can specify :

```sql
...
  WHERE WORKDEPT = 'C01' OR WORKDEPT = 'D11'
```

Note: You can also use IN to specify this request: WHERE WORKDEPT IN ('C01', 'D11').

- **NOT** says that, to qualify, a row must not meet the criteria set by the search condition or predicate that follows the NOT. For example, to find all employees in the department E11 except those with a job code equal to analyst, you can specify:

```sql
...
  WHERE WORKDEPT = 'E11' AND NOT JOB = 'ANALYST'
```

When SQL evaluates search conditions that contain these connectors, it does so in a specific order. SQL first evaluates the NOT clauses, next evaluates the AND clauses, and then the OR clauses.

You can change the order of evaluation by using parentheses. The search conditions enclosed in parentheses are evaluated first. For example, to select all employees in departments E11 and E21 who have education levels greater than 12, you can specify:

```sql
...
  WHERE EDLEVEL > 12 AND
     (WORKDEPT = 'E11' OR WORKDEPT = 'E21')
```

The parentheses determine the meaning of the search condition. In this example, you want all rows that have a:

- WORKDEPT value of E11 or E21, and
- EDLEVEL value greater than 12

If you did not use parentheses:

```sql
...
  WHERE EDLEVEL > 12 AND WORKDEPT = 'E11'
    OR WORKDEPT = 'E21'
```

Your result is different. The selected rows are rows that have:

- WORKDEPT = E11 and EDLEVEL > 12, or
- WORKDEPT = E21, regardless of the EDLEVEL value

If you are combining multiple equal comparisons, you can write the predicate with the ANDs as shown in the following example:

```sql
...
  WHERE WORKDEPT = 'E11' AND EDLEVEL = 12 AND JOB = 'CLERK'
```

You can also compare two lists, for example:

```sql
...
  WHERE (WORKDEPT, EDLEVEL, JOB) = ('E11', 12, 'CLERK')
```

When two lists are used, the first item in the first list is compared to the first item in the second list, and so on through both lists. Thus, each list must contain the same number of entries. Using lists is identical to writing the query with AND. Lists can only be used with the equal and not equal comparison operators.

### Joining data from more than one table

Sometimes the information you want to see is not in a single table. To form a row of the result table, you might want to retrieve some column values from one table and some column values from another table. You can retrieve and join column values from two or more tables into a single row.

Several different types of joins are supported: inner join, left outer join, right outer join, left exception join, right exception join, and cross join.

#### Usage notes on join operations

When you join two or more tables, consider the following items:

- If there are common column names, you must qualify each common name with the name of the table (or a correlation name). Column names that are unique do not need to be qualified. However, the USING clause can be used in a join to allow you to identify columns that exist in both tables without specifying table names.
- If you do not list the column names you want, but instead use SELECT *, SQL returns rows that consist of all the columns of the first table, followed by all the columns of the second table, and so on.
- You must be authorized to select rows from each table or view specified in the FROM clause.
- The sort sequence is applied to all character, or UCS-2 or UTF-16 graphic columns being joined.

**Inner join**\
An inner join returns only the rows from each table that have matching values in the join columns. Any rows that do not have a match between the tables do not appear in the result table.

**Left outer join**\
A left outer join returns all the rows that an inner join returns plus one row for each of the other rows in the first table that do not have a match in the second table.

**Right outer join**\
A right outer join returns all the rows that an inner join returns plus one row for each of the other rows in the second table that do not have a match in the first table. It is the same as a left outer join with the tables specified in the opposite order.

**Exception join**\
A left exception join returns only the rows from the first table that do not have a match in the second table.

**Cross join**\
A cross join, also known as a Cartesian Product join, returns a result table where each row from the first table is combined with each row from the second table.

**Full outer join**\
Like the left and right outer joins, a full outer join returns matching rows from both tables. However, a full outer join also returns nonmatching rows from both tables.

**Multiple join types in one statement**\
Sometimes you need to join more than two tables to produce the result that you want.
