"""Parallel URLs loading using ThreadPoolExecutor"""

import logging
import re
import urllib.request

from concurrent.futures import ThreadPoolExecutor


logging.basicConfig(level=logging.INFO, format='%(asctime)s:%(message)s')

# Some regex for the HTML parsing
TITLE_RE = re.compile(r'<title>(.+?)</title>')
HREF_RE = re.compile(r'href="(.+?)"')


def parallel(n_of_threads, func, args):
    """Apply `args` to `func` in parallel and return results"""
    pool = ThreadPoolExecutor(n_of_threads)
    results = [r for r in pool.map(func, args)]
    return results

def load(url: str) -> str:
    """Load HTML from the given `url`"""
    logging.info('Load "%s"', url)

    html = None
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read().decode('utf-8')
    except urllib.error.HTTPError as e:
        logging.warning('Error loading "%s": %s', url, e)

    return html or ''

def get_title(html: str) -> str:
    """Extract a content of <title> tag from given `html`"""
    # Never parse an HTML with the regex!
    g = TITLE_RE.search(html).groups()
    return g[0] if g else None

def pipeline(url: str) -> str:
    """Combine sequential stages"""
    html = load(url)
    title = get_title(html)
    logging.info('Got "%s"', title)

    return title


if __name__ == '__main__':
    urls = ['http://google.com', 'http://yandex.ru', 'http://bing.com']
    threads = 8

    print(parallel(threads, pipeline, urls))
