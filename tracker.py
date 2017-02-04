class Tracker:
  def __init__(self, **kwargs):
    self.db = kwargs.get("db")
    if self.db == None:
      self.db = DB()

  def has_existing_db(self):
    return self.db.exist("tiny_habits_tracker")

  def create_db(self):
    self.db.create("tiny_habits_tracker")

  def add_habit(self, name):
    self.db.add("habits", name=name)

  def habits(self):
    return self.db.fetch_all("habits")

import sqlite3 as sqlite
import os.path

class DB:
  def __init__(self):
    self.connection = None
    self.cursor = None

  def create(self, name):
    self.connection = sqlite.connect("./db/%s" % name)
    self.cursor = self.connection.cursor()
    self.cursor.execute("create table if not exists habits (id INT, name TEXT)")
    self.connection.commit()

  def exist(self, name):
    return os.path.isfile("./db/%s" % name)

  def add(self, table, **kwargs):
    query_string = "insert into %s values (1, ?)" % table
    self.cursor.execute(query_string, (kwargs.get("name"),))
    self.connection.commit()

  def fetch_all(self, table_name):
    self.cursor.execute("select * from %s" % table_name)
    return self.cursor.fetchall()
