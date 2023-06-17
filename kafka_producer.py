from kafka import KafkaProducer
import os
from dotenv import load_dotenv

load_dotenv()
 
producer = KafkaProducer(
  bootstrap_servers=[os.getenv('kafka_server')],
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username=os.getenv('kafka_username'),
  sasl_plain_password=os.getenv('kafka_password'),
)
# ...

# producer.send('chatter', b'Hello Upstash!')
count = 0
for i in range(100):

    future = producer.send('chatter', f'Hello Upstash! {count}'.encode('utf-8'))
    record_metadata = future.get(timeout=10)
    print(i)
    count += 1
producer.close()




