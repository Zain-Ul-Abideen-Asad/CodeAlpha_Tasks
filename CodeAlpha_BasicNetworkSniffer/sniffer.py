from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw

def packet_analyzer(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n==============================")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        if packet.haslayer(TCP):
            print("Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol       : ICMP")

        else:
            print(f"Protocol       : Other ({protocol})")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"Payload        : {payload[:50]}")

print("Starting Network Sniffer...")
sniff(prn=packet_analyzer, store=False)
