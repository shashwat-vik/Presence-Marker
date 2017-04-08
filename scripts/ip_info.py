import socket

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

fqa = "http://{0}/{1}/create_sheet".format(get_ip_address(), '982aeace73ed943e80b408b12e816f2b')

print ("\n{0}\n".format('='*len(fqa)))
print (fqa)
print ("\n{0}\n".format('='*len(fqa)))
