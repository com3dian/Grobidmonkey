import unittest
import Levenshtein
from grobidmonkey import reader
from anytree import Node, RenderTree

def renderTreesIdentical(tree1, tree2):
    """
    Check if two render trees are identical.

    Args:
        tree1: RenderTree object 1
        tree2: RenderTree object 2

    Returns:
        bool: True if the trees are identical, False otherwise
    """
    for node1, node2 in zip(tree1,tree2):
        if node1.node.name != node2.node.name:
            return False
    return True

class TestMethods(unittest.TestCase):

    def __init__(self, methodName: str = "runTest") -> None:
        super().__init__(methodName)
        self.testDoc = 'test_resources/paper_process-3.pdf.tei.xml'
        self.lorem = '''
        Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Ut purus elit, 
        vestibulum ut, placerat ac, adipiscing vitae, felis. Curabitur dictum gravida 
        mauris. Nam arcu libero, nonummy eget, consectetuer id, vulputate a, magna. 
        Donec vehicula augue eu neque. Pellentesque habitant morbi tristique senectus 
        et netus et malesuada fames ac turpis egestas. Mauris ut leo. Cras viverra metus 
        rhoncus sem. Nulla et lectus vestibulum urna fringilla ultrices. Phasellus eu 
        tellus sit amet tortor gravida placerat. Integer sapien est, iaculis in, pretium 
        quis, viverra ac, nunc. Praesent eget sem vel leo ultrices bibendum. Aenean 
        faucibus. Morbi dolor nulla, malesuada eu, pulvinar at, mollis ac, nulla. 
        Curabitur auctor semper nulla. Donec varius orci eget risus. Duis nibh mi, congue 
        eu, accumsan eleifend, sagittis quis, diam. Duis eget orci sit amet orci dignissim 
        rutrum.
        '''
        self.lorem = self.lorem.replace('\n        ', '')
        self.outlineRoot = Node("Article")
        intro = Node("1 Introduction", parent=self.outlineRoot)
        subSec = Node("1.1 Subsection 1.1", parent=intro)
        subSubSec = Node("1.1.1 Subsubsection 1.1.1", parent=subSec)
        conclusion = Node("2 Conclusion", parent=self.outlineRoot)
        self.outline = RenderTree(self.outlineRoot)

    def testlxml(self):
        monkeyReader = reader.MonkeyReader('lxml')
        essay = monkeyReader.readEssay(self.testDoc)
        abstractDistance = Levenshtein.distance(self.lorem, essay['Abstract'][0])
        self.assertTrue(abstractDistance/len(self.lorem) <= 0.05)

        introDistance = Levenshtein.distance(self.lorem, essay['Introduction'][0])
        self.assertTrue(introDistance/len(self.lorem) <= 0.05)

        subsecDistance = Levenshtein.distance(self.lorem, essay['Subsection 1.1'][0])
        self.assertTrue(subsecDistance/len(self.lorem) <= 0.05)

        subsubsecDistance = Levenshtein.distance(self.lorem, essay['Subsubsection 1.1.1'][0])
        self.assertTrue(subsubsecDistance/len(self.lorem) <= 0.05)

        concDistance = Levenshtein.distance(self.lorem, essay['Conclusion'][0])
        self.assertTrue(concDistance/len(self.lorem) <= 0.05)

        self.assertTrue(renderTreesIdentical(self.outline, 
                                             monkeyReader.readOutline(self.testDoc)))



    def testx2d(self):
        monkeyReader = reader.MonkeyReader('x2d')
        essay = monkeyReader.readEssay(self.testDoc)

        abstractDistance = Levenshtein.distance(self.lorem, essay['Abstract'][0])
        self.assertTrue(abstractDistance/len(self.lorem) <= 0.05)

        introDistance = Levenshtein.distance(self.lorem, essay['Introduction'][0])
        self.assertTrue(introDistance/len(self.lorem) <= 0.05)

        subsecDistance = Levenshtein.distance(self.lorem, essay['Subsection 1.1'][0])
        self.assertTrue(subsecDistance/len(self.lorem) <= 0.05)

        subsubsecDistance = Levenshtein.distance(self.lorem, essay['Subsubsection 1.1.1'][0])
        self.assertTrue(subsubsecDistance/len(self.lorem) <= 0.05)

        concDistance = Levenshtein.distance(self.lorem, essay['Conclusion'][0])
        self.assertTrue(concDistance/len(self.lorem) <= 0.05)

        self.assertTrue(renderTreesIdentical(self.outline, 
                                             monkeyReader.readOutline(self.testDoc)))


    def testMonkey(self):
        monkeyReader = reader.MonkeyReader('monkey')
        essay = monkeyReader.readEssay(self.testDoc)

        abstractDistance = Levenshtein.distance(self.lorem, essay['Abstract'][0])
        self.assertTrue(abstractDistance/len(self.lorem) <= 0.05)

        introDistance = Levenshtein.distance(self.lorem, essay['Introduction'][0])
        self.assertTrue(introDistance/len(self.lorem) <= 0.05)

        subsecDistance = Levenshtein.distance(self.lorem, essay['Subsection 1.1'][0])
        self.assertTrue(subsecDistance/len(self.lorem) <= 0.05)

        subsubsecDistance = Levenshtein.distance(self.lorem, essay['Subsubsection 1.1.1'][0])
        self.assertTrue(subsubsecDistance/len(self.lorem) <= 0.05)

        concDistance = Levenshtein.distance(self.lorem, essay['Conclusion'][0])
        self.assertTrue(concDistance/len(self.lorem) <= 0.05)

        self.assertTrue(renderTreesIdentical(self.outline, 
                                             monkeyReader.readOutline(self.testDoc)))
    

    
if __name__ == '__main__':
    unittest.main()