from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDER_MODULES = ['pep_parse.spiders']
NEWSPIDER_MODULE = SPIDER_MODULES

ROBOTSTXT_OBEY = True


class UtilityConstants:
    RESULTS_DIR = 'results'
    NAME = 'pep'
    ALLOWED_DOMAINS = ['peps.python.org']
    START_URLS = [f'https://{domain}/' for domain in ALLOWED_DOMAINS]


FEEDS = {
    f'{UtilityConstants.RESULTS_DIR}/pep_%(time)s.csv': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
FILE_NAME = 'status_summary_'

BASE_DIR = Path(__file__).parent.parent
