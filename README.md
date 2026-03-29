# Assignment3
Scan hosts using ping and measure response time Retrieve ARP table and display IP-MAC mappings Perform network scans using Nmap

---------------------------------------------------------------------------------------------------
1st out put
┌──(kali㉿kali)-[~/Downloads/assignment]
└─$ python3 ping_scanner.py
Enter IP / Hostname: 127.0.0.1
[+] 127.0.0.1 is UP | Response Time: 7.41 ms

----------------------------------------------------------------------------------------------------
2nd output
(kali㉿kali)-[~/Downloads/assignment]
└─$ python3 arp_scanner.py
Press Enter to retrieve ARP table...127.0.0.1

=== ARP Table ===
Address                  HWtype  HWaddress           Flags Mask            Iface
192.168.142.2            ether   00:50:56:f7:3e:a8   C                     eth0
192.168.142.1            ether   00:50:56:c0:00:08   C                     eth0
192.168.142.254          ether   00:50:56:f5:8a:5c   C                     eth0

----------------------------------------------------------------------------------------------------
3rd output
┌──(kali㉿kali)-[~/Downloads/assignment]
└─$ python3 nmap_scanner.py                           
=== Nmap Scanner ===
Enter IP / Hostname / Network: 127.0.0.1

Select Scan Type:
1. Host Discovery (-sn)
2. Port Scan (-sS)
3. Custom Port Scan
4. Service Detection (-sV)
5. OS Detection (-O)
Enter choice: 1

=== Scan Results ===
Starting Nmap 7.95 ( https://nmap.org ) at 2026-03-29 07:32 EDT
Nmap scan report for localhost (127.0.0.1)
Host is up.
Nmap done: 1 IP address (1 host up) scanned in 0.00 seconds
