import requests
from bs4 import BeautifulSoup
from django.shortcuts import render
from django import views
from soup.soup import ScrapFinder, get_page_param

# from django.views.generic import TemplateView


class SearchRtvView(views.View):

    URL = "https://www.pepper.pl/grupa/audiowizualne-nowe"

    def get(self, request):

        soup = ScrapFinder(request, self.URL)
        promo_list = soup.get_all_page_params("thread--deal")
        ctx = {}
        num = 0

        for promo in promo_list:
            ctx[f"promo-{num}"] = {
                "title": get_page_param(promo, "thread-title"),
                "price": get_page_param(promo, "thread-price"),
                "old_price": get_page_param(promo, "mute--text"),
                "code": get_page_param(promo, "clickable", "input", "value"),
                "hot": get_page_param(promo, "vote-temp--hot", "span"),
                "link": get_page_param(promo, "cept-dealBtn", "a", "href"),
                "link2": get_page_param(promo, "cept-tb", "a", "href")
            }

            num += 1

        return render(request, "pepper_searcher/index.html", {"ctx": ctx})


class SearchPcView(views.View):

    URL = "https://www.pepper.pl/grupa/komputery-nowe"

    def get(self, request):

        soup = ScrapFinder(request, self.URL)
        promo_list = soup.get_all_page_params("thread--deal")
        ctx = {}
        num = 0

        for promo in promo_list:
            ctx[f"promo-{num}"] = {
                "title": get_page_param(promo, "thread-title"),
                "price": get_page_param(promo, "thread-price"),
                "old_price": get_page_param(promo, "mute--text"),
                "code": get_page_param(promo, "clickable", "input", "value"),
                "hot": get_page_param(promo, "vote-temp--hot", "span"),
                "link": get_page_param(promo, "cept-dealBtn", "a", "href"),
                "link2": get_page_param(promo, "cept-tb", "a", "href")
            }

            num += 1

        return render(request, "pepper_searcher/index.html", {"ctx": ctx})
