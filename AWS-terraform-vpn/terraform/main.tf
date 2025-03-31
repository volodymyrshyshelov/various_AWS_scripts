module "pptp_vpn" {
  source = "../pptp_vpn"

  // Cloud options
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key


  // PPTP server configuration
  vpn_client_name     = "Artefall"
  vpn_client_password = "12345678"
}







