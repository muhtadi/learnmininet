#!/usr/bin/python3

from mininet.topo import Topo
from mininet.net import Mininet
from mininet.util import dumpNodeConnections
from mininet.cli import CLI


class part1_topo(Topo):
    def build(self):
        
        # switch1 = self.addSwitch('switchname')
        switch = self.addSwitch('switch1')
        # host1 = self.addHost('hostname')
        host = self.addHost('host1')
        host = self.addHost('host2')
        host = self.addHost('host3')
        host = self.addHost('host4')
        # self.addLink(hostname,switchname)
        self.addLink(host, switch)


topos = {"part1": part1_topo}

if __name__ == "__main__":
    t = part1_topo()
    net = Mininet(topo=t)
    net.start()
    CLI(net)
    net.stop()
