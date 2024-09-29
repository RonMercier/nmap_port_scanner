# Nmap Port Scanner
I created a port scanner using Python and the Nmap tool.  This tool was made solely for learning and should only be used if you have permission to scan.

To create the port scanner, you will first need to install [Nmap](https://nmap.org/) and then the [python-nmap](https://pypi.org/project/python-nmap/) library.

### Windows
1. Download the installer from the [Nmap download page](https://nmap.org/download)
2. Run the installer and follow the on-screen instructions.

### Linux
Use the following commands in your terminal based on the distribution:
```
sudo apt-get install nmap      # For Debian-based systems
sudo yum install nmap          # For Red Hat-based systems
```

### macOS
Use the following command in your terminal:
```
brew install nmap              # Using Homebrew package manager
```

### Installing python-nmap
The python-nmap library provides a Python interface to Nmap.  You can install it using the following command:
```
pip install python-nmap
```

The script initializes the Nmap scanner using ```nmap.PortScanner()```.  Then the ```nm.scan(target, port_range)``` function performs the scan on the specified target and port range.

### Output
Host: 127.0.0.1 (localhost)
State: up

Protocol: TCP
Port: 631 State: open Service: ipp
