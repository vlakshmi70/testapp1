import unittest
from selenium import webdriver

class NewVisitorTests(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_check_todo_list_start(self):
        self.browser.get("http://localhost:8000")
        self.assertIn("To-Do", self.browser.title())
        self.fail("Finish the test")

if __name__ == "__main__":
    unittest.main()
