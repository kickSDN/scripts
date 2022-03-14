#!/usr/bin/python

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
    h1 = net.addHost( 'h1', mac='00:00:00:00:00:01', ip='10.0.0.1/8' )
    c2 = net.addController( 'c2', controller=RemoteController, ip='127.0.0.1', port=6633 )
    s3 = net.addSwitch( 's3', listenPort=6634, mac='00:00:00:00:00:03' )
    h4 = net.addHost( 'h4', mac='00:00:00:00:00:04', ip='10.0.0.4/8' )

    print "*** Creating links"
    net.addLink(h4, s3, 0, 2)
    net.addLink(h1, s3, 0, 1)

    print "*** Starting network"
    net.build()
    s3.start( [c2] )
    c2.start()

    print "*** Running CLI"
    CLI( net )

    print "*** Stopping network"
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    topology()

