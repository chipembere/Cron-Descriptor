import unittest
import datetime
from cron_reader import to_datetime

class TestSum(unittest.TestCase):

    def test_to_datetime(self):
        self.assertEqual(type(to_datetime("10:30")), datetime.time, "Should datetime 'time' object")

if __name__ == '__main__':
    unittest.main()