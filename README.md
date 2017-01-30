This little utility app is designed to help track your progress through BJ Fogg's [Tiny Habits]((http://tinyhabits.com/) method of developing new habits.

To run this program locally, I am using

- pysqlite 2.6.0
- SQLite database library 3.8.10.2

You can find out which version of pysqlite you have locally by doing the following in the Python interactive interpreter:
```
>>> import sqlite3
>>> sqlite3.version
```

You can find out which version of the SQLite database library you have locally by doing the following in the Python interactive interpreter:
```
>>> import sqlite3
>>> sqlite3.sqlite3_version
```

Note: I learned how to interact with SQLite3 from Python by using [this](http://zetcode.com/db/sqlitepythontutorial/) fantastic resource. 
