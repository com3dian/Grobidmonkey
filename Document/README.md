### Grobidmonkey Reader

#### Overview

The `MonkeyReader` class serves as the primary interface for end-users interacting with the grobidmonkey library, and therefore, we provide a detailed documentation for the MonkeyReader class.

The purpose of the MonkeyReader class is to extract essays and outlines from XML files using different methods. It supports parsing TEI-XML files through three methods: `lxml`, `x2d`, and `monkey`. Depending on the chosen method, the class uses corresponding submodules to extract either the essay content or the outline structure from the XML input.

#### Class Structure

##### Attributes

- method: A string indicating the method chosen for parsing XML files.
- methodSet: A set containing valid parsing methods (lxml, x2d, monkey).
- essay: A dictionary containing the extracted essay content.

##### Methods

- `readEssay(self, file: str) -> dict`:
  Reads the essay content from the given XML file based on the specified method.

  Args: 
    - `file` (str): The path to the TEI-XML file.

  Returns: A dictionary where the keys are section titles, and the values are lists of strings. Each string represents a paragraph marked with `<p>...</p>` in the input TEI-XML file.

- `readOutline(self, file: str, showOutline: bool = False) -> anytree.RenderTree`:
  Parses the TEI-XML file containing an outline and extracts its structure.
  
  Args:
    - `file` (str): The path to the TEI-XML file.

    - `showOutline` (bool): A flag indicating whether to print the outline structure. Defaults to False.

  Returns: A [`anytree.RenderTree`](https://anytree.readthedocs.io/en/stable/api/anytree.render.html#anytree.render.RenderTree) representation of the document outline.
  