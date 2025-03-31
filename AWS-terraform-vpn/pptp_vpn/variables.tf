# Cloud configuration

variable "region" {
  type        = string
  default     = "us-west-1"
  description = "Place where VPN will be deployed"
}

variable "instance_type" {
  type        = string
  default     = "t2.micro"
  description = "Instance type for server"
}

variable "access_key" {
  type        = string
  description = "Cloud access key"
  sensitive   = true
}

variable "secret_key" {
  type        = string
  description = "Cloud secret key"
  sensitive   = true
}

# Configuration of chap-secrets file

variable "vpn_client_name" {
  type        = string
  description = "Login name of VPN user"
}

variable "vpn_client_password" {
  type        = string
  description = "Password of VPN user"
  sensitive   = true
}

variable "allowed_ip_address" {
  type        = string
  description = "Allowed IP addresses to connect from"
  default     = "*"
}

# Configuration of pptpd.conf file

variable "local_ip" {
  type        = string
  description = "Local PPTP VPN IP address"
  default     = "192.168.84.1"
}

variable "remote_ip_range" {
  type        = string
  description = "IP address pool, PPTPD will assign IP to users from"
  default     = "192.168.84.100-200"
}

# Configuration of pptpd options file

variable "primary_dns" {
  type        = string
  description = "PPTPD primary DNS"
  default     = "8.8.8.8"
}

variable "secondary_dns" {
  type        = string
  description = "PPTPD secondary dns"
  default     = "8.8.4.4"
}

locals {
  pptp_config_content = templatefile("${path.module}/user_data/pptpd.conf.tpl", {
    local_ip  = var.local_ip,
    remote_ip = var.remote_ip_range
  })

  chap_secrets_content = templatefile("${path.module}/user_data/chap-secrets.tpl", {
    vpn_client_name     = var.vpn_client_name,
    vpn_client_password = var.vpn_client_password,
    allowed_ip_address  = var.allowed_ip_address
  })

  pptpd_options_content = templatefile("${path.module}/user_data/pptpd-options.tpl", {
    primary_dns   = var.primary_dns,
    secondary_dns = var.secondary_dns
  })
}