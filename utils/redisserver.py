import redis, datetime, json

class Redis():

    date_job_name = 'date:jobs:'

    date_author_name = 'date:author:'

    def __init__(self):
        self.redis = redis.StrictRedis(
                host='192.168.171.128',
            port=6379,
            decode_responses=True)

    # 文章详情任务键名
    def dateJobName(self, date = None):
        if date is not None:
            return self.date_job_name + str(date)
        else:
            date = datetime.datetime.now().strftime("%Y%m%d")
            return self.date_job_name + str(date)

    def getDateJob(self,date = None, article_id = None):
        return json.loads(self.redis.hget(self.dateJobName(date), article_id))

    def getDateJobKeys(self, date = None):
        return self.redis.hkeys(self.dateJobName(date))

    def insertDateJob(self,date = None, article_id = None, data = None):
        self.redis.hset(self.dateJobName(date),article_id, json.dumps(data))