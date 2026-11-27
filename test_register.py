import unittest
from register import check, FIELDS

class RegisterTests(unittest.TestCase):
    def test_empty_verified_row(self):
        row = dict.fromkeys(FIELDS, "")
        row.update(id="x", status="verified")
        self.assertTrue(check([row]))
    def test_pending(self):
        row = dict.fromkeys(FIELDS, "")
        row.update(id="x", status="pending")
        self.assertEqual(check([row]), [])
    def test_duplicate(self):
        row = dict.fromkeys(FIELDS, "")
        row.update(id="x", status="pending")
        self.assertTrue(check([row, row]))
