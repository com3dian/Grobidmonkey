
[![Python](https://img.shields.io/pypi/pyversions/Grobidmonkey)](https://pypi.org/project/grobidmonkey/)
![Static Badge](https://img.shields.io/badge/package-grobidmonkey-2D9596)
[![PyPI](https://badge.fury.io/py/grobidmonkey.svg)](https://badge.fury.io/py/grobidmonkey)
[![Github Workflow Tests Status](https://github.com/com3dian/Grobidmonkey/workflows/Test/badge.svg)](https://github.com/com3dian/Grobidmonkey/workflows/Test/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/com3dian/Grobidmonkey)
[![PyPI Downloads](https://img.shields.io/pypi/dm/grobidmonkey.svg?label=Pypi%20downloads)](https://pypi.org/project/grobidmonkey/)
![Github Created At](https://img.shields.io/github/created-at/com3dian/Grobidmonkey)
![GitHub License](https://img.shields.io/github/license/com3dian/Grobidmonkey)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)


<div align="center" style="text-align: left; font-size: larger;">
  <img src="https://raw.githubusercontent.com/com3dian/Grobidmonkey/master/Document/resources/noun-chimpanzee-4933957(1).png" alt="Chimpanzee" width="200" />
  <p>
    <code>grobidmonkey</code> is a light-weight python package designed for postprocessing <a href="https://grobid.readthedocs.io/en/latest/">GROBID</a> outputs.
    It provides a reader class that converts these files into Python dictionaries, making them simple to read and work with. The grobidmonkey reader is capable of reading the entire essay as a dictionary, where each key represents section titles and the corresponding values are lists of section contents in paragraphs. Also the reader provides a method for reading the outline of essay as a tree.
  </p>
</div>


- Website: https://github.com/com3dian/Grobidmonkey

- Documentation: https://github.com/com3dian/Grobidmonkey/tree/master/Document

- Source code: https://github.com/com3dian/Grobidmonkey/tree/master/src/grobidmonkey

- Bug reports: https://github.com/com3dian/Grobidmonkey/issues

- Citing in your work: https://studenttheses.uu.nl/handle/20.500.12932/45939 or
```tex
@mastersthesis{lu2024unsupervised,
  title={Unsupervised Paper2Slides Generation},
  author={Lu, Zehao},
  year={2024}
}
```

### Installation

Currently grobidmonkey is only available in PyPI, and can be installed with
```bash
pip install grobidmonkey
```

### Quick Start

```python
from grobidmonkey import reader
monkeyReader = reader.MonkeyReader('monkey') # or 'lxml' or 'x2d'

# read paper outline
outline = monkeyReader.readOutline('/path/to/your/paper.pdf.tei.xml')

# read paper content
essay = monkeyReader.readEssay('/path/to/your/paper.pdf.tei.xml')
```
For detailed explanantion and tutorial, please check the [Document](https://github.com/com3dian/Grobidmonkey/tree/master/Document) page. 

### Contirbution

We welcome all contributions, whether they involve code, documentation, or testing, feel free to reach out to me via email at com3dian@outlook.com.

### About GROBID

GROBID means **G**ene**R**ation **O**f **BI**bliographic **D**ata.

[GROBID](https://github.com/kermitt2/grobid) is a machine learning library for extracting, parsing and re-structuring raw documents such as PDF into structured XML/TEI encoded documents with a particular focus on technical and scientific publications.

You can also try the [GROBID web app](https://kermitt2-grobid.hf.space/) with your paper.
