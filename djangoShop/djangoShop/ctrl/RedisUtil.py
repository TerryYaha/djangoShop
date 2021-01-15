import redis


def readProp(key):
    redisInfo = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
    return redisInfo.get(key)

def setProp(key, val):
    redisInfo = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
    redisInfo.set(key, val)
    # 取出数据
    # redisInfo.get('您好')