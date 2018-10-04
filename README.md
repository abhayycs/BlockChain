# BlockChain
Remote Software Update using BlockChain Technology
Enable the features of remote software update using block chain technology to verify the integrity of a software file uploaded by the software provider.

Create topology using mininet
terminal 1 > 
  sudo mn --topo=single,4 --link=tc,bw=1000 --controller=remote --mac
Adding flowrules to the network
terminal 2 >
  sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:01,action=output:1
  sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:02,action=output:2
  sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:03,action=output:3
  sudo ovs-ofctl add-flow s1 dl_dst=00:00:00:00:00:04,action=output:4
  sudo ovs-ofctl add-flow s1 dl_dst=ff:ff:ff:ff:ff:ff,action=flood
  watch added flow rules
  sudo ovs-ofctl dump-flows s1
terminal 1 > xterm h1 h2 h3 h4
Executes the commands in given order
x1 > cd OBMs
  python3 OBM.p
x3 > cd OEMs
  python3 OEM.py
x4 > cd Cloud
  python3 cloud.py
x2 > cd SPs
  python3 software_provider.py
