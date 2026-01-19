# tests/test_todo.py
import unittest
import tempfile
import os
from todo_app.todo import TodoManager

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        fd, self.path = tempfile.mkstemp(suffix=".json")
        os.close(fd)

    def tearDown(self):
        try:
            os.remove(self.path)
        except OSError:
            pass

    def test_add_and_list(self):
        m = TodoManager(storage_file=self.path)
        t = m.add("Comprar leche")
        all_ = m.list()
        self.assertEqual(len(all_), 1)
        self.assertEqual(all_[0].text, "Comprar leche")

    def test_complete_and_delete(self):
        m = TodoManager(storage_file=self.path)
        t = m.add("Tarea X")
        ok = m.complete(t.id)
        self.assertTrue(ok)
        self.assertTrue(m.find(t.id).done)
        d = m.delete(t.id)
        self.assertTrue(d)
        self.assertIsNone(m.find(t.id))

if __name__ == "__main__":
    unittest.main()
