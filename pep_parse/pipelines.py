import csv
from collections import defaultdict
from datetime import datetime

from pep_parse.settings import (BASE_DIR, DATE_FORMAT, FILE_NAME,
                                UtilityConstants)


class PepParsePipeline:
    def open_spider(self, spider):
        self.result = defaultdict(int)

    def process_item(self, item, spider):
        self.result[item['status']] += 1
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / UtilityConstants.RESULTS_DIR
        file_name = '{}{}.csv'.format(
            FILE_NAME,
            datetime.now().strftime(DATE_FORMAT)
        )
        with open(results_dir / file_name, 'w', encoding='utf-8') as file:
            csv.writer(file, dialect=csv.excel, lineterminator='\n').writerows(
                (
                    ('Status', 'Quantity'),
                    *self.result.items(),
                    ('Total', sum(self.result.values()))
                )
            )
