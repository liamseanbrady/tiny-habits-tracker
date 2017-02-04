class Tracker:
  def __init__(self, **kwargs):
    self.db = kwargs["db"]

  def has_existing_db(self):
    return self.db.exist("tiny_habits_tracker")

  def create_db(self):
    self.db.create("tiny_habits_tracker")

  def add_habit(self, name):
    self.db.add("habit", name)
