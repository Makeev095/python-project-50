import argparse
from gendiff.generate_diff import generate_diff
import json

filepath1 = json.load(open('/Users/makey/Desktop/Проекты/python-project-50/gendiff/file1.json'))
filepath2 = json.load(open('/Users/makey/Desktop/Проекты/python-project-50/gendiff/file2.json'))


def main():
    parser = argparse.ArgumentParser(description="Compares two configuration files and shows a difference.")
    parser.add_argument("-f", "--format", help="set format of output")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.parse_args()
    generate_diff(filepath1, filepath2)


if __name__ == '__main__':
    main()