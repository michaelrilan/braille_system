# import subprocess
# import webview
# import time
# import threading

# # Start the Django server in a separate thread
# def start_django():
#     subprocess.Popen(['python', 'manage.py', 'runserver', '127.0.0.1:1201'])  # Starts Django server

# # Create PyWebview window after the server has started
# def create_window():
#     # Wait for a few seconds to allow the Django server to start
#     time.sleep(10)
#     # Load Django server URL into PyWebview window
#     webview.create_window('Braille App', 'http://127.0.0.1:1201')
#     webview.start()

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

# Start the Django server in a separate thread
def start_django():
    subprocess.Popen(['python', 'manage.py', 'runserver', '127.0.0.1:1201'])  # Starts Django server

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
    # Start Django server in the background
    t1 = threading.Thread(target=start_django)
    t1.start()

    # Start the PyWebview window
    create_window()
