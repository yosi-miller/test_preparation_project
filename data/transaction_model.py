import random
import time
import uuid


def create_transaction(user_id):
    transaction = {
        'transaction_id': str(uuid.uuid4()),  # UUID ייחודי
        'user_id': user_id,
        'amount': round(random.uniform(0.01, 7500), 2),
        'timestamp': time.time(),
        'is_fishing': False
        }
    return transaction