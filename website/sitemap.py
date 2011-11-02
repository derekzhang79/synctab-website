from datetime import datetime
from django.core import paginator

class WebsiteSitemap:
    limit = 50000

    priority = 1.0
    lastmod = datetime.now()

    def __init__(self):
        self._paginator = paginator.Paginator(self.items(), self.limit)

    def items(self):
        return ['/help', '/download', '/contact', '/submitIssue']

    def changefreq(self, item):
        if item.endswith("contact") or item.endswith("submitIssue"):
            return "weekly"
        
        return "daily"

    def __get(self, name, obj, default=None):
        try:
            attr = getattr(self, name)
        except AttributeError:
            return default
        if callable(attr):
            return attr(obj)
        return attr

    def get_urls(self, domain, page=1):
        urls = []

        for item in self._paginator.page(page).object_list:
            loc = "http://%s%s" % (domain, item)
            priority = self.__get('priority', item)
            url_info = {
                'location':   loc,
                'lastmod':    self.__get('lastmod', item),
                'changefreq': self.__get('changefreq', item),
                'priority':   str(priority is not None and priority or '')
            }
            urls.append(url_info)
        return urls
