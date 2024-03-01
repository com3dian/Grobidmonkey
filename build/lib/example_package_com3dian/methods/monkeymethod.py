# Copyright 2023 Zehao Lu. All rights reserved.
# Monkey method for parsing.


import re
from anytree import Node, RenderTree


def formatSection(section, title=None):
    """
    Extracts and formats content from an XML section.

    Args:
        section (str): The XML section to be processed.
        title (str, optional): An optional title to be used instead of
        extracting one from the section.

    Returns:
        tuple: A tuple containing the extracted title (if available) and a
        list of cleaned content strings.

    Example:
        >>> section = '<head>Title</head><p>Content 1</p><p>Content 2</p>\n'
        >>> title, content = formatSection(section)
        >>> print(title)
        'Title'
        >>> print(content)
        ['Content 1', 'Content 2']
    """
    section = section[:-1]
    contentList = re.split('</p>|<p>', section)
    pattern = r">([^<]+)</head>"
    matches = re.search(pattern, contentList[0])
    if matches:
        title = matches.group(1)

    content = []
    for index in range(1, len(contentList)):
        text = contentList[index]
        pattern = r"<.*?>"
        if not len(cleanedText := re.sub(pattern, "", text)):
            continue

        content.append(cleanedText)

    return title, content


def readEssay(fileLines):
    """
    Extracts structured sections from a list of lines in a document.

    This function processes a list of text lines representing a document,
    searching for specific section headers and their associated content.
    It recognizes two types of sections: 'Abstract' and custom sections
    defined within the document.

    Args:
        fileLines (list): A list of strings, each representing a line of text
        in the document.

    Returns:
        dict: A dictionary containing extracted sections as key-value pairs,
        where the keys are section names (e.g., 'Abstract', custom section
        names) and the values are list of the corresponding section contents.

    Example:
        >>> # Given a list of lines in a document
        >>> Lines = ['<div xmlns="http://www.tei-c.org/ns/1.0">',
        ...          '<head n="1">Introduction</head>',
        ...          'This is the introduction section.',
        ...          '<head n="2">Conclusion</head>',
        ...          'This is the conclusion section.']
        >>> Article = readEssay(fileLines)
        >>> print(Article)
        {
            'Introduction': ['This is the introduction section.'],
            'Conclusion': ['This is the conclusion section.']
        }
    """
    ans = {}
    abstractTag = '<abstract>'
    GROBIDTag = '<div xmlns="http://www.tei-c.org/ns/1.0">'
    newSectionTag = GROBIDTag + '<head n="'

    for lineIndex in range(len(fileLines)):
        line = fileLines[lineIndex]
        if abstractTag in line:
            sectionName, content = formatSection(fileLines[lineIndex+1], 'Abstract')
            ans[sectionName] = content
            continue

        start = line.find(newSectionTag)
        if start != -1:
            sectionName, content = formatSection(line)

            ans[sectionName] = content
    return ans


def getOutline(fileLines):
    """
    Parse an outline structure from a list of lines and return a tree
    structure.

    Args:
        fileLines (list): A list of strings, each representing a line of text
        in the document.

    Returns:
        anytree.RenderTree: The Anytree representation of the document
        outline.
    """
    outlineDict, nodeDict = {}, {}
    GROBIDTag = '<div xmlns="http://www.tei-c.org/ns/1.0">'
    newSectionTag = GROBIDTag + '<head n="'
    for line in fileLines:
        if line.find(newSectionTag) != -1:
            pattern = r'<div xmlns="http://www.tei-c.org/ns/1.0"><head n="(.*?)">'
            match = re.search(pattern, line)
            sectionName, _ = formatSection(line)
            sectionIndex = match.group(1)
            outlineDict[sectionIndex] = sectionName

    root = Node('Article')
    for sectionIndex, sectionTitle in outlineDict.items():
        lastDotPosition = sectionIndex.rfind('.')
        if lastDotPosition != -1:
            # get the index before the last '.'
            if (parentIndex := sectionIndex[:lastDotPosition]) in nodeDict.keys():
                parent = nodeDict[parentIndex]
                child = Node(sectionIndex + ' ' + sectionTitle, parent=parent)
                nodeDict[sectionIndex] = child
        else:
            child = Node(sectionIndex + ' ' + sectionTitle, parent=root)
            nodeDict[sectionIndex] = child

    return RenderTree(root)
