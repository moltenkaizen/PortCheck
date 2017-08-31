"""
Port Check Utility.

Parses arguments passed on the commandline
Scans a list of ports
Socket is used to make a connection and determine if the port is open

Possible improvements:
Class-ify
Ability to scan a list of ports
Add tests
Optional delay timing between socket connections to prevent flooding
Multithreaded scans
"""
import socket
from contextlib import closing
# from time import sleep
import argparse

parser = argparse.ArgumentParser(description='Port Check')
parser.add_argument('-d', '--destination',
                    help='Destination IP',
                    required=True)
parser.add_argument('-v', '--verbose',
                    help='Verbose',
                    required=False,
                    action="store_true")
# parser.add_argument('args', nargs=argparse.REMAINDER)
parser.add_argument('-p', '--port',
                    help='Port(s)',
                    required=False,
                    type=str,
                    nargs='*')


def main(parser):
    """Main Function."""
    # Resolve host to ip. This seems to be ok if you pass an ip or a hostname
    args = parser.parse_args()
    verbose = args.verbose
    destination = args.destination
    remote_server = socket.gethostbyname(destination)

    # Check len(items) in args.port list to use single or port range mode
    if get_port_scan_mode(args.port) == 'single':
        port = args.port[0]
        if valid_port_number(port):
            print('Single port mode')
            print('Checking ' + str(port) +
                  ' on ' + remote_server)
            check_socket(remote_server, port, verbose, 'single')
        else:
            parser.error('Port must be in the range 1-65535')
    elif get_port_scan_mode(args.port) == 'range':
        port_start = args.port[0]
        port_end = args.port[1]
        if valid_port_number(port_start) and valid_port_number(port_end):
            print('Port range mode')
            print('Checking ' + str(port_start) + ' to ' + str(port_end) +
                  ' on ' + remote_server)
            port_scan(remote_server, port_start, port_end, verbose, 'range')
        else:
            parser.error('Ports must be in the range 1-65535')
    else:
        parser.error('Invalid Port(s) specified.\
              Either select one port or a range of ports. -p 1 1000')


if __name__ == "__main__":
    # Pass the args object parsed from command line args to main()
    main(parser=parser)
