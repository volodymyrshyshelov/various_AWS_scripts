#!/bin/bash

# Install required dependencies

sudo apt update
sudo apt install pptpd -y

# Write configuration

echo -e "${pptp_config}" >> /etc/pptpd.conf
echo -e "${chap_secrets}" >> /etc/ppp/chap-secrets
echo -e "${pptpd_options}" >> /etc/ppp/pptpd-options

# Restart pptpd

sudo service pptpd restart

# Enable IP forwarding

sysctl -w net.ipv4.ip_forward=1

sudo iptables -t nat -A POSTROUTING -o eth0 -j MASQUERADE && iptables-save
