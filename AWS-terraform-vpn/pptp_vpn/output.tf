output "vpn_ip_address" {
  value       = aws_eip.this.public_ip
  description = "IP address of VPN service"
}

output "dns_name" {
  value       = aws_eip.this.public_dns
  description = "DNS name to connect"
}

