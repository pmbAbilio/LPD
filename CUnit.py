import admin
import winreg
import socket
import subprocess
import platform
import sys

if platform.system() == "Windows":
    if not admin.isUserAdmin():
        # admin.runAsAdmin()
        subprocess.call("cls", shell=True)
if platform.system() == "Linux":
    subprocess.call("clear", shell=True)

if len(sys.argv) is 2:
    # print("There are {} arguments".format(len(sys.argv) - 1))
    remoteServerIP = socket.gethostbyname(sys.argv[1])
    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)
    try:
        for port in range(1, 1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	 Open".format(port))
            elif result == 10060:
                print(
                    "Oops, something went wrong, it looks like the connection to the port {} timed out".format(
                        port
                    )
                )
            else:
                print("Unknown Error code!!")
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print("Hostname could not be resolved. Exiting")
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

