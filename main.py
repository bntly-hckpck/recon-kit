import argparse
from port_scanner import port_scanning
from banner_grabber import banner_grabbing
from report import report_writing

# check if port is within range (1-65535)
def port_validation(port_number, arg_name):

    if port_number < 1 or port_number > 65535:
        print(f"error: {arg_name} must be in range (1-65535)")
        return False
    else:
        return True

def main():

    # argument parser
    parser = argparse.ArgumentParser(description="recon-kit")

    # arguments
    parser.add_argument("target_ip", help="insert target ip address")
    parser.add_argument("start_port", type=int, help="insert first port of scanning range (1-65535)")
    parser.add_argument("end_port", type=int, help="insert last port of scanning range (1-65535)")
    args = parser.parse_args()

    # port validation
    if not port_validation(args.start_port, "first port of scanning range"):
        exit(1)
    if not port_validation(args.end_port, "last port of scanning range"):
        exit(1)

    # extract values from args
    target_ip = args.target_ip
    start_port = args.start_port
    end_port = args.end_port

    # port scanning
    open_ports = port_scanning(target_ip, start_port, end_port)
    print(f"Found {len(open_ports)} open ports")

    # banner grabbing
    result = []
    for port in open_ports:
        banner = banner_grabbing(target_ip, port)
        result.append({"port" : port, "banner" : banner}) # dict for key-value pair
        print(f"{port}: {banner}")

    # report writing
    report_writing(result)

if __name__ == "__main__":
    main()
