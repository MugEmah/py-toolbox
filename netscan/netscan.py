import argparse
import platform
import subprocess
import ipaddress
from colorama import Fore, Style, init
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed
import signal
import sys

# Initialize colorama
init(autoreset=True)

# Graceful exit on Ctrl+C
def handle_sigint(sig, frame):
    print(f"\n{Fore.YELLOW}Scan interrupted by user. Exiting...{Style.RESET_ALL}")
    sys.exit(0)

signal.signal(signal.SIGINT, handle_sigint)

def ping_host(host):
    """Ping a single host and return True if reachable, False otherwise."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", host],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        return host, ("ttl=" in result.stdout.lower() or "time=" in result.stdout.lower())
    except Exception:
        return host, False

def expand_hosts(target):
    """Expand CIDR or single host into a list of IPs."""
    try:
        network = ipaddress.ip_network(target, strict=False)
        return [str(ip) for ip in network.hosts()]
    except ValueError:
        return [target]  # Single host or domain name

def scan_network(hosts, max_threads=50):
    """Scan a list of hosts in parallel."""
    results = []
    with ThreadPoolExecutor(max_workers=max_threads) as executor:
        futures = {executor.submit(ping_host, host): host for host in hosts}
        for future in tqdm(as_completed(futures), total=len(futures), desc="Scanning", ncols=80):
            results.append(future.result())
    return results

def main():
    parser = argparse.ArgumentParser(description="Fast Multithreaded Network Scanner")
    parser.add_argument("target", help="Host, domain, or network in CIDR (e.g., 192.168.1.0/30)")
    parser.add_argument("--threads", type=int, default=50, help="Number of threads (default=50)")
    args = parser.parse_args()

    hosts = expand_hosts(args.target)
    print(f"\n🔍 Scanning {len(hosts)} host(s) with {args.threads} threads...\n")

    try:
        results = scan_network(hosts, args.threads)
        for host, is_up in results:
            if is_up:
                print(f"{Fore.GREEN}{host} is UP{Style.RESET_ALL}")
            else:
                print(f"{Fore.RED}{host} is DOWN{Style.RESET_ALL}")
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}Scan interrupted. Showing partial results...\n{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
