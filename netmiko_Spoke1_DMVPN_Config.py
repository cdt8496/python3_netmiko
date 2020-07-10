from netmiko import ConnectHandler

IOSv = {
    'device_type':'cisco_ios',
    'ip':'172.16.175.72',
    'username':'cisco',
    'password':'cisco',
}

net_connect = ConnectHandler(**IOSv)

config_commands = ['int loop 2','ip address 2.2.2.2 255.255.255.255']
output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['int tunnel 2','ip address 10.10.0.2 255.255.255.0',
                   'no ip redirects','ip mtu 1400','ip nhrp authentication cisco123',
		   'ip nhrp map multicast 200.1.2.2','ip nhrp map 10.10.0.1 200.1.1.1',
		   'ip nhrp network-id 2','ip nhrp nhs 10.10.0.1','ip nhrp shortcut',
		   'ip tcp adjust-mss 1360','tunnel source 200.1.2.2',
		   'tunnel destination 200.1.1.1']

output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['router eigrp CHARLES','address-family ipv4 unicast autonomous-system 5',
                   'af-interface default','passive-interface','af-interface tunnel 2',
		   'no passive-interface','network 10.10.0.2 255.255.255.255',
		   'network 2.2.2.2 255.255.255.255']

output = net_connect.send_config_set(config_commands)
print(output)

config_commands = ['ip route 200.1.1.1 255.255.255.255 200.1.2.10',
                   'ip route 200.1.3.3 255.255.255.255 200.1.2.10']

output = net_connect.send_config_set(config_commands)
print(output)
