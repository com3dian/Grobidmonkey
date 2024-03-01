# Copyright 2023 Zehao Lu. All rights reserved.
# Parsing method based on the lxml package.

from grobidmonkey.utils import dictUnion, OutlineReader


def readEssay(root, currentKey=None):
    """
    Recursively parse GROBID output data and extract relevant information.

    Args:
        data (dict): The GROBID output data to be parsed.
        currentKey (str): The current key of current sub-dict (optional).

    Returns:
        dict: A dictionary containing the extracted information organized by
        sections.
        str: Key to the current sub-dict.
    """
    ans = dict()
    keywordList = ['head', '#text', 'p']
    specialwordList = ['date', 'abstract', 'ref']
    stopwordList = ['idno', 'listBibl', 'note', 'figDesc', 'figure']

    grobidAPI = '{http://www.tei-c.org/ns/1.0}'
    keywordList = [grobidAPI + word for word in keywordList]
    specialwordList = [grobidAPI + word for word in specialwordList]
    stopwordList = [grobidAPI + word for word in stopwordList]

    Isleaf = lambda x: len(x) == 0
    sectionName = currentKey

    for child in root:
        childName = child.tag
        childText = child.text

        if childName in stopwordList:
            continue

        if childName == (grobidAPI + 'abstract'):
            ans[(sectionName := 'Abstract')] = []
        if childName == (grobidAPI + 'ref'):
            if sectionName in ans.keys():
                ans[sectionName][-1] += childText
            else:
                ans[sectionName] = [childText]

        if childName in keywordList:
            if childName == (grobidAPI + 'head'):
                sectionName = child.text
                ans[sectionName] = []
            else:
                ans = dictUnion(ans, {sectionName: [childText]})

        if Isleaf(child):
            pass
        else:
            recDict, sectionName = readEssay(child, sectionName)
            ans, sectionName = dictUnion(ans, recDict), sectionName
    return ans, sectionName


class lxmlOutlineReader(OutlineReader):
    """
    A specialized OutlineReader for reading TEI XML data using lxml.

    This class extends the base OutlineReader to read and construct an outline
    (tree structure) from TEI XML data using the lxml library.

    Attributes:
        TEILink (str): The XML namespace link for TEI elements.

    """
    def __init__(self):
        """
        In addition to the attributes inherited from the base class, this
        class initializes the TEILink attribute.
        """
        super().__init__()
        self.TEILink = '{http://www.tei-c.org/ns/1.0}'

    def read(self, root):
        """
        Read and parse TEI XML data to populate the outline.

        Args:
            root (lxml.Element): The root element of the TEI XML document.

        Returns:
            None
        """
        Isleaf = lambda x: len(x) == 0
        for child in root:
            childName = child.tag
            if childName == (self.TEILink + 'head'):
                sectionIndex = child.get('n')
                if sectionIndex is None:
                    continue
                sectionName = child.text
                self.globalSectionDict[sectionIndex] = sectionName
            if Isleaf(child):
                continue
            else:
                self.read(child)

        return None