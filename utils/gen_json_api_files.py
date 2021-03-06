#!/usr/bin/env python3

import json

"""
Take the data from the csv files in ../csv and turn them into json
"""


def generate_region_json():
    region_json = {}

    # Open the csv file for all regions
    with open('../csv/region.csv') as f:
        region_csv = f.readlines()

    # Discard header
    region_csv.pop(0)

    for line in region_csv:
        region, date, new_case, total_case = line.strip().split(',')

        # Create structure of region if no data in region yet
        if region not in region_json:
            region_json[region] = {}
            region_json[region]['new_case'] = {}
            region_json[region]['total_case'] = {}

        # Insert data for date
        region_json[region]['new_case'][date] = int(new_case)
        region_json[region]['total_case'][date] = int(total_case)


    with open('../json/region.json', 'w') as f:
        f.write(json.dumps(region_json, indent=4, ensure_ascii=False))


def generate_total_json():
    total_json = {}

    # Open the csv file for total
    with open('../csv/total.csv') as f:
        total_csv = f.readlines()

    # Discard header
    total_csv.pop(0)

    for line in total_csv:
        date,total_case,total_death,total_recovered, hosp, icu = line.strip().split(',')

        # Insert data for date
        total_json[date] = {}
        if total_case != '?':
            total_json[date]['total_case'] = int(total_case)
        if total_death != '?':
            total_json[date]['total_death'] = int(total_death)
        if total_recovered != '?':
            total_json[date]['total_recovered'] = int(total_recovered)
        if hosp != '?':
            total_json[date]['hospitalisations'] = int(hosp)
        if icu != '?':
            total_json[date]['intensive_care'] = int(icu)


    with open('../json/total.json', 'w') as f:
        f.write(json.dumps(total_json, indent=4, ensure_ascii=False))


def generate_montreal_json():
    montreal_json = {}

    # Open the csv file for all regions
    with open('../csv/montreal.csv') as f:
        montreal_csv = f.readlines()

    # Discard header
    montreal_csv.pop(0)

    for line in montreal_csv:
        region, date, total_case = line.strip().split(',')

        # Create structure of region if no data in region yet
        if region not in montreal_json:
            montreal_json[region] = {}
            montreal_json[region]['total_case'] = {}

        # Insert data for date
        if total_case != '?':
            montreal_json[region]['total_case'][date] = int(total_case)


    with open('../json/montreal.json', 'w') as f:
        f.write(json.dumps(montreal_json, indent=4, ensure_ascii=False))


def main():
    generate_region_json()
    generate_total_json()
    generate_montreal_json()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
