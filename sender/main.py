import time
from send_function.send_post_data import send_post_data
from generator.generate_random_number import generate_random_number
from utils import (
    RANDOM_STRING_LENGTH,
    KEEPER_HOST,
    KEEPER_PORT,
    KEEPER_METHOD,
)


if __name__ == "__main__":
    while True:
        try:
            data = generate_random_number(length=RANDOM_STRING_LENGTH)
            send_post_data(
                    data=data, host=KEEPER_HOST, port=KEEPER_PORT, method=KEEPER_METHOD
                )
            print(f"Forwarded: {data}")
        except ConnectionRefusedError:
            print("Connection to the server refused. Make sure the server is running.")
        time.sleep(2)