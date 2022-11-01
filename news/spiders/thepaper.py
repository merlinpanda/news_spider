import scrapy, requests, json


class ThepaperSpider(scrapy.Spider):
    name = 'thepaper'

    API = 'https://api.thepaper.cn/contentapi/nodeCont/getByNodeIdPortal'

    SPIDER_CHANNEL = [25949, 108856, 25950, 25951, 119908, 25952, 119489, 25953, -23, 122153]

    articles = []

    def start_requests(self):
        nodes = self.getAllNodes()
        if len(nodes) > 0:
            for node in nodes:
                nodeId = node['nodeId']
                forwordType = node['forwordType']
                nodeType = node['nodeType']

                if nodeId in self.SPIDER_CHANNEL:

                    pass
        pass

    def parse(self, response):
        pass

    def spider_article(self, response):
        pass

    def getAllNodes(self):
        url = 'https://cache.thepaper.cn/contentapi/node/getWwwAllNodes'
        response = requests.get(url)
        res = json.loads(response.text)
        if res['code'] == 200:
            return res['data']['channelList']
        else:
            return []
