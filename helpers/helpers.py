import random
import string


def generate_fields_user(user_data):
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    fields_collection={}

    for field in user_data:
        fields_collection[field] = generate_random_string(10)

    return fields_collection
