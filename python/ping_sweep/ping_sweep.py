import subprocess
import platform
import ipaddress

def ping_host(ip):
    system_name = platform.system().lower()

    if system_name == "windows":
        command = ["ping", "-n", "1", "-w", "1000", str(ip)]
    else:
        command = ["ping", "-c", "1", "-W", "1", str(ip)]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0

def main():
    network_input = input("Enter a network in CIDR format (example: 192.168.1.0/24): ").strip()

    try:
        network = ipaddress.ip_network(network_input, strict=False)

        print(f"\n=== Ping Sweep Results for {network} ===")
        active_hosts = []

        for ip in network.hosts():
            if ping_host(ip):
                print(f"{ip} is UP")
                active_hosts.append(str(ip))

        if not active_hosts:
            print("No active hosts found.")

    except ValueError:
        print("Error: Invalid network format. Use CIDR notation like 192.168.1.0/24.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()