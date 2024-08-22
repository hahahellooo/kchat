from kafka import KafkaProducer
import time
import json
from tqdm import tqdm 

pd = KafkaProducer(
        bootstrap_servers=['172.17.0.1:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8'),
        compression_type='gzip',
        batch_size=100
        
        )
start = time.time()

for i in tqdm(range(10000)):
    data = {'str':'value' + str(i)}
    pd.send('test-gzip-4', value=data)
    pd.flush()
    time.sleep(0.001)
end = time.time()
print("[DONE]:", end - start)
