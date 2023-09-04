def cidr(cidr_notation):
   # Convert the CIDR notation string to an IP address and subnet mask
   ip_str, mask_str = cidr_notation.split('/')
   octets = ip_str.split('.')
   ip_int = (int(octets[0]) << 24) + (int(octets[1]) << 16) + (int(octets[2]) << 8) + int(octets[3])
   mask_int = int(mask_str)
   mask = (0xffffffff << (32 - mask_int)) & 0xffffffff

   # Calculate the network address and broadcast address
   network = (ip_int & mask)
   broadcast = (ip_int | (~mask & 0xffffffff))

   # Convert the IP address integers back to strings and return the result
   network_str = '.'.join([str((network >> i) & 0xff) for i in (24, 16, 8, 0)])
   broadcast_str = '.'.join([str((broadcast >> i) & 0xff) for i in (24, 16, 8, 0)])

   return f"{network_str} - {broadcast_str}"

Inetnum = input('What is the inetnum? ')
Netname = input('What is the netname e.g GitHub ')
Descr = input('What is the descr e.g Tech GitHub LTD? ')
if '/' in Inetnum:
    print ('inetnum:         ' + cidr(Inetnum),
       '\nnetname:         ' + Netname.replace(" ","-").upper(),
       '\ndescr:           ' + Descr.upper(),
       '\ncountry:         GB',
       '\nadmin-c:         GSOC-RIPE',
       '\ntech-c:          GSOC-RIPE',
       '\nstatus:          ASSIGNED PA',
       '\nmnt-by:          EUROPE-GSOC',
       '\nsource:          RIPE')
elif '-' in Inetnum:
    print ('inetnum:         ' + Inetnum,
       '\nnetname:         ' + Netname.upper(),
       '\ndescr:           ' + Descr.upper(),
       '\ncountry:         GB',
       '\nadmin-c:         GSOC-RIPE',
       '\ntech-c:          GSOC-RIPE',
       '\nstatus:          ASSIGNED PA',
       '\nmnt-by:          EUROPE-GSOC',
       '\nsource:          RIPE')
else:
    print('Error: Double check Inetnum')