import json

from kafka import KafkaConsumer, KafkaProducer

# Replace 'your-topic' with the actual topic name
consumer = KafkaConsumer(
    'transaction-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='transactions',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # פענוח JSON
)

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))  # המרה ל-JSON)


def check_transaction_fishing(transaction):
    pass


for transaction in consumer:
    print(transaction['transaction_id'])
    # check_transaction_fishing(transaction)

    if transaction['is_fishing']:
        producer.send('transaction-topic', value=transaction)
        print('Transaction is fished!')
    else:
        if transaction['amount'] > 3000:
            producer.send('transaction-topic', value=transaction)
            print('Transaction is above 3000')
        else:
            producer.send('transaction-topic', value=transaction)
            print('Transaction is ok!')

producer.flush()
producer.close()