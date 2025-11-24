import queue
import random
import time

request_queue = queue.Queue()
request_id = 0

def generate_request():
    """Generates a new request and adds it to the queue."""
    global request_id
    request_id += 1
    request = f"Request-{request_id}"
    request_queue.put(request)
    print(f"Generated and added a new request: {request}. Queue size: {request_queue.qsize()}")

def process_request():
    """Processes a request from the queue."""
    if not request_queue.empty():
        processed_request = request_queue.get()
        print(f"Processing request: {processed_request}. Queue size: {request_queue.qsize()}")
    else:
        print("Queue is empty, no requests to process.")

def main():
    """Main program loop."""
    try:
        while True:
            if random.choice([True, False]):
                generate_request()
            
            process_request()
            
            time.sleep(1)

    except KeyboardInterrupt:
        print("\nProgram terminated by user.") 

if __name__ == "__main__":
    main()