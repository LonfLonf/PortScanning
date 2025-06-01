import argparse
import socket

port_services = {
    20: "FTP (Data)",
    21: "FTP (Control)",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP (Server)",
    68: "DHCP (Client)",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPCbind",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP Trap",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    515: "LPD (Printer)",
    587: "SMTP (submission)",
    631: "IPP (Printing)",
    636: "LDAPS",
    993: "IMAPS",
    995: "POP3S",
    1080: "SOCKS Proxy",
    1433: "Microsoft SQL Server",
    1521: "Oracle DB",
    1723: "PPTP (VPN)",
    2049: "NFS",
    2181: "Zookeeper",
    3306: "MySQL",
    3389: "RDP",
    3690: "Subversion (SVN)",
    4000: "Remote Anything",
    4444: "Metasploit (default handler)",
    5432: "PostgreSQL",
    5900: "VNC",
    5985: "WinRM (HTTP)",
    5986: "WinRM (HTTPS)",
    6379: "Redis",
    8000: "HTTP (Alt)",
    8080: "HTTP Proxy",
    8443: "HTTPS (Alt)",
    9000: "PHP-FPM",
    9200: "Elasticsearch",
    10000: "Webmin"
}

web_ports = [80, 443, 8080, 8000, 8443]

remote_ports = [22, 23, 3389, 5900]

database_ports = [3306, 5432, 1433, 1521]

file_ports = [20, 21, 137, 138, 139, 445]

top_10_ports = [21, 22, 23, 25, 53, 80, 110, 139, 443, 445]

top_20_ports = [
    20, 21, 22, 23, 25, 53, 67, 68, 69, 80,
    110, 111, 135, 139, 143, 161, 443, 445, 993, 3306
]

nmap_top_100 = [
    7, 20, 21, 22, 23, 25, 26, 37, 53, 79, 80, 81, 82, 83, 84, 85, 88,
    89, 90, 99, 100, 106, 109, 110, 111, 113, 119, 125, 135, 139, 143,
    144, 146, 161, 163, 179, 199, 211, 212, 222, 254, 255, 256, 259,
    264, 280, 311, 340, 366, 389, 406, 407, 416, 417, 425, 427, 443,
    444, 458, 464, 465, 481, 497, 500, 512, 513, 514, 515, 524, 541,
    543, 544, 545, 548, 554, 555, 563, 587, 593, 616, 617, 625, 631,
    636, 646, 648, 666, 667, 668, 683, 687, 691, 700, 705, 711, 714,
    720, 722, 726, 749, 765, 777, 783, 787, 800, 801, 808, 843, 873,
    880, 888, 898, 900, 901, 902, 903, 911, 912, 981, 987, 990, 992,
    993, 995, 999, 1000, 1001
]

time = {
    "fast": 0.5,
    "normal": 1.0,
    "full": 3.0
}

def SelectorPreser(input, start, end):
    if input == "top10":
        return top_10_ports
    elif input == "top20":
        return top_20_ports
    elif input == "top100":
        return nmap_top_100
    elif input == "web":
        return web_ports
    elif input == "remote":
        return remote_ports
    elif input == "database":
        return database_ports
    elif input == "file":
        return file_ports
    elif input == "default":
        return list(range(start, end + 1))
    else:
        return None

def PrintStatus(verbose, result, service, port):
    if result == 0:
        print(f"[+] Port {port} is open ({service})")
    elif verbose:
        print(f"[-] Port {port} is closed ({service})")
        
def PortScan(target, preset, time, verbose):
    for port in preset:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(time)
        result = s.connect_ex((target, port))
        service = port_services.get(port, "Unknown Service")
        PrintStatus(verbose, result, service, port)
        s.close()
            
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-target", help="IP or URL", required=True)
    parser.add_argument("-start", help="Start Port", type=int, default=1)
    parser.add_argument("-end", help="End Port", type=int, default=5000)
    parser.add_argument("-mode", help="(Fast, Normal, Full)", default="normal")
    parser.add_argument("-preset", help="(Normal)", default="default")
    parser.add_argument("-v", help="Verbose mode",  action="store_true")
    
    args = parser.parse_args();
    preset = SelectorPreser(args.preset.lower(), args.start, args.end)
    timeout = time.get(args.mode.lower(), 1)
    PortScan(args.target, preset, timeout, args.v)
    
if __name__ == "__main__":
    main()
    

