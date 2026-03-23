import shutil

def bytes_to_gb(num_bytes):
    return num_bytes / (1024 ** 3)

def main():
    path = input("Enter a drive or folder path to check (example: C:\\ or /): ").strip()

    try:
        total, used, free = shutil.disk_usage(path)

        total_gb = bytes_to_gb(total)
        used_gb = bytes_to_gb(used)
        free_gb = bytes_to_gb(free)
        free_percent = (free / total) * 100

        print("\n=== Disk Usage Report ===")
        print(f"Path: {path}")
        print(f"Total Space: {total_gb:.2f} GB")
        print(f"Used Space:  {used_gb:.2f} GB")
        print(f"Free Space:  {free_gb:.2f} GB")
        print(f"Free Space Percentage: {free_percent:.2f}%")

        if free_percent < 15:
            print("WARNING: Low disk space.")
        else:
            print("Disk space is at a healthy level.")

    except FileNotFoundError:
        print("Error: The path you entered does not exist.")
    except PermissionError:
        print("Error: Permission denied for that path.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()