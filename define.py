import socket

# Đặt thông tin domain và port
host = 'hngl2808.pythonanywhere.com'  # Thay bằng domain bạn muốn truy cập
port = 80             # Port 80 cho HTTP

# Tạo socket và kết nối tới domain
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    
    # Gửi request HTTP GET
    request = f"GET / HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"
    s.sendall(request.encode())

    # Nhận dữ liệu trả về từ server
    response = b""
    while True:
        data = s.recv(1024)
        if not data:
            break
        response += data

# Giải mã và in ra kết quả
print(response.decode())
