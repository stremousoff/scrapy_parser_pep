import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.constants import BASE_DIR, UtilityConstants


class PepParsePipeline:

    def __init__(self):
        self.result = defaultdict(int)

    def open_spider(self, spider):
        self.results_dir = BASE_DIR / UtilityConstants.RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
                self.results_dir / '{}{}.csv'.format(
                    UtilityConstants.FILE_NAME,
                    datetime.now().strftime(UtilityConstants.DATE_FORMAT)
                ),
                'w',
                encoding='utf-8'
        ) as file:
            csv.writer(file, dialect=csv.excel, lineterminator='\n').writerows(
                (
                    ('Status', 'Quantity'),
                    *self.result.items(),
                    ('Total', sum(self.result.values()))
                )
            )
