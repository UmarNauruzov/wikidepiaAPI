import requests
from bs4 import BeautifulSoup
import logging


class WikipediaCrawler:
    def __init__(self):
        self.visited_pages = set() #visited_pages - множество всех посещенных страниц
        self.links_to_visit = set() #links_to_visit - множество ссылок, которые необходимо обработать

    # Функция crawl принимает начальную и конечную ссылки и возвращает путь между этими страницами на Википедии.
    def crawl(self, start_url, end_url):
        self.links_to_visit.add(start_url)
        path, found = self._bfs(start_url, end_url)
        return path if found else []
    """
    Функция _bfs реализует алгоритм поиска в ширину для нахождения пути между 
    начальной и конечной страницами. Она принимает начальную и конечную ссылки, 
    итерируется по ссылкам на страницы, которые можно получить из текущей страницы. 
    Если ссылка ведет на страницу на Википедии, и еще не была посещена, она добавляется в очередь на обработку.
    """
    def _bfs(self, start_url, end_url):
        queue = [(start_url, [])]
        while queue:
            url, path = queue.pop(0)
            if url == end_url:
                return path + [url], True
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                self.visited_pages.add(url)
                for link in soup.find_all('a', href=True):
                    link_url = link['href']
                    if link_url.startswith('/wiki/'):
                        full_link = 'https://ru.wikipedia.org' + link_url
                        if full_link not in self.visited_pages:
                            queue.append((full_link, path + [url]))
            except Exception as e:
                logging.error('Error while crawling {}: {}'.format(url, e))
        return [], False


if __name__ == '__main__':
    start_url = input('Введите ссылку на начальную страницу Википедии: ')
    end_url = input('Введите ссылку на конечную страницу Википедии: ')
    crawler = WikipediaCrawler()
    path = crawler.crawl(start_url, end_url)
    if path:
        for url in path:
            try:
                response = requests.get(url)
                soup = BeautifulSoup(response.content, 'html.parser')
                print('{}------------------------'.format(path.index(url) + 1))
                print(soup.find('p').text)
                if url != path[-1]:
                    print(path[path.index(url) + 1])
            except Exception as e:
                logging.error('Error while crawling {}: {}'.format(url, e))
    else:
        print('Путь между страницами не найден')
