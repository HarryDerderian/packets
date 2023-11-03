import scapy.all as scapy

if __name__ == "__main__" :
    # Targeted IP... aka ourself, don't want any legal trouble.
    LOCAL_HOST_IP = "127.0.0.1"
    
    # FLAGS (commands our packet will send out)
    cmd_2_flag = {"SYN" : "S"}
    target_port = 21 # (SSH)
    # Transmission Control Protocol
    TCP = scapy.TCP(dport = target_port, flags = cmd_2_flag["SYN"])
    TARGET_IP = scapy.IP(dst = LOCAL_HOST_IP)
    # Merge the above with '/' this will create a complete packet.
    packet = scapy.IP(dst = LOCAL_HOST_IP) / TCP
    try :
        # Send out the packet, wait for a response.
        response = scapy.sr1(packet)
        print(str(response))
        print("END PROGRAM")
    except :
        print("MUST RUN AS ADMINISTRATOR")
        print("Program requires to be ran as admin.")