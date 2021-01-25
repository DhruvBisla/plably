from setuptools import setup, find_packages
import re
import os

def get_version(package):
    with open(os.path.join(package, "__init__.py")) as f:
        return re.search("__version__ = ['\"]([^'\"]+)['\"]", f.read()).group(1)

def get_long_description():
    with open("README.md", encoding="utf8") as f:
        return f.read()

setup(
    name="plably",
    version=get_version("plably"),
    url="https://github.com/DhruvBisla/plably",
    license="MIT",
    author="Dhruv Bisla",
    author_email="bisladhruv@gmail.com",
    description="A simple plotly utility to generate graphs for my lab reports.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    keywords=['plotly', 'graphs', 'utility', 'lab-report'],
    entry_points={"console_scripts": ["plably=plably.main:main"]},
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    requires = ['plotly','kaleido'],
    install_requires=['plotly','kaleido'],
    zip_safe=False,
)
