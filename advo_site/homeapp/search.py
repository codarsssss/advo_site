import requests
from bs4 import BeautifulSoup
import re
import lxml
from lxml import html
from advo_site.settings import ALLOWED_HOSTS, DEBUG


def search(user_input):

    if DEBUG:
        BASE_URL = 'http://127.0.0.1:8000'
    else:
        BASE_URL = 'https://' + ALLOWED_HOSTS[0]

    search_result = []
    if user_input:
        urls = [
            BASE_URL + '',
            BASE_URL + '/team/',
            BASE_URL + '/cases/',
            BASE_URL + '/career/',
            BASE_URL + '/zashchita-pri-ugolovnom-presledovanii/',
            BASE_URL + '/ugolovno-pravovaya-zashchita-biznesa/',
            BASE_URL + '/antikorruptsionnyy-komplayns/',
            BASE_URL + '/semeynaya-praktikapraktika/',
            BASE_URL + '/zemelnaya-praktika/',
            BASE_URL + '/nalogovaya-praktika/',
            BASE_URL + '/mediatsiya/',
            BASE_URL + '/it-ip-praktika/',
            BASE_URL + '/korporativnaya-praktika/',
            BASE_URL + '/meditsinskoe-pravo/',
            BASE_URL + '/arbitrazhnaya-praktika/',
            BASE_URL + '/sanktsionnaya-praktika/',
            BASE_URL + '/kak-my-rabotaem/',
            BASE_URL + '/polnomochiya-advokata/',
            BASE_URL + '/advokatskaya-tayna/',
            BASE_URL + '/soglashenie-i-order/',
            BASE_URL + '/varianty-voznagrozhdeniya/',
            BASE_URL + '/cases/1/',
            BASE_URL + '/cases/2/',
            BASE_URL + '/cases/3/',
            BASE_URL + '/cases/4/',
            BASE_URL + '/cases/5/',
            BASE_URL + '/cases/6/',
            BASE_URL + '/cases/7/',
            BASE_URL + '/cases/8/',
            BASE_URL + '/cases/9/',
            BASE_URL + '/cases/10/',
            BASE_URL + '/cases/11/',
            BASE_URL + '/cases/12/',
            BASE_URL + '/cases/13/',
            BASE_URL + '/cases/14/',
            BASE_URL + '/cases/15/',
            BASE_URL + '/privicy/'
        ]
        for url in urls:
            try:
                response = requests.get(url)
                if response.status_code == 200:
                    response.encoding = 'utf-8'
                    soup = BeautifulSoup(response.text, 'lxml')
                    page_content = soup.get_text()
                    title_tag = soup.find('title')
                    title = title_tag.text

                    if user_input.lower() in page_content.lower():
                        page_content = page_content.lower()
                        page_content = page_content.rstrip()

                        match_start = re.search(user_input.lower(), page_content).start()

                        page_content = page_content[match_start:match_start + 100]
                        search_result.append(('...{}...'.format(page_content), url, title))
            except requests.exceptions.RequestException:
                print(requests.exceptions.RequestException)

    return search_result



