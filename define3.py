import concurrent.futures
import threading

# Đếm số luồng tối đa
def test_thread():
    while True:
        pass  # Luồng giả chỉ để chiếm tài nguyên

# Thử tạo nhiều luồng cho đến khi xảy ra lỗi
max_threads = 0
try:
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        while True:
            futures.append(executor.submit(test_thread))
            max_threads += 1
            print(max_threads)
except RuntimeError:
    print(f"Số luồng tối đa là: {max_threads}")
