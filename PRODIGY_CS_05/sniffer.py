from scapy.all import sniff

def packet_details(packet):
    if packet.haslayer('IP'):
        source_ip = packet['IP'].src
        destination_ip = packet['IP'].dst
        protocol = packet['IP'].proto

        print(f"Source IP addr: {source_ip}\tDestination IP addr: {destination_ip}\tProtocol:{protocol}")

sniff(prn = packet_details)