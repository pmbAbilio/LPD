import re
import geoip2.database


class Reader:
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
        reader = geoip2.database.Reader("./GeoLite2-Country.mmdb")

        returnData = reader.country(ip)
        return returnData.country.name

    # This functio will parse the log files, returning the ips and the corresponding location
    def ip_parser(self):
        file = open("auth.log")
        file = file.readlines()
        ips = []
        dates = []
        for line in file:
            # ips_temp = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)
            if re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line):
                print(
                    "Connection attempt from {}".format(
                        self.getCountry(
                            re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", line)[
                                0
                            ]
                        )
                    )
                )
                # print(line)
                # dates.append(line)
                # for d in dates:
                # dates_temp = re.findall(r"\b\d{1,2}\:\d{1,2}\:\d{1,2}\b", d)[0]
                # print(dates_temp)
                """ for ip in ips_temp:
                    if ip not in ips:
                        ips.append(ip)
                        print(ip) """


tester = Reader()
tester.ip_parser()
