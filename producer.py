from kafka import KafkaProducer
from json import dumps
import time

producer = KafkaProducer(
        acks=1, # 메시지 전송 완료에 대한 체크
        bootstrap_servers=['kafka1:9092','kafka2:9092','kafka3:9092'], # 전달하고자 하는 카프카 브로커의 주소 리스트
        value_serializer=lambda x:dumps(x).encode('utf-8') # 메시지의 값 직렬화
    )

while(True):
    data = {'str' : 'result'+str(time.time())}
    producer.send('temp', value=data)
    producer.flush()
    print(data)
    time.sleep(0.1)
 
