import platform
import socket
import getpass

def get_hostname():
    return socket.gethostname()

def get_ip_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except Exception:
        return "Unable to determine IP address"

def main():
    print("=== System Information ===")
    print(f"Hostname: {get_hostname()}")
    print(f"Operating System: {platform.system()} {platform.release()}")
    print(f"OS Version: {platform.version()}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"IP Address: {get_ip_address()}")
    print(f"Python Version: {platform.python_version()}")
    print(f"Current User: {getpass.getuser()}")

if __name__ == "__main__":
    main()