import argparse
import ipaddress
from port_scanner import port_scanning
from banner_grabber import banner_grabbing
from report import report_writing

def main():

    # argument parser
    parser = argparse.ArgumentParser(description="recon-kit")

    # arguments
    parser.add_argument("target_ip", help="insert target ip address")
    parser.add_argument("start_port", type=int, help="insert first port of scanning range (1-65535)")
    parser.add_argument("end_port", type=int, help="insert last port of scanning range (1-65535)")
    args = parser.parse_args()

    # ip validation
    try:
        ipaddress.ip_address(args.target_ip)
    except ValueError:
        parser.error(f"error: invalid IP address '{args.target_ip}'")

    # port validation
    if args.start_port > args.end_port:
        parser.error(f"starting port ({args.start_port}) exceeds ending port ({args.end_port})")
    if args.start_port < 1:
        parser.error(f"starting port ({args.start_port}) below min (1)")
    if args.start_port > 65535:
        parser.error(f"starting port ({args.start_port}) above max (65535)")
    if args.end_port < 1:
        parser.error(f"ending port ({args.end_port}) below min (1)")
    if args.end_port > 65535:
        parser.error(f"ending port ({args.end_port}) above max (65535)")

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
