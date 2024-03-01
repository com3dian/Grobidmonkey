from anytree import Node, RenderTree


def dictUnion(dict1, dict2):
    """
    Merge two dictionaries, dict1 and dict2, into a new dictionary by combining
    key-value pairs from both dictionaries. If a key exists in both
    dictionaries, the values are merged according to their types (e.g., lists
    are concatenated)

    Args:
        dict1 (dict): The first dictionary.
        dict2 (dict): The second dictionary.

    Returns:
        dict: A new dictionary containing the merged key-value pairs.

    Example:
        >>> dict1 = {'x': [1, 2], 'y': 'hello'}
        >>> dict2 = {'x': [3], 'z': 'world'}
        >>> dictUnion(dict1, dict2)
        {'x': [1, 2, 3], 'y': 'hello', 'z': 'world'}
    """
    ansDict = dict()
    if (type(dict1) is dict) and (type(dict2) is dict):
        for key in dict1.keys():
            if key in dict2.keys():
                if type(dict1[key]) is list and type(dict2[key]) is not list:
                    list1 = dict1[key]
                    list1.append(dict2[key])
                    ansDict[key] = list1

                if type(dict1[key]) is list and type(dict2[key]) is list:
                    ansDict[key] = dict1[key] + dict2[key]

            else:
                ansDict[key] = dict1[key]
        for key in dict2.keys():
            if key not in dict1.keys():
                ansDict[key] = dict2[key]
    else:
        # error message indicating non-dictionary input
        raise TypeError('Invalid input types. Inputs must be dictionaries.')

    return ansDict


class OutlineReader():
    """
    An outline reader class for generating an Anytree representation of
    document structures.

    Attributes:
        globalSectionDict (dict): A dictionary that maps section indices to
        section titles.
        globalNodeDict (dict): A dictionary that maps section indices to
        Anytree nodes.
        root (anytree.Node): The root node of the Anytree representation of
        the document tree.
    """
    def __init__(self):
        """
        Constructor for the OutlineReader class.

        Initializes the global section dictionary, global node dictionary, and
        root node.
        """
        self.globalSectionDict, self.globalNodeDict = dict(), dict()
        self.root = Node('Article')
        self.globalSectionDict[''] = 'Article'
        self.globalNodeDict[''] = self.root

    def findParentNodeIndex(self, childIndex):
        """
        Given a section index, find the parent section index.

        Args:
            childIndex (str): The index of sub-section.

        Returns:
            str: The index of parent section.
        """
        lastDotIndex = childIndex.rfind('.')
        if lastDotIndex != -1:
            return childIndex[:lastDotIndex]
        else:
            return ''

    def getTree(self, treeRoot):
        """
        Generate an Anytree representation of the document structure.

        Args:
            treeRoot (dict): The root node of the document tree.

        Returns:
            anytree.RenderTree: The Anytree representation of the document
            outline.
        """
        self.read(treeRoot)
        Iter = lambda x: x.items() if type(x) is dict else enumerate(x)
        for sectionIndex, sectionTitle in Iter(self.globalSectionDict):
            if sectionIndex == '':
                continue
            parentIndex = self.findParentNodeIndex(sectionIndex)
            parent = self.globalNodeDict[parentIndex]
            child = Node(sectionIndex + ' ' + sectionTitle, parent=parent)
            self.globalNodeDict[sectionIndex] = child
        return RenderTree(self.root)
