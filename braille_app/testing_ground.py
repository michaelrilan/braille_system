# l_username = ['ma.rilan', 'af.nazaire', 'jd.doe', 'jd.doe1']

# def generate_unique_username(first_name, last_name, existing_usernames):
#     # Split the first name to handle multiple words (e.g., "John Dave")
#     first_name_parts = first_name.split()
    
#     # Get the first letter of each part of the first name
#     first_letters = ''.join([name[0].lower() for name in first_name_parts])
    
#     # Lowercase the last name
#     last_name_lower = last_name.lower()
    
#     # Combine the first letters and the lowercase last name to form the initial username
#     base_username = f"{first_letters}.{last_name_lower}"
#     unique_username = base_username
#     count = 1

#     # Check if the username is unique, if not, append a number to make it unique
#     while unique_username in existing_usernames:
#         unique_username = f"{base_username}{count}"
#         count += 1
    
#     return unique_username

# # Example usage
# first_name = "John Dave"
# last_name = "Doe"
# new_username = generate_unique_username(first_name, last_name, l_username)

# print(new_username)


# import socket

# def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
#     """
#     Checks if the machine has internet connection by trying to establish a socket connection 
#     to a reliable host (default is Google's public DNS server).
    
#     Args:
#         host (str): The host to connect to, default is Google's DNS (8.8.8.8).
#         port (int): The port to use, default is 53 (DNS service).
#         timeout (int): The timeout duration in seconds for the connection attempt.

#     Returns:
#         bool: True if connection is successful, False otherwise.
#     """
#     try:
#         socket.setdefaulttimeout(timeout)
#         # Try to establish a connection
#         socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#         return True
#     except socket.error as ex:
#         print(f"Connection failed: {ex}")
#         return False

# # Example usage
# if check_internet_connection():
#     print("Internet connection is active.")
# else:
#     print("No internet connection.")




import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

# Function to generate PDF
def generate_pdf():
    # Define the directory and file name
    directory = "static/document"
    file_name = "hello_world.pdf"
    file_path = os.path.join(directory, file_name)

    # Create directory if it doesn't exist
    if not os.path.exists(directory):
        os.makedirs(directory)

    # Create a canvas object
    c = canvas.Canvas(file_path, pagesize=letter)

    # Set the font to Arial, 22 point
    c.setFont("Helvetica", 22)  # ReportLab doesn't have Arial, use Helvetica instead
    
    # Calculate the center of the page
    width, height = letter
    text = "Hello World"
    text_width = c.stringWidth(text, "Helvetica", 22)
    
    # Draw the title at the center of the page
    c.drawString((width - text_width) / 2, height / 2, text)
    
    # Save the PDF
    c.save()

# Run the function
generate_pdf()
