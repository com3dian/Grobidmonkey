from grobidmonkey.methods import x2dmethod, lxmlmethod, monkeymethod
import xmltodict

from lxml import etree

class MonkeyReader():
    def __init__(self, method):
        self.method = method
        self.methodSet = set(['lxml', 'x2d', 'monkey'])
        if method not in self.methodSet:
            raise ValueError('Method has to be one of \'lxml\', \'x2d\', or \'monkey\'')

    def readEssay(self, file):
        if self.method == 'lxml':
            tree = etree.parse(file)
            root = tree.getroot()
            essay, _ = lxmlmethod.readEssay(root)
        
        if self.method == 'x2d':
            with open(file, 'rb') as xml_file:
                essayDict = xmltodict.parse(xml_file)
            essay, _ = x2dmethod.readEssay(essayDict)

        if self.method == 'monkey':
            with open(file, 'r') as xml_file:
                lines = xml_file.readlines()

            essay = monkeymethod.readEssay(lines)

        self.essay = {key: value for key, value in essay.items() if key is not None}
        return self.essay
    
    def readOutline(self, file):
        if self.method == 'lxml':
            outlineReader = lxmlmethod.lxmlOutlineReader()
            tree = etree.parse(file)
            outlineReader.read(tree.getroot())
            outlineTree = outlineReader.getTree(tree.getroot())
        
        if self.method == 'x2d':
            outlineReader = x2dmethod.x2dOutlineReader()
            with open(file, 'rb') as xml_file:
                essayDict = xmltodict.parse(xml_file)
            outlineTree = outlineReader.getTree(essayDict)

        if self.method == 'monkey':
            with open(file, 'r') as xml_file:
                lines = xml_file.readlines()

            outlineTree = monkeymethod.getOutline(lines)


        for pre, fill, node in outlineTree:
            print("%s%s" % (pre, node.name))
        
        return outlineTree





