import re
from pathlib import Path
from urllib.parse import urljoin

import requests_cache
from bs4 import BeautifulSoup

DOWNLOADS_URL: str = 'https://docs.python.org/3/download.html'
BASE_DIR: Path = Path(__file__).parent

downloads_dir: Path = BASE_DIR / 'downloads'
downloads_dir.mkdir(exist_ok=True)

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, features='lxml')
    main_div = soup.find('div', {'role': 'main'})
    if main_div:
        table_tag = main_div.find('table', {'class': 'docutils'})
        if table_tag:
            pdf_a4_tag = table_tag.find(
                'a',
                {'href': re.compile(r'.+html\.zip$')},
            )
            if pdf_a4_tag:
                pdf_a4_link = pdf_a4_tag['href']
                if isinstance(pdf_a4_link, str):
                    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
                    filename = archive_url.split('/')[-1]
                    archive_path: Path = downloads_dir / filename
                    response = session.get(archive_url)
                    with open(archive_path, 'wb') as file:
                        file.write(response.content)
