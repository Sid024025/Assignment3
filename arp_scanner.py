import subprocess
import platform

def get_arp_table():
    try:
        if platform.system().lower() == "windows":
            command = ["arp", "-a"]
        else:
            command = ["arp", "-n"]

        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        print("\n=== ARP Table ===")
        print(result.stdout)

    except Exception as e:
        print(f"[ERROR] {e}")

def main():
    input("Press Enter to retrieve ARP table...")
    get_arp_table()

if __name__ == "__main__":
    main()
