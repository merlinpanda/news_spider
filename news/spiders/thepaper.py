import scrapy, requests, json, time


class ThepaperSpider(scrapy.Spider):
    name = 'thepaper'

    API = 'https://api.thepaper.cn/contentapi/nodeCont/getByNodeIdPortal'

    SPIDER_CHANNEL = [25949, 108856, 25950, 25951, 119908, 25952, 119489, 25953, -23, 122153]

    articles = []

    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Origin': 'https://www.thepaper.cn',
        'Referer': 'https://www.thepaper.cn/',
        'Host': 'api.thepaper.cn',
        'Cookie': 'Hm_lvt_94a1e06bbce219d29285cee2e37d1d26=1667312558; acw_tc=76b20f7116673239132413006e349c8f318ef2ab1ef40e209003d7d1cd49c0; ariaDefaultTheme=undefined; Hm_lpvt_94a1e06bbce219d29285cee2e37d1d26=1667324077',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    def start_requests(self):
        timenow = int(round(time.time() * 1000))
        nodes = self.getAllNodes()
        if nodes:
            for node in nodes:
                nodeId = node['nodeId']
                if nodeId in self.SPIDER_CHANNEL:
                    try:
                        children = node['childNodeList']
                    except:
                        continue

                    if children:
                        for child in children:
                            body = self.param(nodeId= child['nodeId'], page= 1, time= timenow)
                            body = json.dumps(body)
                            yield scrapy.Request(url=self.API, method = 'POST', headers = json.dumps(self.headers), body= body, callback=self.parse)


    def category(self, nodeId, page, time):
        body = self.param(nodeId= nodeId, page= page, time= time)
        body = json.dumps(body)
        yield scrapy.Request(url=self.API, method = 'POST', headers = json.dumps(self.headers), body= body, callback=self.parse)

    def param(self, nodeId, page, time):
        return {
            "nodeId": nodeId,
            "excludeContIds": [],
            "pageSize": 20,
            "startTime": time,
            "pageNum": page
        }

    def parse(self, response):
        try:
            print("*"*40)
            print(response.body)
            print("*"*40)
            body = json.loads(response.body)
            # if body['code'] == 200:
            #     articles = body['data']['list']
            #     if articles:
            #         for article in articles:
            #             yield self.spider_article(article=article)

            #     has_next = body['data']['hasNext']
            #     if has_next == True:
            #         prev_request = json.loads(response.request.body)
            #         yield self.category(nodeId=prev_request['nodeId'], page = eval(prev_request['page']) + 1, time= prev_request['startTime'] )
        except:
            print("&"*40)

    def spider_article(self, article):
        url = 'https://www.thepaper.cn/newsDetail_forward_' + str(article['contId'])
        return scrapy.Request(url=url, headers=json.dumps(self.headers), callback=self.parse_article)

    def parse_article(self, response):
        print("*"*40)
        print(response.body)
        print("*"*40)

    def getAllNodes(self):
        try:
            url = 'https://cache.thepaper.cn/contentapi/node/getWwwAllNodes'
            response = requests.get(url)
            res = json.loads(response.text)
            if res['code'] == 200:
                return res['data']['channelList']
            else:
                return None
        except:
            print("there cont get nodes")
