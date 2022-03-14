#!/usr/bin/python
"""
#Script created by VND - Visual Network Description (SDN version) 
"""
from pox.core import core
from pox.lib.addresses import IPAddr
from pox.lib.addresses import EthAddr
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

#flow1: 
switch0 = 000000000000003
flow0msg = of.ofp_flow_mod() 
flow0msg.cookie = 0 
flow0msg.match.in_port = 1
# ACTIONS---------------------------------
flow0out = of.ofp_action_output (port = 2)
flow0msg.actions = [flow0out] 

#flow2: 
switch1 = 000000000000003
flow1msg = of.ofp_flow_mod() 
flow1msg.cookie = 0 
flow1msg.match.in_port = 2
# ACTIONS---------------------------------
flow1out = of.ofp_action_output (port = 1)
flow1msg.actions = [flow1out] 

def install_flows(): 
   log.info("    *** Installing static flows... ***")
   # Push flows to switches
   core.openflow.sendToDPID(switch0, flow0msg)
   core.openflow.sendToDPID(switch1, flow1msg)
   log.info("    *** Static flows installed. ***")

def launch (): 
   log.info("*** Starting... ***")
   core.callDelayed (15, install_flows)
   log.info("*** Waiting for switches to connect.. ***")
