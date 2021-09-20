"""
    Copyright 2021-present real-supreme

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import concurrent.futures
import sys
import time
from concurrent.futures import ThreadPoolExecutor as executor

import termcolor as tc

import data.portscan, data.vulnerable, data.bruteforce
from resources.graphics import _ascii
from terminal import clear_terminal_screen

if __name__ == "__main__":
    clear_terminal_screen()
    print(_ascii)
    targets = str(input("Enter Targets [Separate using ,]: ")).split(",")
    if targets is None:
        print("Where's the target?!")
        sys.exit()
    ports = input("Port Range to scan separated by comma: [Press Enter to skip]")
    if ports is None:
        ports = (1, 100)
    else:
        ports = tuple(ports.split(","))

    try:
        passwords = open("passwords.txt").readlines()
    except FileNotFoundError:
        passwords = ["password"]
    t1 = time.perf_counter()
    with executor() as ex:
        port_res = [
            ex.submit(portscan.portscanner(ports).scan, tar.strip()) for tar in targets
        ]
        print(port_res)
        # for r in concurrent.futures.as_completed(port_res):
        def result_iterator(r):
            bans, ports, tar = r.result()
            bans = vulnerable.vulnerable(bans).match_banners()  # Yielded List
            print(next(bans), ports, tar)

            def password_iterator(password: str):
                password = password.replace("\n", "")
                # print("Brute Force Executions")
                brute_codes = bruteforce.bruteforce(
                    host=tar, password=password, ports=ports
                ).ssh_connector()
                # print(f"Brute Force Val = {brute_codes}\n{type(brute_codes)}")
                for brute_code in brute_codes:
                    if brute_code == 0:
                        resp = str(
                            "\nPassword: "
                            + tc.colored(password, "green")
                            + f"\nHost: {tar}"
                        )
                    elif brute_code < 0:
                        resp = str(tc.colored("Server Error!", "red"))
                    else:
                        resp = str(
                            "\nPassword: "
                            + tc.colored(password, "magneta")
                            + f"\nHost: {tar}"
                        )
                    print(resp)

            try:
                passes = open("passwords.txt").readlines()
            except FileNotFoundError:
                passes = ["password", "passes"]
            print(ex.map(password_iterator, passes))

        ex.map(result_iterator, concurrent.futures.as_completed(port_res))
    t2 = time.perf_counter()
    print("Program finished in " + str(t2 - t1) + " seconds")
