import socket

def check_port(host, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((host, port))
            return result == 0
    except socket.gaierror:
        print("Error: Could not resolve hostname.")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

def main():
    host = input("Enter a hostname or IP address: ").strip()

    try:
        port = int(input("Enter a port number: ").strip())

        if port < 1 or port > 65535:
            print("Error: Port number must be between 1 and 65535.")
            return

        is_open = check_port(host, port)

        if is_open is True:
            print(f"Port {port} on {host} is OPEN.")
        elif is_open is False:
            print(f"Port {port} on {host} is CLOSED or not reachable.")

    except ValueError:
        print("Error: Please enter a valid numeric port.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()