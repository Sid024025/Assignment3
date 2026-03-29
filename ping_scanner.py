import platform
import subprocess
import time

def ping_host(host):
    param = "-n" if platform.system().lower() == "windows" else "-c"
    command = ["ping", param, "1", host]

    try:
        start = time.time()
        output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, timeout=3)
        end = time.time()

        if output.returncode == 0:
            print(f"[+] {host} is UP | Response Time: {(end - start)*1000:.2f} ms")
        else:
            print(f"[-] {host} is DOWN")
    except subprocess.TimeoutExpired:
        print(f"[!] {host} timed out")

def main():
    target = input("Enter IP / Hostname: ")
    ping_host(target)

if __name__ == "__main__":
    main()
