from kafka import KafkaConsumer
from json import loads

consumer = KafkaConsumer(
        'input',
        bootstrap_servers=['ec2-13-125-118-73.ap-northeast-2.compute.amazonaws.com:9092'],
        auto_offset_reset='latest',
        group_id="chat-group",
        enable_auto_commit=True,
        value_deserializer=lambda x: loads(x.decode('utf-8'))
)

print("채팅 프로그램 - 메시지 수신")
print("메시지 대기 중 ...")

# 예외 처리하는 구문
try:
    for m in consumer:
        data = m.value
        print(f"[FRIEND] {data['message']} {data['time']}" )

except KeyboardInterrupt:
    print("채팅 종료")

finally:
    consumer.close()

