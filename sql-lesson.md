# intro

## review
- [linux commmands](linux-lesson.md)

## learning objectives

- learn SQL basics
    - databases
    - queries
- basic SQL injection
    - most basic example
        - string escaping
        - logic
        - comments 
- `sqlmap`
    - automated SQL exploitation tool

## SQL basics - what is SQL
- structured query language
- used for databases
    - databases are the 'back end' of web, phone applications
    - database stores user account info: user id, username, password, other info
- impractical to manually inspect millions of records; need some way to quickly
  grab info
- information is retrieved from database with *queries*. this is like asking the database questions:
        - who is the user with user id 1?
        - how many users interacted with the video with video id
          b1946ac92492d2347c6235b4d2611184?
```mermaid
classDiagram
    Database <|-- users
    Database <|-- content
    class users{
      userid
      username
      firstName
      lastName
      emailAddress
    }
    class content{
      contentid
      contentAuthor
      authorid
      dateCreated
    }
```
## hands on practice 1 - sql familiarization (~15 minutes)

follow [this link](https://www.sqlcourse.com/beginner-course/selecting-data) to
get some hands-on practice with SQL queries.  Take about fifteen minutes to
read this page, and then attempt the questions at the end.


## SQL query structure

```sql
sql(database)> SELECT <columns> FROM <table> WHERE <condition>;
```

- `sql(database)>` : this is the prompt.  we are currently working in the
  database named `database`
- `SELECT <columns>` : select the information we're interested from each
  listed column
- `FROM <table>` : the table from the database containing the data we're
  interested in
- `WHERE <condition>` : refinement - see below

### `WHERE <condition>`

- queries may return lots of information that we're not necessarily interested
  in
- use `WHERE` to further refine information returned
- `<condition>` is an expression which evaluates to either *true* or *false*
  (boolean)


## putting it together - basic SQL injection
- "injection": altering user input to get the target machine to do something
  other than the intended behavior

### basic SQL query
```sql
sql(dvwa)> SELECT first_name, last_name FROM users WHERE user_id = '$id';
```
- `$id` is user input - is this injectible?

### basic injection example
- hinges on the `WHERE user_id = '$id'` part of the query
- `'$id`' is a variable that will contain user-supplied information.
- user can put in 'bad data' that alters the SQL query


```sql
#original
sql(dvwa)> SELECT first_name, last_name FROM users WHERE user_id = '$id';

#injected
sql(dvwa)> SELECT first_name, last_name FROM users WHERE user_id = '$id' or
'1=1'-- -;
```

- `or '1=1'-- -`: user-supplied 'bad' data
    - `or '1=1'`a conditional which always evaluates to `true`
    - `-- -`: an SQL comment - ignore everything that follows

- injection: user-supplied bad data
    - `' or '1=1'-- -`

### boolean expressions - truth table

```
| p | q | p AND q | p OR q | p AND p |
|:-:|:-:|:-------:|:------:|:-------:|
| f | f |    f    |    f   |    f    |
| f | t |    f    |    t   |    f    |
| t | f |    f    |    t   |    t    |
| t | t |    t    |    t   |    t    |
```
