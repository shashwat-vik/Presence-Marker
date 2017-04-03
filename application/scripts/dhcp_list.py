import requests

def DHCP():
    url = 'http://192.168.0.1/userRpm/AssignedIpAddrListRpm.htm'
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch',
    'Accept-Language':'en-US,en;q=0.8',
    'Authorization':'Basic YWRtaW46YWRtaW5yZWJvcm4=',
    'Connection':'keep-alive',
    'Host':'192.168.0.1',
    'Referer':'http://192.168.0.1/',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }

    resp = requests.get(url, headers=headers)
    data = resp.text

    DHCPDynList = data.split("var DHCPDynList = new Array")[1].split(';\n</SCRIPT>')[0]
    DHCPDynList = DHCPDynList.replace('\n','')
    DHCPDynList = eval(DHCPDynList)

    DHCPDynPara = data.split("var DHCPDynPara = new Array")[1].split(';\n</SCRIPT>')[0]
    DHCPDynPara = DHCPDynPara.replace('\n','')
    DHCPDynPara = eval(DHCPDynPara)

    #print (repr(DHCPDynPara))
    #print (repr(DHCPDynList))

    print ("{0:<5}{3:<18}{2:<22}{1:<10}".format('ID', 'NAME', 'MAC', 'IP'))
    print("-"*56)
    for i in range(DHCPDynPara[0]):
        j = i+1
        row = i * DHCPDynPara[1]
        print("{0:<5}{3:<18}{2:<22}{1:<10}".format(j, DHCPDynList[row], DHCPDynList[row+1], DHCPDynList[row+2]))
