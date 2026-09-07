import subprocess
import platform

def ping_host(host: str, count: int = 4) -> bool:
    """Ping a host and return True if reachable."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, str(count), host]
    result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return result.returncode == 0

if __name__ == "__main__":
    hosts = ["google.com", "github.com", "1.1.1.1"]
    for host in hosts:
        status = "UP" if ping_host(host) else "DOWN"
        print(f"{host}: {status}")
