# Training parsing

Practicum Training Parsing is a collection of Python scripts for web scraping, HTTP request caching, regular expressions, and command-line argument parsing.

## TECH STACK

![BeautifulSoup4](https://img.shields.io/badge/requests-black?style=for-the-badge&logoColor=#005FAD)
![BeautifulSoup4](https://img.shields.io/badge/BeautifulSoup4-black?style=for-the-badge&logoColor=#005FAD)
![LXML](https://img.shields.io/badge/xml-black?style=for-the-badge&logo=xml&logoColor=#005FAD)
![Python](https://img.shields.io/badge/python-black?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/SQLite-black?style=for-the-badge&logo=sqlite&logoColor=blue)
![Git](https://img.shields.io/badge/git-black.svg?style=for-the-badge&logo=git&logoColor=orange)

## Project Structure

- `antarctic_timezone.py` — fetches current time and UTC offset for Vostok Station via API with periodic `CachedSession` cache clearing.
- `arg_parsing.py` — CLI script built with `argparse` supporting positional arguments, `choices`, and custom flags.
- `caching.py` — basic example of HTTP response caching and inspecting cached URLs with `requests-cache`.
- `download.py` — parses `docs.python.org` using `BeautifulSoup` and `re` to find and download the PDF (A4) documentation archive into `downloads/`.
- `latest_versions.py` — scrapes the Python documentation sidebar to extract all Python versions, statuses, and links.
- `progress_bar.py` — demonstrates terminal progress bars with custom descriptions using `tqdm`.
- `re_exp.py` — extracts city, street, house, and apartment numbers from text strings using regex named groups.
- `requests_vs_requests_cache.py` — benchmarks standard `requests` against `requests-cache` on delayed endpoints.
- `soup.py` — minimal `BeautifulSoup` HTML parsing setup with the `lxml` parser.
- `url_getting.py` — filters `<a>` tags in HTML using regular expressions to extract direct image links.
- `whats_new.py` — scrapes the "What's New in Python" section and collects titles, links, and author metadata.

## How to Run the Project

Clone the repository and navigate into it

```bash
git clone https://github.com/briliov/practicum-training-parsing
```

```bash
cd practicum-training-parsing
```

Create and activate a virtual environment

```bash
python3 -m venv .venv
```

Linux | Mac

```bash
source .venv/bin/activate
```

Windows

```bash
source .venv/scripts/activate
```

Install dependencies from requirements.txt

```bash
python3 -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

Run any script from the repository

```bash
python3 whats_new.py
```

```bash
python3 arg_parsing.py Stepan -s Yakovlev -c Minsk --murzik
```
