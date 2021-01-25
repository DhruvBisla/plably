import argparse
import sys
from os import path
from . import plot

def main():
    parser = argparse.ArgumentParser(prog='plably', description='Create a graph')
    parser.add_argument("name", help="The name of the graph")
    parser.add_argument("data", help="Path to the data source")
    parser.add_argument("out", help="Path to the generated plably graph")
    args = parser.parse_args()

    if not path.exists(args.data):
        print("Path to data does not exist.")
        sys.exit()
    else:
        print("Creating graph ...")
        graph = plot.Plot(args.name, args.data, args.out)
        graph.createGraph()

if __name__ == "__main__":
    main()