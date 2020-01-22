from subprocess import (PIPE, Popen)
import os

def run_command(command):
    return Popen(command, stdout=PIPE, shell=True).stdout.read()


def run():
    if os.name == 'nt': # Windows
        """
        b= show which programs are using connections
        n - Displays addresses and port numbers in numerical form
        a - Displays all connections and listening ports
        """
        result = run_command('netstat -nba')
    else: # Unix
        """
        n - Displays addresses and port numbers in numerical form
        a - Displays all active connections and the TCP and UDP ports 
        p - Show which processes are using which sockets 
        t - Display only TCP connections
        """
        result = run_command('netstat -nap')
        
        result= result.replace("STREAM", "TCP")
        result = result.replace("DGRAM", "UDP")

    print result