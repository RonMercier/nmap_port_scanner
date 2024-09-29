import nmap
import sys

#Function to perform the scan
def nmap_port_scanner(target, port_range):
    #Initializes the Nmap Port Scanner
    nm = nmap.PortScanner()

    #Perform the scan
    try:
        nm.scan(target, port_range)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()

    #Prints the results
    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")

            lport = nm[host][proto].keys()
            sorted(lport)
            for port in lport:
                print(f"Port: {port}\tState: {nm[host][proto]['state']}\tService: {nm[host][proto][port]['name']}")

if __name__ == "__main__":
    #Replace (example.com) with your target hostname or IP address
    target = "example.com"

    #Define the range of ports to scan (ex: "1-1024" for ports 1 to 1024)
    port_range = "1-1024"

    nmap_port_scanner(target, port_range)