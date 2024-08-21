# kchat

### SET
```bash
$ bin/zookeeper-server-start.sh config/zookeeper.properties
$ bin/kafka-server-start.sh config/server.properties
```
### Dependencies
kafka-python>=2.0.2

### Python test
```bash
$ python src/kchat/kafka/pd.py
$ $KAFKA_HOME/bin/kafka-console-consumer.sh --topic topic1 --from-beginning --bootstrap-server localhost:9092
```
### result

![image](https://github.com/user-attachments/assets/21dc639a-4635-40c7-9961-869eeb00c8af)

![image](https://github.com/user-attachments/assets/edb7815d-d915-4cbb-b82b-0a225681ee60)


