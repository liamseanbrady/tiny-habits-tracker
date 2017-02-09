import unittest
from types import MethodType
from tracker import Tracker

class TinyHabitsTrackerTest(unittest.TestCase):
  def test_returns_true_if_database_already_exists(self):
    def stubbed_method(name):
      if name == "tiny_habits_tracker":
        return True
      else:
        return False

    fake_db = FakeDb()
    fake_db.exist = stubbed_method
    tracker = Tracker(db=fake_db)
    result = tracker.has_existing_db()

    self.assertEqual(result, True)

  def test_returns_false_if_database_does_not_already_exist(self):
    def stubbed_method(name):
      return False

    fake_db = FakeDb()
    fake_db.exist = stubbed_method
    tracker = Tracker(db=fake_db)
    result = tracker.has_existing_db()

    self.assertEqual(result, False)

  def test_creates_new_database_if_no_database_currently_exists(self):
    fake_db = FakeDb()
    def stubbed_method(name):
      fake_db.method_called = True
    fake_db.create = stubbed_method
    tracker = Tracker(db=fake_db)
    tracker.create_db()

    self.assertEqual(fake_db.method_called, True)

  def test_adding_a_new_habit(self):
    fake_db = FakeDb()
    def stubbed_method(prop, **kwargs):
      fake_db.method_called = True
      fake_db.method_params.append(kwargs.get("name"))
    fake_db.add = stubbed_method
    tracker = Tracker(db=fake_db)
    tracker.add_habit("breathe")

    self.assertEqual(fake_db.method_called, True)
    self.assertEqual(fake_db.method_params, ["breathe"])

class FakeDb:
  def __init__(self):
    self.method_called = None
    self.method_params = []

if __name__ == "__main__":
  unittest.main()
