from queue import Queue
import time
import random

# Create request queue
request_queue = Queue()

def generate_request():
    req_id = random.randint(1000, 9999)
    print(f"Generated request #{req_id}")
    request_queue.put(req_id)

def process_request():
    if not request_queue.empty():
        req_id = request_queue.get()
        print(f"Processing request #{req_id}")
        time.sleep(1)
    else:
        print("Queue is empty")

if __name__ == "__main__":
    print("System started. Press Ctrl+C to stop.")
    try:
        while True:
            # Simulate random request generation
            if random.choice([True, False]):
                generate_request()
            
            process_request()
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\nProgram stopped.")