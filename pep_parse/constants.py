from pathlib import Path

BASE_DIR = Path(__file__).parent.parent


class UtilityConstants:
    RESULTS_DIR = 'results'
    NAME = 'pep'
    ALLOWED_DOMAINS = ['peps.python.org']
    START_URLS = [f'https://{domain}/' for domain in ALLOWED_DOMAINS]
