import unittest
import os.path
from tracker import Tracker
from sqlite_adapter import SQLiteAdapter

class EndToEndTest(unittest.TestCase):
  def test_creating_a_db_and_adding_a_habit(self):
    self.assertFalse(os.path.isfile("./db/tiny_habits_tracker"))
    tracker = Tracker()
    tracker.create_db()
    self.assertTrue(os.path.isfile("./db/tiny_habits_tracker"))
    tracker.add_habit("breathe")
    self.assertEqual(tracker.habits()[0][1], "breathe")
    os.remove("./db/tiny_habits_tracker")
    self.assertFalse(os.path.isfile("./db/tiny_habits_tracker"))

if __name__ == "__main__":
  unittest.main()
