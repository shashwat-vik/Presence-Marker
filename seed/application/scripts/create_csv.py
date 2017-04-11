import csv, socket
from scripts.dhcp_list import DHCP

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def attendance_csv(filename, sem, branch, sect, period, periods_count, start_roll, end_roll, present_rolls, role_ip_dict):
    ip_mac_dict = dict()
    try:
        ip_mac_dict = DHCP()
    except:
        pass

    f = open(filename, 'w', newline='')
    csvwriter = csv.writer(f)

    fields = ['SEMESTER', 'BRANCH', 'SECTION']
    csvwriter.writerow(fields)

    args = [[sem, ''], [branch, ''], [sect, '']]
    rows = zip(args[0], args[1], args[2])
    for row in rows:
        csvwriter.writerow(row)

    pres = lambda x: 'P' if x else ''
    fields = ['IP', 'MAC', 'ROLE']
    fields.extend(["PERIOD {0}".format(period+i) for i in range(periods_count)])
    csvwriter.writerow(fields)

    for role in range(start_roll, end_roll+1):
        row = []
        ip, mac = None, None
        ip = role_ip_dict.get(role)
        if ip:
            if ip == '::1':
                ip = get_ip_address()
            mac = ip_mac_dict.get(ip)

        row = [ip, mac, role]
        for i in range(periods_count):
            row.append(pres(role in present_rolls))

        csvwriter.writerow(row)

    f.close()
