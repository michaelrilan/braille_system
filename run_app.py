# import webview
# import os
# import socket

# # Check if the Django server is running by attempting to connect
# def is_server_running(host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.settimeout(1)  # Set timeout to 1 second
#         try:
#             sock.connect((host, port))
#         except socket.error:
#             return False
#     return True

# # Create PyWebview window
# def create_window():
#     print("Checking if server is running...")
    
#     if is_server_running('127.0.0.1', 1201):
#         print("Server is running. Creating a window for the Django app.")
#         # If the server is running, load the Django server URL into PyWebview window
#         window = webview.create_window('Braille App', 'http://127.0.0.1:1201')
#         webview.start()
#     else:
#         # Correct path for 'error.html'
#         current_dir = os.path.dirname(os.path.abspath(__file__))
#         error_file_path = os.path.join(current_dir, 'error.html')  # Adjusted path
        
#         print(f"Server is not running. Checking for error file at {error_file_path}...")
        
#         if os.path.exists(error_file_path):
#             print("Error file found. Creating a window to display the error file.")
#             window = webview.create_window('Error', f'file://{error_file_path}')
#             webview.start()
#         else:
#             print(f"Error file not found: {error_file_path}")
#             # Fallback to create a window with an error message
#             window = webview.create_window('Error', 'data:text/html,Error file not found')
#             webview.start()

# if __name__ == '__main__':
#     create_window()



# import subprocess
# import webview
# import time
# import threading
# import socket

# # Start the Django server in a separate thread
# def start_django():
#     subprocess.Popen(['python', 'manage.py', 'runserver', '127.0.0.1:1201'])  # Starts Django server

# # Check if the Django server is running by attempting to connect
# def is_server_running(host, port):
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
#         sock.settimeout(1)  # Set timeout to 1 second
#         try:
#             sock.connect((host, port))
#         except socket.error:
#             return False
#     return True

# # Wait until the server is running
# def wait_for_server(host, port, timeout=30):
#     for _ in range(timeout):
#         if is_server_running(host, port):
#             print("Server is running!")
#             return True
#         time.sleep(1)
#     return False

# # Create PyWebview window after the server has started
# def create_window():
#     # Wait until the server is running
#     if wait_for_server('127.0.0.1', 1201):
#         # Load Django server URL into PyWebview window
#         webview.create_window('Braille App', 'http://127.0.0.1:1201')
#         webview.start()
#     else:
#         print("Failed to connect to the server within the timeout period.")

# if __name__ == '__main__':
#     # Start Django server in the background
#     t1 = threading.Thread(target=start_django)
#     t1.start()

#     # Start the PyWebview window
#     create_window()



import subprocess
import webview
import time
import threading
import socket
import os
import sys

# Start the Django server in a minimized window
def start_django():
    # Start the server in a minimized command prompt
    if sys.platform == "win32":
        # On Windows, use the 'START /MIN' command to minimize the window
        subprocess.Popen(['cmd', '/c', 'start', '/min', 'python', 'manage.py', 'runserver', '127.0.0.1:1201'],
                         creationflags=subprocess.CREATE_NEW_CONSOLE)
    else:
        # For other platforms, start normally (you may need to adapt this for other OS)
        subprocess.Popen(['python', 'manage.py', 'runserver', '127.0.0.1:1201'])

# Check if the Django server is running by attempting to connect
def is_server_running(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set timeout to 1 second
        try:
            sock.connect((host, port))
        except socket.error:
            return False
    return True

# Wait until the server is running
def wait_for_server(host, port, timeout=30):
    for _ in range(timeout):
        if is_server_running(host, port):
            print("Server is running!")
            return True
        time.sleep(1)
    return False

# Create PyWebview window after the server has started
def create_window():
    # Wait until the server is running
    if wait_for_server('127.0.0.1', 1201):
        # Load Django server URL into PyWebview window
        webview.create_window('Braille App', 'http://127.0.0.1:1201')
        webview.start()
    else:
        print("Failed to connect to the server within the timeout period.")

if __name__ == '__main__':
    # Check if the server is already running
    if not is_server_running('127.0.0.1', 1201):
        # Start Django server in the background if not already running
        t1 = threading.Thread(target=start_django)
        t1.start()

    # Start the PyWebview window
    create_window()
