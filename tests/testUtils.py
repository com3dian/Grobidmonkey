import unittest
from anytree import Node, RenderTree
from grobidmonkey.utils import dictUnion, OutlineReader


class TestDictUnion(unittest.TestCase):
    def testSimple(self):
        dict1 = {'x': [1, 2], 'y': 'hello'}
        dict2 = {'x': [3], 'z': 'world'}
        result = dictUnion(dict1, dict2)
        expected = {'x': [1, 2, 3], 'y': 'hello', 'z': 'world'}
        self.assertEqual(result, expected)

    def testEmpty(self):
        dict1 = {}
        dict2 = {}
        result = dictUnion(dict1, dict2)
        expected = {}
        self.assertEqual(result, expected)

    def testNonListValue(self):
        dict1 = {'x': [1, 2], 'y': 'hello'}
        dict2 = {'x': [3], 'y': 'world'}
        result = dictUnion(dict1, dict2)
        expected = {'x': [1, 2, 3]}
        self.assertEqual(result, expected)

    def testListValue(self):
        dict1 = {'x': [1, 2], 'y': ['hello']}
        dict2 = {'x': [3], 'y': 'world'}
        result = dictUnion(dict1, dict2)
        expected = {'x': [1, 2, 3], 'y': ['hello', 'world']}
        self.assertEqual(result, expected)

    def test_invalid_input(self):
        dict1 = {'x': [1, 2], 'y': 'hello'}
        dict2 = 'not a dictionary'
        with self.assertRaises(TypeError):
            result = dictUnion(dict1, dict2)


class TestOutlineReader(unittest.TestCase, OutlineReader):
    def testFoundParent(self):
        # test case 1
        childIndex = '1.2.3'
        result = self.findParentNodeIndex(childIndex)
        expected = '1.2'
        self.assertEqual(result, expected)

        # test case 2
        childIndex = '123'
        result = self.findParentNodeIndex(childIndex)
        expected = ''
        self.assertEqual(result, expected)

    def read(self, root):
        # place holder
        pass

if __name__ == '__main__':
    unittest.main()