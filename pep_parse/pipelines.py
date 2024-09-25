import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import BASE_DIR, DATE_FORMAT, FILE_NAME, RESULTS_DIR


class PepParsePipeline:
    @classmethod
    def from_crawler(cls, crawler):
        (BASE_DIR / RESULTS_DIR).mkdir(exist_ok=True)
        return cls()

    def open_spider(self, spider):
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        with open(
                BASE_DIR / RESULTS_DIR / '{name}_{date}.csv'.format(
                    name=FILE_NAME, date=datetime.now().strftime(DATE_FORMAT)
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
