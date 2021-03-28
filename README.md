[![Package Version](https://github.com/DhruvBisla/plably/workflows/Tests/badge.svg)](https://github.com/DhruvBisla/plably/actions/)
[![Package Version](https://img.shields.io/pypi/v/plably?color=success&label=pypi%20package&logo=PyPi
)](https://pypi.org/project/plably/)

# Plably

## Background

### Motivation
I use plably to generate the graphs for my lab reports. It incorporates some extra functionality I could not find in other software, including that of graphing uncertainty.

### Plably??
Alright, I could've been a bit more creative. "Plably" is the combination of the two words ["plotly"](https://github.com/plotly/plotly.py) and "lab," the python library used to generate the graphs and the purpose of the tool, respectively.

## Installation

```shell
pip install plably
```

Plably may be installed with pip using the command given above.

## Usage

```shell
plably <title> <data> <output>
```

Where title is the title, in the form "Dependent Variable vs. Independent Variable," data is the path to the input csv file, and output is the path to write the generated graph to.
