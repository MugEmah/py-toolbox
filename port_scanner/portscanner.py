import argparse
import socket
import ipaddress
import platform
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from tqdm import tqdm
from colorama import Fore, Style, init
import signal
import sys

# Initialize colorama
init(autoreset=True)

# Graceful exit
def handle_sigint(sig, frame):
    print(f"\n{Fore.YELLOW}Scan interrupted by user. Exiting...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

# Common ports for service detection
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    50: "IPSec",
    67: "DHCP",
    68: "DHCP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "MSRPC",
    137: "NetBIOS",
    138: "NetBIOS",
    139: "NetBIOS",
    143: "IMAP",
    161: "SNMP",
    162: "SNMP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Proxy"
}

def detect_os(ip):
    """Basic OS detection using ping TTL value."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", ip],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout.lower()
        if "ttl=" in output:
            ttl = int(output.split("ttl=")[1].split()[0])
            if ttl <= 64:
                return "Linux/Unix"
            elif ttl <= 128:
                return "Windows"
            else:
                return "Unknown"
    except Exception:
        return "Unknown"
    return "Unknown"

def scan_port(ip, port, timeout=1):
    """Try connecting to a port, return service if open."""
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            if s.connect_ex((ip, port)) == 0:
                service = COMMON_PORTS.get(port, "Unknown")
                return port, service
    except:
        return None
    return None

def expand_hosts(target):
    """Expand CIDR or single host into a list of IPs."""
    try:
        network = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return [target]  # Single host or domain

def scan_host(ip, ports, threads):
    """Scan a single host for open ports."""
    open_ports = []
    with ThreadPoolExecutor(max_workers=threads) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in ports}
        for future in as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)
    return open_ports

def main():
    parser = argparse.ArgumentParser(description="Multithreaded Python Port Scanner")
    parser.add_argument("target", help="Target IP, domain, or subnet (CIDR)")
    parser.add_argument("--ports", default="1-1024", help="Port range, e.g. 1-65535 (default: 1-1024)")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads (default: 100)")
    args = parser.parse_args()

    # Parse ports
    start_port, end_port = map(int, args.ports.split("-"))
    ports = range(start_port, end_port + 1)

    # Expand hosts
    hosts = expand_hosts(args.target)
    print(f"\n Scanning {len(hosts)} host(s) | Ports {start_port}-{end_port} | Threads {args.threads}\n")

    for ip in tqdm(hosts, desc="Scanning Hosts", ncols=80):
        try:
            os_guess = detect_os(ip)
            open_ports = scan_host(ip, ports, args.threads)

            print(f"\n{Fore.CYAN}Host: {ip} | OS: {os_guess}{Style.RESET_ALL}")
            if open_ports:
                for port, service in open_ports:
                    print(f"  {Fore.GREEN}[+] Port {port} OPEN ({service}){Style.RESET_ALL}")
            else:
                print(f"  {Fore.RED}No open ports found{Style.RESET_ALL}")
        except KeyboardInterrupt:
            print(f"\n{Fore.YELLOW}Scan interrupted! Partial results above.{Style.RESET_ALL}")
            sys.exit(0)

if __name__ == "__main__":
    main()
