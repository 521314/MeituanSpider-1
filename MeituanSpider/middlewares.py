import requests


class ProxyPoolMiddleware(object):
    """ IP代理 """
    def get_proxy(self):
        r = requests.get('http://127.0.0.1:5000/get')
        return "http://"+ r.text

    def process_request(self, request, spider):
        proxy = self.get_proxy()
        if proxy:
            request.meta["proxy"] = proxy


