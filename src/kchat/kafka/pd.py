from kafka import KafkaProducer
import time
import json

pd = KafkaProducer(
        bootstrap_servers=['localhost:9092'], value_serializer=lambda x:json.dumps(x).encode('utf-8')
        )
start = time.time()

for i in range(10):
    data = {'str':'value' + str(i)}
    pd.send('topic1', value=data)
    pd.flush()

end = time.time()
print("[DONE]:", end - start)
