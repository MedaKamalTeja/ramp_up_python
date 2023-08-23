import re
import os
import subprocess

def validate_ip(ip):
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    return re.match(pattern, ip)

def is_pingable(ip):
    result = subprocess.call(['ping', '-c', '1', ip])
    return result == 0

def write_to_file(filename, ip_list):
    with open(filename, 'w') as file:
        for ip in ip_list:
            file.write(ip + '\n')
    print(f"IPs written to '{filename}'.")

def main():
    pinging_ips = []
    not_pinging_ips = []

    while True:
        user_input = input("Enter an IP address (Yes/No): ").strip().lower()

        if user_input == 'no':
            write_to_file('pinging_ips.txt', pinging_ips)
            write_to_file('not_pinging_ips.txt', not_pinging_ips)
            print("IPs written to 'pinging_ips.txt' and 'not_pinging_ips.txt'.")
            break
        elif user_input == 'yes':
            user_ip = input("Enter an IP address: ").strip()
            if validate_ip(user_ip):
                if is_pingable(user_ip):
                    pinging_ips.append(user_ip)
                    print("IP is pingable. Added to pinging list.")
                else:
                    not_pinging_ips.append(user_ip)
                    print("IP is not pingable. Added to not pinging list.")
            else:
                print("Invalid IP address. Please enter a valid IP.")
        else:
            print("Invalid input. Please enter Yes or No.")

if __name__ == "__main__":
    main()
