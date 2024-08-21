from kafka import KafkaProducer
from json import dumps
import time
import json

p = KafkaProducer(
        bootstrap_servers=['localhost:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
)


print("채팅 프로그램 - 메시지 발신자")
print("메시지를 입력하세요. (종료시 'exit' 입력)")

while True:
    msg = input("YOU: ")
    if msg.lower() == 'exit':#대소문자 구문없이 exit를 받음
        break

    data = {'message': msg, 'time': time.time()}
    p.send('chat', value=data)
    p.flush()
    time.sleep(1)

print("채팅 종료")
