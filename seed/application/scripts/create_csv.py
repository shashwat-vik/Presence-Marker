import csv, socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def attendance_csv(filename, sem, branch, sect, period, start_roll, end_roll, present_rolls):
    f = open(filename, 'w', newline='')
    csvwriter = csv.writer(f)

    fields = ['SEMESTER', 'BRANCH', 'SECTION', 'PERIOD']
    args = [[sem, ''], [branch, ''], [sect, ''], [period, '']]
    csvwriter.writerow(fields)

    rows = zip(args[0], args[1], args[2], args[3])
    for row in rows:
        csvwriter.writerow(row)

    pres = lambda x: 'P' if x else ''

    fields = ['ROLE', 'STATUS']
    csvwriter.writerow(fields)
    args = [[], []]
    for i in range(start_roll, end_roll+1):
        csvwriter.writerow([i, pres(i in present_rolls)])
    f.close()

def ip_role_csv(filename, client_data):
    f = open(filename, 'w', newline='')
    csvwriter = csv.writer(f)

    fields = ['IP', 'ROLE']
    csvwriter.writerow(fields)

    for ip, role in client_data:
        if ip == '::1':
            ip = get_ip_address()
        csvwriter.writerow([ip, role])
    f.close()

def dhcp_tp_link_csv(filename, client_data, ip_mac):
    f = open(filename, 'w', newline='')
    csvwriter = csv.writer(f)

    fields = ['ROLE', 'IP', 'MAC', 'NAME']
    csvwriter.writerow(fields)

    for ip, role in client_data:
        row = []
        if ip == '::1':
            ip = get_ip_address()
        row.append(role)
        row.append(ip)
        x = ip_mac.get(ip)
        if x:
            row.append(x[0])
            row.append(x[1])
        else:
            row.append('')
            row.append('')
        csvwriter.writerow(row)

    f.close()
#write_data('a.csv', 6, 'IT', 'B', 1, 20, 40, {20, 25, 30, 35, 40})
