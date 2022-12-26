import subprocess
import ipaddress
import requests
import socket
import time
import re
import os

msg = """IP Multi-Tool by Precious1337
                        
                        
                        LookUp an IP(1)
                        
                        Get Website IP(2)
                        
                        View your IP(3)
                        
                        Ping an IP(4)
                        
                        NSLookIp Host(5)
                        
                        Exit(0)
                        
                        
>"""
os.system("cls||clear")
option = int(input(msg))
option1 = option

def ping(ip_address):
    sent_requests = 0
    replies = 0
    timeouts = 0
    lowest_latency = float('inf')
    highest_latency = 0
    total_latency = 0
    while True:
        result = subprocess.run(['ping', '-n', '1', ip_address], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        if "Destination host unreachable" in output:
            print("IP is offline")
        elif "Request timed out" in output:
            timeouts += 1
        else:
            sent_requests += 1
            replies += 1
            latency_match = re.search(r'Average = (\d+)ms', output)
            if latency_match:
                latency = int(latency_match.group(1))
                total_latency += latency
                lowest_latency = min(lowest_latency, latency)
                highest_latency = max(highest_latency, latency)
                average_latency = total_latency / replies
        os.system("cls||clear")
        print(f"Sent requests: {sent_requests}\nReplies: {replies}\nTimeouts: {timeouts}\nLowest latency: {lowest_latency}ms\nHighest latency: {highest_latency}ms\nAverage latency: {average_latency:.2f}ms\nCtrl-C to exit...")
        time.sleep(1)

def is_valid_domain(domain):
    if len(domain) > 255:
        return False
    if domain[-1] == ".":
        domain = domain[:-1]
    allowed = re.compile("(?!-)[A-Z\d-]{1,63}(?<!-)$", re.IGNORECASE)
    return all(allowed.match(x) for x in domain.split("."))

def nslookup(domain):
    if not is_valid_domain(domain):
        print(f"{domain} is not a valid domain")
        return
    try:
        ip_address = socket.gethostbyname(domain)
        print(f"{domain}: {ip_address}")
    except socket.gaierror:
        print(f"Could not resolve the domain {domain}")

while True:
    if option == 1:
        os.system("cls||clear")
        ip = input("IP:")
        os.system("cls||clear")
        print("please wait...")
        req = requests.get(f"http://ipwhois.app/json/{ip}")
        response = req.json()
        os.system("cls||clear")
        print("IP:             ", response["ip"])
        print("ISP:            ", response["isp"])
        print("Orginization:   ", response["org"])
        print("Country:        ", response["country"])
        print("Region:         ", response["region"])
        print("City:           ", response["city"])
        print("Latitude:       ", response["latitude"])
        print("Longitude:      ", response["longitude"])
        print("Type:           ", response["type"])
        input("Press Enter to continue...")
        os.system("cls||clear")
        option = int(input(msg))
    if option == 2:
        os.system("cls||clear")
        URL = input("URL:")
        os.system("cls||clear")
        print("please wait...")
        req = requests.get(f"http://ipwhois.app/json/{URL}")
        response = req.json()
        os.system("cls||clear")
        print("IP:             ", response["ip"])
        print("ISP:            ", response["isp"])
        print("Orginization:   ", response["org"])
        print("Country:        ", response["country"])
        print("Region:         ", response["region"])
        print("City:           ", response["city"])
        print("Latitude:       ", response["latitude"])
        print("Longitude:      ", response["longitude"])
        print("Type:           ", response["type"])
        input("Press Enter to continue...")
        os.system("cls||clear")
        option = int(input(msg))
    if option == 3:
        os.system("cls||clear")
        print("Please wait...")
        req = requests.get(f"http://ipwhois.app/json/")
        response = req.json()
        os.system("cls||clear")
        print("IP:             ", response["ip"])
        print("ISP:            ", response["isp"])
        print("Orginization:   ", response["org"])
        print("Country:        ", response["country"])
        print("Region:         ", response["region"])
        print("City:           ", response["city"])
        print("Latitude:       ", response["latitude"])
        print("Longitude:      ", response["longitude"])
        print("Type:           ", response["type"])
        input("Press Enter to continue...")
        os.system("cls||clear")
        option = int(input(msg))
    if option == 4:
        os.system("cls||clear")
        ip = input("Enter an IP address: ")
        try:
            ipaddress.ip_address(ip)
        except ValueError:
            print("Invalid IP address")
        else:
            try:
                ping(ip)
            except KeyboardInterrupt:
                print("\nExiting program")
                os.system("cls||clear")
                option = int(input(msg))
    if option == 5:
        os.system("cls||clear")
        domain = input("Enter a domain: ")
        os.system("cls||clear")
        nslookup(domain)
        input("Press Enter to continue...")
        os.system("cls||clear")
        option = int(input(msg))
    if option == 0:
        os.system("cls||clear")
        break