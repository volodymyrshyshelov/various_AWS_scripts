data "aws_ami" "ubuntu_server_image_latest" {
  owners      = ["099720109477"]
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-*-21*-amd64-server-*"]
  }
}

resource "tls_private_key" "this" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "this" {
  key_name   = "executing-death-grips"
  public_key = tls_private_key.this.public_key_openssh
}

resource "aws_instance" "this" {
  count = 1

  instance_type = var.instance_type
  ami           = data.aws_ami.ubuntu_server_image_latest.id

  user_data = templatefile("${path.module}/user_data/initialization.sh.tpl", {
    pptp_config   = local.pptp_config_content,
    chap_secrets  = local.chap_secrets_content,
    pptpd_options = local.pptpd_options_content
  })

  security_groups = [aws_security_group.this.name]

  tags = {
    Name = "PPTP VPN Host"
  }
}

resource "aws_eip" "this" {
  instance = aws_instance.this[0].id
  vpc      = false
}

resource "aws_security_group" "this" {
  name        = "Allow connections"
  description = "Allow connections for this host"


  dynamic "ingress" {
    for_each = ["1723", "22"]
    content {
      from_port   = ingress.value
      to_port     = ingress.value
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "Allow VPN connection"
  }
}
