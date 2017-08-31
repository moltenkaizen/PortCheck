class PortCheck:

    def __init__(self, **kwargs):
        self.host = kwargs.get('host')
        self.port_string = kwargs.get('ports', '1-1024')
        self.port_list = []
        self.verbose = kwargs.get('verbose', False)


    def check_socket(self, port):
        """
        Accept host and port.

        Try to connect to that host/port
        Print result of that attempt
        """
        with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as sock:
            if sock.connect_ex((self.host, port)) == 0:
                print("Port: " + str(port) + " is open")
            else:
                if self.verbose == True or len(self.port_list) <= 3:
                    print("Port: " + str(port) + " is closed")


    def port_scan(self):
        """
        Accept host and port range.

        Loop through port range running the check_socket for each
        """
        for i in self.port_list:
            check_socket(i)
            # sleep(3.0 / 1000.0)


    def valid_port_number(self):
        """Check if ports fit 1-65535."""
        for i in self.port_list:
            if (i < 1 or i > 65535)
                print('Ports must be in range')
                return


    def populate_list(self):
        rangeSet = self.port_string.split(",")
        for singleRange in rangeSet:
            if '-' in singleRange
                range(self.singleRange)
