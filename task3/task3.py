import argparse
import json
import os


def fill_structure(structure, results):

    if isinstance(structure, list):
        for item in structure:
            fill_structure(item, results)
    elif isinstance(structure, dict):
        if 'value' in structure:
            structure['value'] = results.get(structure['id'])
        if 'values' in structure:
            fill_structure(structure['values'], results)


def main(values_file, tests_file):

    with open(values_file, 'r') as f:
        values_raw = json.load(f)['values']

    results = {}
    for vr in values_raw:
        results[vr['id']] = vr['value']

    with open(tests_file, 'r') as f:
        structure = json.load(f)

    fill_structure(structure['tests'], results)
    with open("report.json", "w") as f:
        json.dump(structure, f, indent=2)
        print(f'Results saved to {os.path.realpath(f.name)}')


parser = argparse.ArgumentParser(description='Generate diff')
parser.add_argument('values_file', help='filepath to tests results json')
parser.add_argument('tests_file', help='filepath to report structure json')
args = parser.parse_args()
main(args.values_file, args.tests_file)
