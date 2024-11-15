import json

from data.transaction_model import create_transaction
import data.users_data as ud
from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8')  # המרה ל-JSON ואז ל-bytes
                         )

def check_is_fishing(check_transaction):
    if check_transaction['amount'] > 5000 or check_transaction['amount'] < 0.01:
        return True
    elif check_transaction['user_id'] in ud.black_users_list:
        return True
    return False


while True:
    user_id = ud.get_random_user_id()
    transaction = create_transaction(user_id)
    is_fishing = check_is_fishing(transaction)

    if is_fishing:
        transaction['is_fishing'] = True


    producer.send('transaction-topic', transaction)
    print(f'Transaction {transaction} sent')

producer.flush() # producer.flush is used to make sure that all messages are sent before closing the producer
producer.close() # close the producer