l_username = ['ma.rilan', 'af.nazaire', 'jd.doe', 'jd.doe1']

def generate_unique_username(first_name, last_name, existing_usernames):
    # Split the first name to handle multiple words (e.g., "John Dave")
    first_name_parts = first_name.split()
    
    # Get the first letter of each part of the first name
    first_letters = ''.join([name[0].lower() for name in first_name_parts])
    
    # Lowercase the last name
    last_name_lower = last_name.lower()
    
    # Combine the first letters and the lowercase last name to form the initial username
    base_username = f"{first_letters}.{last_name_lower}"
    unique_username = base_username
    count = 1

    # Check if the username is unique, if not, append a number to make it unique
    while unique_username in existing_usernames:
        unique_username = f"{base_username}{count}"
        count += 1
    
    return unique_username

# Example usage
first_name = "John Dave"
last_name = "Doe"
new_username = generate_unique_username(first_name, last_name, l_username)

print(new_username)
