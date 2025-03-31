# AWS-terraform-vpn

## Overview

**AWS-terraform-vpn** is a set of Terraform modules designed to deploy different VPN server configurations in AWS. This collection allows users to quickly and efficiently set up VPN servers for secure remote access to AWS resources.

## Table of Contents

- [AWS-terraform-vpn](#aws-terraform-vpn)
  - [Overview](#overview)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Supported VPN Types](#supported-vpn-types)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
    - [Deploying a VPN Server](#deploying-a-vpn-server)
    - [Destroying the VPN Server](#destroying-the-vpn-server)
  - [Configuration](#configuration)
  - [Outputs](#outputs)
  - [Security Considerations](#security-considerations)
  - [Contributing](#contributing)
  - [License](#license)

## Features

- **Modular structure**: Each VPN server type is a standalone module that can be used independently.
- **Automated provisioning**: Deploys VPN instances with predefined security settings.
- **Scalability**: Supports multiple VPN configurations tailored to various use cases.
- **Infrastructure as Code (IaC)**: Fully managed with Terraform for repeatability and version control.

## Supported VPN Types

The following VPN configurations are available in this collection:

- **PPTP VPN**: A legacy VPN protocol that is simple to set up but offers weaker security.
- **WireGuard VPN**: A modern, fast, and highly secure VPN solution.

Each VPN type has its own Terraform module with customizable parameters.

## Prerequisites

Before deploying a VPN server, ensure you have the following:

- An AWS account with the necessary IAM permissions.
- [Terraform](https://www.terraform.io/downloads.html) version 1.0.0 or higher.
- AWS CLI configured with credentials (`aws configure`).
- SSH key pair for accessing deployed EC2 instances.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/.git
   cd terraform-aws-vpn-collection
   ```

2. **Navigate to the desired VPN module:**
   ```bash
   cd wireguard_vpn  # or cd pptp_vpn
   ```

3. **Initialize Terraform:**
   ```bash
   terraform init
   ```

## Usage

### Deploying a VPN Server

1. **Create a Terraform plan:**
   ```bash
   terraform plan
   ```

2. **Apply the configuration:**
   ```bash
   terraform apply
   ```
   Confirm the deployment when prompted by typing `yes`.

3. **Retrieve the VPN server details:**
   ```bash
   terraform output
   ```

### Destroying the VPN Server

To remove all resources created by Terraform:
   ```bash
   terraform destroy
   ```

## Configuration

Each module provides several configuration options through Terraform variables. Below is an example of a WireGuard VPN configuration in a Terraform `.tfvars` file:

```hcl
aws_region = "us-east-1"
instance_type = "t3.micro"
vpn_port = 51820
allowed_ips = "0.0.0.0/0"
```

To apply custom settings, create a `terraform.tfvars` file in the module directory and modify the parameters as needed.

## Outputs

Once the deployment is complete, Terraform provides useful output variables, such as:

- **VPN Server Public IP**: The public IP address of the deployed VPN server.
- **Client Configuration File**: A script or file containing connection details.

To see outputs, run:
```bash
terraform output
```

## Security Considerations

- **Use Security Groups**: Ensure only required IPs have access to the VPN ports.
- **Regularly Update Software**: Keep the VPN server updated with security patches.
- **Monitor Logs**: Check AWS CloudWatch logs for any suspicious activity.
- **Restrict SSH Access**: Use key-based authentication and limit SSH access to trusted sources.

## Contributing

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

