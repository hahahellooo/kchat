from kafka import KafkaConsumer
from json import loads, dumps
import datetime
import json
import uuid

def consumer():
    unique_group_id = f'chat-group{uuid.uuid4()}'
    consumer = KafkaConsumer(
        'input',
        bootstrap_servers=['ec2-13-125-118-73.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='latest',
        group_id=unique_group_id,
        # 고유한 group_id 사용
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

    print("채팅 프로그램 - 메시지 수신")
    print("메시지 대기 중 ...")

# 예외 처리하는 구문
    try:
        for m in consumer:
            data = m.value
            sender = data['sender']
            print(f"[{sender}] {data['message']} 시간: {data['time']}" )

    except KeyboardInterrupt:
            print("채팅 종료")

    finally:
        consumer.close()


def producer():

    p = KafkaProducer(
        bootstrap_servers=['13.125.118.73:9092'],
        value_serializer=lambda x:json.dumps(x).encode('utf-8')
)


    print("채팅 프로그램 - 메시지 발신자")
    print("메시지를 입력하세요. (종료시 'exit' 입력)")

    while True:
        msg = input("YOU: ")
    if msg.lower() == 'exit':#대소문자 구문없이 exit를 받음
    

    data = {'sender' : '정미은', 'message': msg, 'time': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    p.send('input', value=data)
    p.flush()
    time.sleep(1)

print("채팅 종료")

if name == "main":
    # 먼저 Consumer를 시작
    consumer_thread = threading.Thread(target=consumer)
    consumer_thread.start()

    # Consumer가 실행된 후 Producer 시작
    time.sleep(1)  # 잠깐 대기하여 Consumer가 시작될 시간을 확보
    producer_thread = threading.Thread(target=producer)
    producer_thread.start()

    producer_thread.join()
    consumer_thread.join()
