from utils.common import Common

class QqNewsSpider(Common):
    name = 'qq_news'

    def start_requests(self):
        channel = getattr(self,'channel', None)
        print('channel', channel)
        pass

    def parse(self, response):
        pass
