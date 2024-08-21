from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        "topic1",
        bootstrap_servers=['localhost:9092'],
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=5000,
        auto_offset_reset='earliest',#'latest''earliest'
        group_id="Wednesday",
        enable_auto_commit=True,
)

print('[Start] get consumer')
for m in consumer:
    print(f"topic={m.topic}", f"partition={m.partition}", f"offset={m.offset}", f"timestamp_type={m.timestamp_type}")
   # ConsumerRecord(topic='topic1', partition=0, offset=150, timestamp=1724219004618, timestamp_type=0, key=None, value={'str': 'value9'}, headers=[], checksum=None, serialized_key_size=-1, serialized_value_size=17, serialized_header_size=-1)
print('[End] get consumer')

