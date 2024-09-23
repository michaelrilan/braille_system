import subprocess
import webview
import time
import threading

# Start the Django server in a separate thread
def start_django():
    subprocess.Popen(['python', 'manage.py', 'runserver'])  # Starts Django server



def handle_file_download(url):
    print(f'Downloading from: {url}')
    # Handle download here


# Create PyWebview window after the server has started
def create_window():
    # Wait for a few seconds to allow the Django server to start
    time.sleep(10)
    # Load Django server URL into PyWebview window
    window = webview.create_window('My App', 'http://127.0.0.1:8000', webview_edge=True)
    window.events.file_download += handle_file_download
    webview.start()

if __name__ == '__main__':
    # Start Django server in the background
    t1 = threading.Thread(target=start_django)
    t1.start()

    # Start the PyWebview window
    create_window()

