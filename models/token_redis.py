from redis import  Redis

rd = Redis(host='160.6.68.3',
           db=0,
           decode_responses=True
           )

def save_token(token, user_id):
    # 数据类型是string
    rd.set(token, user_id)
    rd.expire(token, 3 * 24 * 3600)