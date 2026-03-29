import subprocess

def run_nmap_scan(target, options):
    try:
        command = ["nmap"] + options + [target]
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print("\n=== Scan Results ===")
        print(result.stdout)

    except FileNotFoundError:
        print("[ERROR] Nmap is not installed or not in PATH")
    except Exception as e:
        print(f"[ERROR] {e}")

def main():
    print("=== Nmap Scanner ===")
    target = input("Enter IP / Hostname / Network: ")

    print("\nSelect Scan Type:")
    print("1. Host Discovery (-sn)")
    print("2. Port Scan (-sS)")
    print("3. Custom Port Scan")
    print("4. Service Detection (-sV)")
    print("5. OS Detection (-O)")

    choice = input("Enter choice: ")

    if choice == "1":
        options = ["-sn"]
    elif choice == "2":
        options = ["-sS"]
    elif choice == "3":
        ports = input("Enter ports (e.g., 22,80,443): ")
        options = ["-p", ports]
    elif choice == "4":
        options = ["-sV"]
    elif choice == "5":
        options = ["-O"]
    else:
        print("Invalid choice")
        return

    run_nmap_scan(target, options)

if __name__ == "__main__":
    main()
