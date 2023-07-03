import redis
import os
from dotenv import load_dotenv
import json


load_dotenv()

r = redis.Redis(
  host= os.getenv('redis_host'),
  port= '33367',
  password= os.getenv('redis_password')
)


# {account:socketid}
# {socket_id : {who?:room,who2:room2...}}



r.set('account','socket_id')
r.set('socket_id','{"who":"room","who2":"room2"}')

# 讀取並設置
a = json.loads(r.get('socket_id'))
a["who3"] = "room3"
r.set('socket_id',json.dumps(a))

# 讀取
b = json.loads(r.get('socket_id'))

# 刪除
c = json.loads(r.get('socket_id'))
# 將who刪除 
c.pop('who')
# 把c設置回去
r.set('socket_id',json.dumps(c))



print(b)
print(c)

