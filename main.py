import scapy.all as scapy

# My first question: What is a packet?
# Google shows: A packet is data sent over networks.
# Some key aspects of this data: Source IP, Dest IP



if __name__ == "__main__" :
        
    # Create an ICMP packet
    LOCAL_HOST_IP = "127.0.0.1"
    packet = scapy.IP( dst = LOCAL_HOST_IP) / scapy.ICMP()
                      # dst (the ip we want to send the packet to)
    
    
    
    # Send the packet
    try :
        scapy.send(packet)
    except :
        print("MUST RUN AS ADMINISTRATOR")
        print("Program requires to be ran as admin.")