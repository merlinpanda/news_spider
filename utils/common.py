import scrapy

class Common(scrapy.Spider):
    MAIN_CHANNEL_TYPE = 0
    SUB_CHANNEL_TYPE = 1

    CHANNELS = [
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "24hours",
            "title": "新闻"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "ent",
            "title": "娱乐"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "milite",
            "title": "军事"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "world",
            "title": "国际"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "tech",
            "title": "科技"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "finance",
            "title": "财经"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "auto",
            "title": "汽车"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "finance_stock",
            "title": "证券"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "house",
            "title": "房产"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "digi",
            "title": "数码"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "health",
            "title": "健康"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "edu",
            "title": "教育"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "finance_licai",
            "title": "理财"
        },
        {
            "type": MAIN_CHANNEL_TYPE,
            "name": "kepu",
            "title": "科普"
        }
    ]

    # 获取子频道文章
    def getSubChannel(self):
        pass

    # 获取主频道文章
    def getChannel(self):
        pass

    # 获取今日要闻
    def todayMainNews(self):
        pass

    # 获取今日话题
    def todayTopic(self):
        pass

    # 获取较真文章
    def jiaoZhen(self):
        pass

    # 获取热门资讯
    def hotNews(self):
        pass

    # 获取精品原创
    def bestOrigin(self):
        pass