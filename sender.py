# SENDER

import socket

# group = '224.1.1.1'
# port = 5004

group = '224.0.0.251'
port = 5353

# 2-hop restriction in network
ttl = 255

redirect_to = '192.168.10.9'

# print(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM,
                     socket.IPPROTO_UDP)
# print('packet',(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl))


# sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, ttl)

sock.bind((redirect_to,5353))



uuid_fn = ['a56831aa-ef2a-1db0-9c3f-d6b56ff217fa','736d6172745f7476']
uuid = uuid_fn[0]
fn = uuid_fn[1]

fn_len = len(fn)//2
a = redirect_to.split('.')
hex_ip = '{:02X}{:02X}{:02X}{:02X}'.format(*map(int, a))
uuid_nodash = ''.join(uuid.split('-'))

print("UUID NODE DASH : ",uuid_nodash.encode('ascii').hex() )

# Query
# ans = '00 00 00 00 00 01 00 00 00 00 00 00 0b 5f 67 6f 6f 67 6c 65 63 61 73 74 04 5f 74 63 70 05 6c 6f 63 61 6c 00 00 0c 00 01'

# response
# Full packet

# ans = '01 00 5e 00 00 fb 20 9b e6 0f 89 92 08 00 45 00 01 7a a6 43 40 00 ff 11 28 80 c0 a8 0a 0b e0 00 00 fb 14 e9 14 e9 01 66 58 c4 00 00 84 00 00 00 00 01 00 00 00 03 0b 5f 67 6f 6f 67 6c 65 63 61 73 74 04 5f 74 63 70 05 6c 6f 63 61 6c 00 00 0c 00 01 00 00 00 78 00 31 2e 53 6d 61 72 74 2d 32 4b 2d 41 54 56 34 2d 61 35 36 38 33 31 61 61 65 66 32 61 31 64 62 30 39 63 33 66 64 36 62 35 36 66 66 32 31 37 66 61 c0 0c c0 2e 00 10 80 01 00 00 11 94 00 aa 23 69 64 3d 61 35 36 38 33 31 61 61 65 66 32 61 31 64 62 30 39 63 33 66 64 36 62 35 36 66 66 32 31 37 66 61 23 63 64 3d 38 37 46 45 35 31 42 36 34 41 45 39 45 46 32 34 46 33 44 46 45 32 43 32 30 38 32 44 37 42 46 30 03 72 6d 3d 05 76 65 3d 30 35 10 6d 64 3d 53 6d 61 72 74 20 32 4b 20 41 54 56 34 12 69 63 3d 2f 73 65 74 75 70 2f 69 63 6f 6e 2e 70 6e 67 0b 66 6e 3d 73 6d 61 72 74 5f 74 76 09 63 61 3d 34 36 31 33 31 37 04 73 74 3d 30 0f 62 73 3d 46 41 38 46 37 30 46 35 41 41 32 37 04 6e 66 3d 31 03 72 73 3d c0 2e 00 21 80 01 00 00 00 78 00 2d 00 00 00 00 1f 49 24 61 35 36 38 33 31 61 61 2d 65 66 32 61 2d 31 64 62 30 2d 39 63 33 66 2d 64 36 62 35 36 66 66 32 31 37 66 61 c0 1d c1 27 00 01 80 01 00 00 00 78 00 04 c0 a8 0a 0b'

# mdns only
ans = '00 00 84 00 00 00 00 01 00 00 00 03 09 5f 32 33 33 36 33 37 44 45 04 5f 73 75 62 0b 5f 67 6f 6f 67 6c 65 63 61 73 74 04 5f 74 63 70 05 6c 6f 63 61 6c 00 00 0c 00 01 00 00 00 78 00 31 2e 53 6d 61 72 74 2d 32 4b 2d 41 54 56 34 2d 61 35 36 38 33 31 61 61 65 66 32 61 31 64 62 30 39 63 33 66 64 36 62 35 36 66 66 32 31 37 66 61 c0 1b c0 3d 00 10 80 01 00 00 11 94 00 aa 23 69 64 3d 61 35 36 38 33 31 61 61 65 66 32 61 31 64 62 30 39 63 33 66 64 36 62 35 36 66 66 32 31 37 66 61 23 63 64 3d 38 37 46 45 35 31 42 36 34 41 45 39 45 46 32 34 46 33 44 46 45 32 43 32 30 38 32 44 37 42 46 30 03 72 6d 3d 05 76 65 3d 30 35 10 6d 64 3d 53 6d 61 72 74 20 32 4b 20 41 54 56 34 12 69 63 3d 2f 73 65 74 75 70 2f 69 63 6f 6e 2e 70 6e 67 0b 66 6e 3d 73 6d 61 72 74 5f 74 76 09 63 61 3d 34 36 31 33 31 37 04 73 74 3d 30 0f 62 73 3d 46 41 38 46 37 30 46 35 41 41 32 37 04 6e 66 3d 31 03 72 73 3d c0 3d 00 21 80 01 00 00 00 78 00 2d 00 00 00 00 1f 49 24 61 35 36 38 33 31 61 61 2d 65 66 32 61 2d 31 64 62 30 2d 39 63 33 66 2d 64 36 62 35 36 66 66 32 31 37 66 61 c0 2c c1 36 00 01 80 01 00 00 00 78 00 04 c0 a8 0a 0b'

data_list = ans #.split()
data_hex = bytes.fromhex(''.join(data_list))
print(data_hex)

sock.sendto(data_hex,(group,port))

#sock.sendto(b"hello world", (group, port))
#sock.sendto(b'E\x00\x01z\x00\x01\x00\x00\xff\x11\x0e\xc6\xc0\xa8\n\x08\xe0\x00\x00\xfb\x14\xe9\x14\xe9\x01fgm\x00\x00\x84\x00\x00\x00\x00\x04\x00\x00\x00\x00\x0b_googlecast\x04_tcp\x05local\x00\x00\x0c\x00\x01\x00\x00\x00x\x001.Smart-2K-ATV4-a56831aaef2a1db09c3fd6b56ff217fa\xc0\x0c$a56831aa-ef2a-1db0-9c3f-d6b56ff217fa\xc0\x1d\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\x148\xc0.\x00!\x80\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\x1fI\xc0_\xc0.\x00\x10\x80\x01\x00\x00\x11\x94\x00\xaa#id=a56831aaef2a1db09c3fd6b56ff217fa#cd=87FE51B64AE9EF24F3DFE2C2082D7BF0\x03rm=\x05ve=05\x10md=Smart 2K ATV4\x12ic=/setup/icon.png\x0bfn=smart_tv\tca=461317\x04st=0\x0fbs=FA8F70F5AA27\x04nf=3\x03rs=', (group, port))

#QUERY
    #SMART
# sock.sendto(b'\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x000smart-2k-atv4-a56831aaef2a1db09c3fd6b56ff217fa-3\x0b_googlecast\x04_tcp\x05local\x00\x00!\x00\x01',(group,port))

    #RIPL
#sock.sendto(b'\x00\x00\x00\x00\x00\x03\x00\x00\x00\x03\x00\x00\x08ripl_tv1\x11_androidtvremote2\x04_tcp\x05local\x00\x00\xff\x80\x01\x07Android\xc0,\x00\xff\x80\x01\xc07\x00\xff\x80\x01\xc0\x0c\x00!\x00\x01\x00\x00\x00x\x00\x08\x00\x00\x00\x00\x19B\xc07\xc07\x00\x01\x00\x01\x00\x00\x00x\x00\x04\xc0\xa8\n\r\xc07\x00\x1c\x00\x01\x00\x00\x00x\x00\x10\xfe\x80\x00\x00\x00\x00\x00\x00\x82\xcb\xbc\xff\xfe\xf0D\x1a',(group,port))

# RESPONSE
#sock.sendto(b'\x00\x00\x84\x00\x00\x00\x00\x01\x00\x00\x00\x03\x0b_googlecast\x04_tcp\x05local\x00\x00\x0c\x00\x01\x00\x00\x00x\x0030Smart-2K-ATV4-a56831aaef2a1db09c3fd6b56ff217fa-3\xc0\x0c\xc0.\x00\x10\x80\x01\x00\x00\x11\x94\x00\xaa#id=a56831aaef2a1db09c3fd6b56ff217fa#cd=87FE51B64AE9EF24F3DFE2C2082D7BF0\x03rm=\x05ve=05\x10md=Smart 2K ATV4\x12ic=/setup/icon.png\x0bfn=smart_tv\tca=461317\x04st=0\x0fbs=FA8F70F5AA27\x04nf=1\x03rs=\xc0.\x00!\x80\x01\x00\x00\x00x\x00-\x00\x00\x00\x00\x1fI$a56831aa-ef2a-1db0-9c3f-d6b56ff217fa\xc0\x1d\xc1)\x00\x01\x80\x01\x00\x00\x00x\x00\x04\xc0\xa8\n\x0b',(group,port))