#!/usr/bin/env python3

from jinja2 import Template
from pprint import pprint

"""
Take the data from the csv files in ../csv and turn them into an HTML webpage
"""

def chart_data_regions(regions):
    """
    Generate info to be used in the HTML page chart
    """
    rgb_color = [
        '198,40,40',
        '173,20,87',
        '106,27,154',
        '69,39,160',
        '40,53,147',
        '21,101,192',
        '2,119,189',
        '0,131,143',
        '0,105,92',
        '46,125,50',
        '85,139,47',
        '158,157,36',
        '158,157,36',
        '249,168,37',
        '255,143,0',
        '239,108,0',
        '216,67,21',
        '78,52,46'
    ]

    chart_data = {'dates': [], 'regions': {}}
    for region, date, new_case, total_case in regions:
        # Add date to dates
        if date not in chart_data['dates']:
            chart_data['dates'].append(date)

        # Add region data for this date
        if region not in chart_data['regions']:
            chart_data['regions'][region] = {'label': region, 'data': [], 'color': rgb_color.pop(0)}

        chart_data['regions'][region]['data'].append(total_case)

    return chart_data


def main():
    # Get regions data
    with open('../csv/region.csv') as f:
        regions = [x.strip().split(',') for x in f.readlines()]

    # Get total data
    with open('../csv/total.csv') as f:
        total = [x.strip().split(',') for x in f.readlines()]

    # Remove headers
    regions.pop(0)
    total.pop(0)

    # Generate HTML with jinja2
    html_template = Template(open('template.html').read())
    rendered = html_template.render(
        regions = regions,
        total = total,
        datasets = chart_data_regions(regions)
    )

    with open('../data.html', 'w') as f:
        f.write(rendered)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
