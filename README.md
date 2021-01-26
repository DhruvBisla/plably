[![Package Version](https://github.com/DhruvBisla/plably/workflows/Tests/badge.svg)](https://github.com/DhruvBisla/plably/actions/)
[![Package Version](https://img.shields.io/pypi/v/plably?color=success&label=pypi%20package&logo=PyPi
)](https://pypi.org/project/plably/)

# Plably

## Background

### Motivation
Plably is the tool I creatd to make graphs for my lab reports. It includes some extra functionality I could not find including graphing uncertainty.

### What type of a name is Plably?
Admittedly, it is rather poorly named. 'Plably' is the combination of the two words 'plotly' and 'lab', being the tool I use for lab reports which uses plotly.

## Installation

```shell
pipx install plably
```

For the best command line experience, plably may be installed via pipx. If you do not have pipx installed, you may find installation instructions [here](https://pipxproject.github.io/pipx/installation/).

## Usage

```shell
plably <title> <data> <output>
```

Where title is the title, in the form 'Dependent Variable vs. Independent Variable,' data is the path to the input csv file, and output is the path to write the generated graph to.