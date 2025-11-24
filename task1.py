from queue import Queue

def main():
    queue = Queue()

    for i in range(5):
        request = f"Request {i+1}"
        print(f"Adding to queue: {request}")
        queue.put(request)

    while not queue.empty():
        processed_request = queue.get()
        print(f"Processing and removing from queue: {processed_request}")

if __name__ == "__main__":
    main()