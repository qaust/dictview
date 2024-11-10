from collections import namedtuple
import unittest

from dictview.viewer import view
from dictview.seeker import seek

class TestSeeker(unittest.TestCase):

    d = {
        "A": {"a": 1,},
        "B": {"b": {"be": 1, "bee": 2, "beee": {"hello": 3},}, 'bb': "woah",},
        "C": 1,
        "D": {"beee": "hi"}
    }
    TestItem = namedtuple("TestItem", ["target", "value", "path"])
    expected = [
        TestItem(target=["bb"], value="woah", path=["B", "bb"]),
        TestItem(target=["a"], value=1, path=["A", "a"]),
        TestItem(target=["beee"], value=None, path=None),
        TestItem(target=["b", "beee"], value={"hello": 3}, path=["B", "b", "beee"]),
        # TestItem(target=("bb"), value="woah", path=["B", "bb"]),
    ]

    def test_seeker_dfs(self):
        for exp in self.expected:
            result = seek(self.d, exp.target, strategy="dfs")
            self.assertEqual(result.value, exp.value, f"\nExpected:\n{exp.value}\nActual:\n{result.value}")
            self.assertEqual(result.path, exp.path, f"\nExpected:\n{exp.path}\nActual:\n{result.path}")

    def test_seeker_bfs(self):
        for exp in self.expected:
            result = seek(self.d, exp.target, strategy="bfs")
            self.assertEqual(result.value, exp.value, f"\nExpected:\n{exp.value}\nActual:\n{result.value}")
            self.assertEqual(result.path, exp.path, f"\nExpected:\n{exp.path}\nActual:\n{result.path}")

    def test_seeker_hybrid(self):
        for exp in self.expected:
            result = seek(self.d, exp.target, strategy="hybrid")
            self.assertEqual(result.value, exp.value, f"\nExpected:\n{exp.value}\nActual:\n{result.value}")
            self.assertEqual(result.path, exp.path, f"\nExpected:\n{exp.path}\nActual:\n{result.path}")


if __name__ == "__main__":
    unittest.main()