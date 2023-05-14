### Create topic
``bin/kafka-topics.sh --create --bootstrap-server localhost:9092 --replication-factor 1 --partitions 1 --topic test_topic``

### List tpoics
``bin/kafka-topics.sh --list --bootstrap-server localhost:9092``

### Initiate a producer
``bin/kafka-console-producer.sh --broker-list localhost:9092 --topic test_tpoic``

### Consuming Messages
``bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic test_topic``

### Start zookeeper service
``sudo systemctl enable --now zookeeper.service``

### Start kafka service
``sudo systemctl enable --now kafka.service``

### Check status of kafka and zookeeper service
``sudo systemctl status kafka zookeeper``

### Check kafka server logs
``tail -50 /usr/local/kafka-server/logs/server.log``
