
[![Python](https://img.shields.io/pypi/pyversions/Grobidmonkey)](https://pypi.org/project/grobidmonkey/)
![Static Badge](https://img.shields.io/badge/package-grobidmonkey-2D9596)
[![PyPI](https://badge.fury.io/py/grobidmonkey.svg)](https://badge.fury.io/py/grobidmonkey)
[![Github Workflow Tests Status](https://github.com/com3dian/Grobidmonkey/workflows/Test/badge.svg)](https://github.com/com3dian/Grobidmonkey/workflows/Test/badge.svg)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/com3dian/Grobidmonkey)
[![PyPI Downloads](https://img.shields.io/pypi/dm/grobidmonkey.svg?label=Pypi%20downloads)](https://pypi.org/project/grobidmonkey/)
![Github Created At](https://img.shields.io/github/created-at/com3dian/Grobidmonkey)
![GitHub License](https://img.shields.io/github/license/com3dian/Grobidmonkey)

The grobidmonkey package is an open-source package designed for postprocessing [GROBID](https://grobid.readthedocs.io/en/latest/) outputs.

- Website: https://github.com/com3dian/Grobidmonkey

- Documentation: https://github.com/com3dian/Grobidmonkey/Document

- Source code: https://github.com/com3dian/Grobidmonkey/src

- Bug reports: https://github.com/com3dian/Grobidmonkey/issues

- Citing in your work: https://studenttheses.uu.nl/handle/20.500.12932/45939 or
```tex
@mastersthesis{lu2024unsupervised,
  title={Unsupervised Paper2Slides Generation},
  author={Lu, Zehao},
  year={2024}
}
```

`grobidmonkey` is built to handle TEI XML files generated by GROBID. It provides a reader class that converts these files into Python dictionaries, making them simple to read and work with. The grobidmonkey reader is capable of reading the entire essay as a dictionary, where each key represents section titles and the corresponding values are lists of section contents in paragraphs. Also the reader provides a method for reading the outline of essay as a tree.

### Installation

Currently grobidmonkey is only available in PyPI, and can be installed with
```shell
pip install grobidmonkey
```

### Quick Start

```python
from grobidmonkey import reader
monkeyReader = reader.MonkeyReader('monkey') # or 'lxml' or 'x2d'

# read paper outline
outline = monkeyReader.readOutline('path/to/your/paper.pdf.tei.xml')

# read paper content
essay = monkeyReader.readEssay('/home/com3dian/Downloads/2308.13067.pdf.tei.xml')
```
For detailed explanantion and tutorial, please check the [Document](https://github.com/com3dian/Grobidmonkey/Document) page. 

### Contirbution

We welcome all contributions, whether they involve code, documentation, or testing, feel free to reach out to me via email at com3dian@outlook.com


### Icon

Gorbidmonkey's icon is a walking monkey.

```
                  $$                                                                   
           $$$$$$$$$$$$$$$$$$                              $$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$                    $$$$$$$$$$                       
    $$$$$$$$                $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$             
   $$$$$$                          $$$$$$$$$$$$$$$$$$$$$$$$$$$           
  $$$$$$                                   $$$$$$$$$$$$                             
 $$$$$$                                                              
 $$$$$$                                                                   
 $$$$$$                                                                             
 $$$$$$                                                                    GROBIDMONKEY
 $$$$$$$                           $$$$$$$$$$$$$$$                     $$$$$$$$$$$$$$$$$$$$
 $$$$$$$                   $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$          $$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$   $$$$$$$$     $$
    $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  $$$$$$      $$  $
      $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$          $$
          $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$     $$$$
              $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$    $$$$$$$$$$$$$$$
                 $$$$$$$$$$$$$$$$    $$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$         $$$$$$$
                  $$$$$$$$$$$$$$$       $$$$$$$$$  $$$$$$$$$$$$$$$$$  
            $$$$$  $$$$$$$$$$$$$$                 $$$$$$$$$$$$$$$$   $$$$
        $$$$$$$$$$$  $$$$$$$$$$$$               $$$$$$$$$$$$$$$$  $$$$$$$
    $$$$$$$$$$$$$$$$ $$$$$$$$$$$$             $$$$$$$$$$$$$$   $$$$$$$$$$
 $$$$$$$$$$$$$$$$$  $$$$$$$$$$$             $$$$$$$$$$$$$    $$$$$$$$$$$
$$$$$$$$$$$        $$$$$$$$$$              $$$$$$$$$$        $$$$$$$$$$$
$$$$$$$            $$$$$$$$$               $$$$$$$$            $$$$$$$$$$
 $$$$$            $$$$$$$$$                $$$$$$$              $$$$$$$$$
 $$$$$$          $$$$$$$$                 $$$$$$$$                $$$$$$$$$
 $$$$$$          $$$$$$$$                $$$$$$$$                 $$$$$$$$$
 $$$$$$          $$$$$$$$              $$$$$$$$$                    $$$$$$$$
 $$$$$           $$$$$$$$$            $$$$$$$$$                       $$$$$$$$
                  $$$$$$$$$$        $$$$$$$$$                           $$$$$$$$
                    $$$$$$$$$$$$$$$$$$$$$$                                $$$$$$$$$$$$$$$$$$$
                         $$$$$$$$$$$                                           $$$$$$$$$$$$$$
```
