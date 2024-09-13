import random
import string

def generate_random_string(length=10):
    # Define the possible characters
    characters = string.ascii_letters + string.digits
    
    # Generate a random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    
    return "#" + random_string

# Generate a 10-character random string
print(generate_random_string())