import unittest

from dictview.viewer import view

class TestViewer(unittest.TestCase):
    
    def test_nested_dict(self):
        d = {
            "A": {"a": 1,},
            "B": {"b": {"be": 1, "bee": 2,}},
            "C": 1
        }
        target = [
            "A",
            "+-a <int>",
            "B",
            "+-b",
            "| +-be <int>",
            "| +-bee <int>",
            "C <int>"
        ]
        result = view(d, length=2, return_obj=True)
        self.assertEqual(result, target)

    def test_empty_dict(self):
        d = {}
        target = []
        result = view(d, return_obj=True)
        self.assertEqual(result, target)

if __name__ == "__main__":
    unittest.main()