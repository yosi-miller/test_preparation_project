import json

from kafka import KafkaConsumer

from database.repository import insert_to_black_list

consumer = KafkaConsumer(
    'black-transaction-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    group_id='transactions',
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))  # פענוח JSON
)


for transaction in consumer:
    transaction = transaction.value  # קבלת המידע כ-JSON

    # בדיקת התוכן שהתקבל
    print(f"Received Transaction ID: {transaction['transaction_id']}, Fishing status: {transaction['is_fishing']}")

    result = insert_to_black_list(transaction)

    print(f'insert id {result}')