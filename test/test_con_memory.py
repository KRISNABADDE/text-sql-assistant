import unittest

from app.services.con_memory import MemoryService


class TestMemoryService(unittest.TestCase):

    def setUp(self) -> None:
        self.memory = MemoryService()

    def test_add_query(self) -> None:
        self.memory.add_query("Show me employees who joined after 2020",
                              "SELECT * FROM employees WHERE joining_date > '2020-01-01';")
        self.assertEqual(len(self.memory.history), 1)
        self.assertEqual(self.memory.history[0], {"user_query": "Show me employees who joined after 2020",
                                                  "sql_query": "SELECT * FROM employees WHERE joining_date > '2020-01-01';"})

    def test_get_recent_queries(self) -> None:
        self.memory.add_query("What is the average salary in the IT department?",
                              "SELECT AVG(salary) FROM employees WHERE department = 'IT';")

        recent = self.memory.get_recent_queries(1)
        expected = "User: What is the average salary in the IT department? -> SQL: SELECT AVG(salary) FROM employees WHERE department = 'IT';"
        self.assertEqual(recent, expected)


if __name__ == "__main__":
    unittest.main()
