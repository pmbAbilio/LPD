from subprocess import (PIPE, Popen)
import os

def command(command):
    return Popen(command, stdout=PIPE, shell=True).stdout.read()


def start():
    if os.name == 'nt': # Windows
        result = command('netstat -nba')
    else: # Unix
        result = command('netstat -napt')
    print (result.decode("utf-8"))


