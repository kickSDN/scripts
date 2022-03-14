
"""
Script created by VND - Visual Network Description (SDN version)
"""
from mininet.net import Mininet
from mininet.node import Controller, RemoteController, OVSKernelSwitch, OVSLegacyKernelSwitch, UserSwitch
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import Link, TCLink

def topology():
    "Create a network."
    net = Mininet( controller=RemoteController, link=TCLink, switch=OVSKernelSwitch )

    print "*** Creating nodes"
    c1 = net.addController( 'c1', controller=RemoteController, ip='127.0.0.1', port=6633 )
    s1 = net.addSwitch( 's1', listenPort=6634, mac='00:00:00:00:00:01' )
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:03', ip='192.168.10.11/24' )
    h2 = net.addHost( 'h2', mac='00:00:00:00:00:04', ip='192.168.50.11/24' )

    print "*** Creating links"
    net.addLink(h1, s1, 0, 2)
    net.addLink(h2, s1, 0, 1)

    print "*** Starting network"
    net.build()
    s1.start( [c1] )
    c1.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

