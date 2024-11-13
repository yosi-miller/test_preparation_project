import random

users = [u for u in range(1, 10001)]
black_users_list = set(random.randint(1, 10001) for _ in range(750))


def get_random_user_id():
    return users[random.randint(0, (10000 - 1))]