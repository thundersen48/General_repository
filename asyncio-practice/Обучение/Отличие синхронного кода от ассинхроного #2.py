import time

filename_main = "test_sync.txt"

def write(data: str, filename: str):
    """Запись строки в файл"""
    with open(filename, mode="a") as f:
        f.write(data + "\n")

def make_requests():
    for i in range(100000):
        write(f"Test {i}", filename_main)

def main():
    start_time = time.time()
    make_requests()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Total execution time: {elapsed_time} seconds")

if name == "main":
    main()