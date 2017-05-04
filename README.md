#### Port Check


Super basic socket based TCP port scanner.

You can check if a single port is open or a range of ports.

Mostly this was a project to add to my python skills. Using DOCSTRINGS, tests, more advanced argparse than I've used in the past, etc...

Using nose for testing. There are some basic tests. Messing with pycharm running the nose tests. 
```
usage: port_check.py [-h] -d DESTINATION [-v] -p [PORT [PORT ...]]

Port Check

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        Destination IP
  -v, --verbose         Verbose
  -p [PORT [PORT ...]], --port [PORT [PORT ...]]
                        Port(s)
```