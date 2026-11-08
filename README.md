# Network Security Lab

## Snort ICMP Alert Setup

Check the installed Snort version:

```bash
snort -V
```

Edit the Snort configuration:

```bash
sudo nano /etc/snort/snort.conf
```

Set the network variables:

```conf
ipvar HOME_NET any
ipvar EXTERNAL_NET any
```

Add a local ICMP alert rule:

```bash
sudo nano /etc/snort/rules/local.rules
```

Add this rule to the file:

```conf
alert icmp any any -> any any (msg:"ICMP Packet Detected"; sid:1000001; rev:1;)
```

Validate the configuration:

```bash
sudo snort -T -c /etc/snort/snort.conf
```

Inspect the available interfaces and routes:

```bash
ip a
ip route
```

Run Snort in console mode on `eth0`:

```bash
sudo snort -A console -q -c /etc/snort/snort.conf -i eth0
```

In another terminal, generate an ICMP packet:

```bash
ping 127.0.0.1
```
