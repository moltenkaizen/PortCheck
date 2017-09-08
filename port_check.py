"""
Port Check Utility.

Parses arguments passed on the commandline
Scans a single port or a range of ports
Socket is used to make a connection and determine if the port is open

Possible future improvements:
Add the ability to scan a list of ports
Multithreaded scans
Optional delay timing between socket connections to prevent flooding
Would writing a Class be better?
Add tests
"""
import socket
import ipaddress
from colorama import Fore, Back, Style
from socket import AF_INET, SOCK_STREAM
import argparse

def IP_Address(address):
    return ipaddress.ip_address(address)

parser = argparse.ArgumentParser(description='Port Check')
parser.add_argument('-d', '--destination',
                    help='Destination IP',
                    required=True,
                    type=IP_Address)
parser.add_argument('-t', '--timeout',
                    help='Timeout in miliseconds',
                    required=False,
                    type=int,
                    default=1000)
parser.add_argument('-v', '--verbose',
                    help='Verbose',
                    required=False,
                    action="store_true")
# parser.add_argument('args', nargs=argparse.REMAINDER)
parser.add_argument('-p', '--port',
                    help='Port(s)',
                    required=True,
                    type=int,
                    nargs='*')


def check_socket(host, port, verbose, mode, timeout):
    """
    Accept host and port.

    Try to connect to that host/port
    Print result of that attempt
    """
    connection = socket.socket(AF_INET, SOCK_STREAM)
    sec_timeout = float(timeout) / 1000.0
    if verbose:
        print('Timeout sec: ', sec_timeout)
    connection.settimeout(sec_timeout)

    try:
        status = connection.connect_ex((host, port))
        if status == 0:
            print("Port: " + str(port) + " is " + Fore.GREEN + "open")
            print(Style.RESET_ALL)
        else:
            if verbose or mode == 'single':
                print("Port: " + str(port) + " is " + Fore.RED + "closed")
                print(Style.RESET_ALL)

    except (socket.timeout, socket.gaierror) as error:
        print(error)
    finally:
        connection.close()


def port_scan(host, port_start, port_end, verbose, mode, timeout):
    """
    Accept host and port range.

    Loop through port range running the check_socket for each
    """
    for i in range(port_start, port_end):
        check_socket(host, i, verbose, mode, timeout)
        # sleep(3.0 / 1000.0)


def valid_port_number(port):
    """Check port if is 1-65535."""
    if port > 0 and port <= 65535:
        return True
    else:
        return False


def get_port_scan_mode(port_list):
    """Parse the args.port list to determine scan mode."""
    if len(port_list) == 1:
        return 'single'
    elif len(port_list) == 2:
        if port_list[0] < port_list[1]:
            return 'range'
        else:
            return 'invalid'
    elif len(port_list) > 2:
        return 'invalid'


def main(parser):
    """Main Function."""
    # Resolve host to ip. This seems to be ok if you pass an ip or a hostname
    args = parser.parse_args()
    verbose = args.verbose
    destination = args.destination.exploded
    remote_server = socket.gethostbyname(destination)
    timeout = args.timeout

    # Check len(items) in args.port list to use single or port range mode
    if get_port_scan_mode(args.port) == 'single':
        port = args.port[0]
        if valid_port_number(port):
            print('Single port mode')
            print('Checking ' + str(port) +
                  ' on ' + remote_server)
            check_socket(remote_server, port, verbose, 'single', timeout)
        else:
            parser.error('Port must be in the range 1-65535')
    elif get_port_scan_mode(args.port) == 'range':
        port_start = args.port[0]
        port_end = args.port[1]
        if valid_port_number(port_start) and valid_port_number(port_end):
            print('Port range mode')
            print('Checking ' + str(port_start) + ' to ' + str(port_end) +
                  ' on ' + remote_server)
            port_scan(remote_server, port_start, port_end, verbose, 'range', timeout)
        else:
            parser.error('Ports must be in the range 1-65535')
    else:
        parser.error('Invalid Port(s) specified.\
              Either select one port or a range of ports. -p 1 1000')


if __name__ == "__main__":
    # Pass the args object parsed from command line args to main()
    main(parser=parser)
