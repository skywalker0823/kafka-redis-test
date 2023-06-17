from kafka import KafkaConsumer
import os
from dotenv import load_dotenv

load_dotenv()

consumer = KafkaConsumer(
  bootstrap_servers=[os.getenv('kafka_server')],
  sasl_mechanism='SCRAM-SHA-256',
  security_protocol='SASL_SSL',
  sasl_plain_username=os.getenv('kafka_username'),
  sasl_plain_password=os.getenv('kafka_password'),
  group_id='chatter',
  auto_offset_reset='earliest',
)
# ...

try:
    print("開始接收訊息")
    consumer.subscribe(['chatter'])
    while True:
        for message in consumer:
            print(message)
except KeyboardInterrupt:
    print("結束程式")
    consumer.close()