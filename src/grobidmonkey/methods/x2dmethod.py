# Copyright 2023 Zehao Lu. All rights reserved.
# Parsing method based on the xmltodict package.


import copy
from grobidmonkey.utils import dictUnion, OutlineReader


def readEssay(data, currentKey=None):
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

    stopwordList = ['figure', 'idno', 'listBibl', 'note']
    keywordList = ['head', '#text', 'p']
    ans = dict()
    Iter = lambda x: x.items() if type(x) is dict else enumerate(x)
    IsInWordList = lambda x, stopwordList: (x in stopwordList) or (type(x) is int)

    sectionName = currentKey

    for key, value in Iter(data):
        updatedValue = copy.deepcopy(value)
        if key == 'abstract':
            sectionName = 'Abstract'
            ans[sectionName] = []
        if key == 'ref':
            if type(value) is dict:
                if '@type' in value.keys():
                    if value['@type'] == 'figure':
                        ans = dictUnion(ans, {sectionName: ['figure ' + value['#text']]})
            continue
        if key == 'head':
            if type((sectionName := value)) is not str:
                sectionNameList = []

                if '#text' in value.keys():
                    updatedValue.pop('#text')
                    if value['#text'] is not None:
                        sectionNameList.append(value['#text'])
                sectionName = ' '.join(sectionNameList)
        if key in stopwordList:
            continue
        if value is None:
            continue
        if type(value) is str:
            if IsInWordList(key, keywordList) and sectionName is not None:
                ansCopy = copy.deepcopy(ans)
                ans = dictUnion(ansCopy, {sectionName: [value]})
            continue

        ansCopy = copy.deepcopy(ans)
        recDict, sectionName = readEssay(updatedValue, sectionName)
        ans = dictUnion(ansCopy, recDict)

    return ans, sectionName


class x2dOutlineReader(OutlineReader):
    """
    A specialized OutlineReader for reading TEI XML data using lxml.

    This class extends the base OutlineReader to read and construct an outline
    (tree structure) from TEI XML data using the x2d library.
    """
    def __init__(self):
        super().__init__()

    def read(self, article):
        """
        Read and parse TEI XML data to populate the outline.

        Args:
            article (dict): The dictionary of the TEI XML document.

        Returns:
            None
        """
        Iter = lambda x: x.items() if type(x) is dict else enumerate(x)
        for key, value in Iter(article):
            if (type(value) is not dict) and (type(value) is not list):
                continue
            if key == 'head':
                sectionIndex = value['@n']
                sectionTitle = value['#text']
                self.globalSectionDict[sectionIndex] = sectionTitle
            self.read(value)
        return None