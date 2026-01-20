import random
import time


def generate_random_with_timestamp():
    random_number = random.randint(1000, 9999)
    timestamp = int(time.time())
    return int(f"{random_number}{timestamp}")
