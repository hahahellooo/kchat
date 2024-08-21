from kafka import KafkaProducer
import time
import json
from tqdm import tqdm 

pd = KafkaProducer(
        bootstrap_servers=['localhost:9092'], value_serializer=lambda x:json.dumps(x).encode('utf-8')
        )
start = time.time()

for i in tqdm(range(10)):
    data = {'str':'value' + str(i)}
    pd.send('topic1', value=data)
    pd.flush()
    time.sleep(1)
end = time.time()
print("[DONE]:", end - start)
