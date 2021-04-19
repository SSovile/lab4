import re
from datetime import datetime

result = []

pattern = r"\[(\d{2}\/\w{3}\/\d{4}:\d{2}:\d{2}:\d{2}).+\"OPTIONS"
dateformat = "%d/%b/%Y:%H:%M:%S"
begin = datetime.strptime("23/Mar/2009:03:38:17", dateformat)
end = datetime.strptime("25/Mar/2009:09:52:50", dateformat)


def main():
    counter = 0
    with open("log.txt") as file:
        probpatern = re.compile(pattern)
        for line in file:
            match = probpatern.search(line)
            # if match:
            #     datetime.strptime(match.group(1), dateformat)
            if match:
                print(str(match))
                if begin <= datetime.strptime(match.group(1), dateformat) <= end:
                    counter += 1
        print(counter)


if __name__ == '__main__':
    main()
