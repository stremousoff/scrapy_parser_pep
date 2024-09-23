**Асинхронный парсер PEP**
=========================

Парсер статусов PEP (Python Enhancement Proposal) на базе фреймворка Scrapy и их анализ.

**Возможности**
------------

* Сохранение всех PEP статусов Python в файл
* Сбор статистики о количестве статусов PEP Python и общем количестве

**Использованные технологии**
---------------------------

* Python
* Scrapy

**Установка**
------------

1. Клонировать репозиторий и перейти в него:
```bash
git clone git@github.com:stremousoff/scrapy_parser_pep.git
cd scrapy_parser_pep
```
2. Создать и активировать виртуальное окружение:
```bash
python -m venv venv
source venv/scripts/activate
```
3. Установить зависимости из файла `requirements.txt`:
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
**Использование**
--------------

Запустить парсер из командной строки с указанием имени spider:
```bash
scrapy crawl pep
```
В результате работы парсера все данные сохраняться в папку `result/`

**Автор**
--------

[Антон Стремоусов](https://github.com/stremousoff)