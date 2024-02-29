import socket
import sys
import threading
from queue import Queue

print_lock = threading.Lock()
q = Queue()


def tcp_scanner(host, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        remote_server_ip = socket.gethostbyname(host)
        sock.settimeout(0.5)
        result = sock.connect_ex((remote_server_ip, port))

        if result == 0:
            try:
                service = socket.getservbyport(port)
                print(f"Port {port} ({service}) is open")
            except OSError:
                print(f"Port {port} Unknown is open")
        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()


def threader():
    while True:
        host, port = q.get()
        tcp_scanner(host, port)
        q.task_done()


def main():

    host = None
    port_range = None

    flags = sys.argv[1:]

    if "-h" in flags or "--help" in flags:
        print("OPtion: -h, --help")
        print("Option: -port <port_range>, use all to scan all ports")
        print("Option: -host <host>")
        print("To use without flags, run:\n$ python3 main.py")
        print(
            "To use with flags, run:\n$ python3 main.py -host <host> -port <port_range> -o <output_file>"
        )
        print("Exiting...")
        sys.exit()

    if "-host" in flags:
        host = flags[flags.index("-host") + 1]
        print(f"Host: {host}")

    if "-port" in flags:
        port_range = flags[flags.index("-port") + 1]
        if port_range == "all":
            port_range = "1-65535"
        print(f"Port range: {port_range}")

    if not host:
        host = input("Enter the remote host or IP address to scan: ")

    if not port_range:
        port_range = input("Enter the range of ports to scan (e.g., 1-65535): ")
        if port_range == "all":
            port_range = "1-65535"

    start_port, end_port = map(int, port_range.split("-"))

    for x in range(100):
        thread = threading.Thread(target=threader)
        thread.daemon = True
        thread.start()

    for port in range(start_port, end_port + 1):
        q.put((host, port))

    q.join()


if __name__ == "__main__":
    print("Starting port scanner...")
    print("Press Ctrl+C to stop the scanner")
    main()
