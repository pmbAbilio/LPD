import re
import geoip2.database
from DatabaseHandler import DatabaseHandler
import matplotlib.pyplot as plt
import numpy as np


class Reader:
    def __init__(self):
        self.dbh = DatabaseHandler()
        self.authLogFile = "../logFiles/auth.log"
        self.ufwLogFile = "../logFiles/ufw.log"

    def find_str(self, s, char):
        index = 0

        if char in s:
            c = char[0]
            for ch in s:
                if ch == c:
                    if s[index : index + len(char)] == char:
                        return index

                index += 1

        return -1

    # Function that will get the country of origin of the ip
    def getCountry(self, ip):
        try:
            reader = geoip2.database.Reader("../GeoLiteFiles/GeoLite2-Country.mmdb")
            returnData = reader.country(ip)
            return returnData.country.name
        except:
            print("An exception occured")

    def logTypeSelector(self):
        self.sshParser()
        self.ufwParser()

    def ufwParser(self):
        file = open(self.ufwLogFile)
        file = file.readlines()
        for line in file:
            if ("UFW BLOCK" in line) and ("DPT" in line):
                IpsFound = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)

                self.dbh.insertData(
                    [
                        line[0:16],
                        IpsFound[0],
                        self.getCountry(IpsFound[0]),
                        "Blocked Connection Attempt on PORT: {}".format(
                            line[
                                line.find("DPT=")
                                + len("DPT=") : line.find("DPT=")
                                + len("DPT=")
                                + 10
                            ].split(" ")[0]
                        ),
                    ]
                )

    # This function will parse the SSH log file, returning the ips and the corresponding location
    def sshParser(self):
        file = open(self.authLogFile)
        file = file.readlines()
        ips = []
        for line in file:
            if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line):
                ipFound = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)[0]
                message = ""
                ipLocation = self.getCountry(ipFound)
                if ipFound not in "0.0.0.0":
                    if ipFound not in ips:
                        ips.append(ipFound)
                    print(
                        "Date: {} Ip: {} From {}".format(
                            line[0:16], ipFound, ipLocation
                        )
                    )
                    if "pam_unix(sshd:auth)" in line:
                        searchKeyword = "pam_unix(sshd:auth)"
                        message = line[
                            line.find(searchKeyword)
                            + len(searchKeyword)
                            + 2 : line.find(";")
                        ]
                    else:
                        message = line.split(":")[3]

                    if ipLocation is None:
                        self.dbh.insertData(
                            [line[0:15], ipFound, "Nao encontrada", message]
                        )
                    else:
                        self.dbh.insertData([line[0:14], ipFound, ipLocation, message])

    def CreatePiePlot(self):
        self.CountList = self.dbh.selectCount()
        labels = []
        sizes = []
        for row in self.CountList:
            print(row)
            labels.append(row[0])
            sizes.append(row[1])

        x = labels
        y = sizes
        colors = [
            "yellowgreen",
            "red",
            "gold",
            "lightskyblue",
            "lightcoral",
            "darkgreen",
            "blue",
            "pink",
            "yellow",
            "grey",
            "violet",
            "magenta",
            "cyan",
        ]

        patches, texts = plt.pie(y, colors=colors, startangle=90, radius=1.2)
        labels = ["{0} - {1}".format(i, j) for i, j in zip(x, y)]

        sort_legend = True
        if sort_legend:
            patches, labels, dummy = zip(
                *sorted(zip(patches, labels, y), key=lambda x: x[2], reverse=True)
            )

        plt.legend(
            patches, labels, loc="center left", bbox_to_anchor=(-0.1, 1.0), fontsize=8
        )

        plt.savefig("Authentication Attempts.png", bbox_inches="tight")
        # plt.show()


tester = Reader()
tester.logTypeSelector()
