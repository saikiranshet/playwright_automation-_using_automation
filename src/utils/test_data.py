import random
import string

def generate_random_username(length=8):
    # Generate a random string
    random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    # Combine the random string with 'gmail.com' to form the complete username
    return f"{random_string}@gmail.com"
