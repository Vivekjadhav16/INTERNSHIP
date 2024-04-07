import pyshark

def packet_sniffer(interface, count=10):
    capture = pyshark.LiveCapture(interface=interface)

    print("Packet Sniffing started on interface:", interface)

    try:
        for packet in capture.sniff_continuously(packet_count=count):
            src_ip = packet.ip.src
            dst_ip = packet.ip.dst
            protocol = packet.transport_layer
            payload = packet.data.data

            print("Source IP:", src_ip)
            print("Destination IP:", dst_ip)
            print("Protocol:", protocol)
            if payload:
                print("Payload:", payload)

            count -= 1
            if count == 0:
                break

    except KeyboardInterrupt:
        print("Packet Sniffing stopped.")

if __name__ == "__main__":
    interface = input("Enter the interface to sniff (e.g., eth0): ")
    packet_sniffer(interface)
