from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class UtilityConstants:
    RESULTS_DIR = 'results'
    NAME = 'pep'
    ALLOWED_DOMAINS = ['peps.python.org']
    START_URLS = ['https://peps.python.org/']
    DATE_FORMAT = '%Y-%m-%d_%H-%M-%S'
    FILE_NAME = 'status_summary_'