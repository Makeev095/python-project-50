import json


def generate_diff(filepath1, filepath2):

    filepath1 = json.load(open('/Users/makey/Desktop/Проекты/python-project-50/gendiff/file1.json'))
    filepath2 = json.load(open('/Users/makey/Desktop/Проекты/python-project-50/gendiff/file2.json'))

    result = {}

    for i in filepath1:
        if (i in filepath2) and (filepath1[i] == filepath2[i]):

            result[i] = filepath1[i]

        elif (i in filepath2) and (filepath1[i] != filepath2[i]):

            result[i] = filepath1[i]
        
    print(json.dumps(result, sort_keys=True, indent=4))
    print(json.dumps(filepath1, sort_keys=True, indent=4))
    