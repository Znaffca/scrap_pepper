import requests
from bs4 import BeautifulSoup


class ScrapFinder:
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0"

    def __init__(self, request, url):
        self.request = request
        self.url = url
        self.user_agent = request.META.get("HTTP_USER_AGENT")
        self.headers = {"User-Agent": self.user_agent}
        self.page = requests.get(self.url, headers=self.headers)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
    
    def get_all_page_params(self, classname, html_input=None):
        if not self.soup.find_all(html_input, attrs={"class": classname}):
            return None
        return self.soup.find_all(html_input, attrs={"class": classname})


def get_page_param(soup, classname, html_input=None, html_text=None):

    result = soup.find(html_input, attrs={"class": classname})

    if not result:
        return None
    elif html_input and html_text:

        return result.get(html_text)
    return result.get_text()