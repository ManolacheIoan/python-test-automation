import socket

def check_port(host: str, port: int, timeout: float = 2.0) -> bool:
    """Check if a specific port is open on a host."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(timeout)
    try:
        result = sock.connect_ex((host, port))
        return result == 0
    finally:
        sock.close()

if __name__ == "__main__":
    common_ports = {80: "HTTP", 443: "HTTPS", 22: "SSH"}
    host = "google.com"
    for port, service in common_ports.items():
        status = "OPEN" if check_port(host, port) else "CLOSED"
        print(f"{host}:{port} ({service}) - {status}")
