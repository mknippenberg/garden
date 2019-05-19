# Notes

This is mainly a directory to play around with and learn event driven technology.

## Sanity test for kafka and zookeeper

From the EDA directory run:

    docker-compose up -d

create topic

    kafka-topics --create --bootstrap-server eda-zk:2181 --replication-factor 1 --partitions 1 --topic test

producer

    kafka-console-producer --broker-list eda-kafka:9093 --topic test

read from test topic

    kafka-console-consumer --bootstrap-server eda-kafka:9093 --topic test --from-beginning