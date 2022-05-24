from utils.redisserver import Redis
import json

redis = Redis()

redis.insertDateJob(article_id=1,data={
    "url": 'http://baidu.com',
    "status": 0
})

job = redis.getDateJob(article_id=1)
print(json.dumps(job))