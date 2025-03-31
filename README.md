# 🚀 various_AWS_scripts

**various_AWS_scripts** is a collection of powerful scripts and resources designed to simplify working with various AWS services. Whether you're deploying infrastructure, managing cloud resources, or automating tasks, this repository provides ready-to-use solutions.

## 📌 Table of Contents

- [✨ Overview](#-overview)
- [📂 Repository Structure](#-repository-structure)
- [🚀 Getting Started](#-getting-started)
- [⚙️ Prerequisites](#-prerequisites)
- [📥 Installation](#-installation)
- [📖 Usage](#-usage)
- [🤝 Contributing](#-contributing)
- [📜 License](#-license)
- [📧 Contact](#-contact)

## ✨ Overview

This repository includes various AWS-related scripts and projects, such as:

- 🔹 **AWS-terraform-vpn**: Terraform configurations for deploying a secure VPN server in AWS.
- 🔹 **AWS_S3_website**: Examples and step-by-step guides for hosting static websites on Amazon S3.
- 🔹 **AWS_delete_resources**: Automated scripts to safely delete specific AWS resources.

## 📂 Repository Structure

```
📦 various_AWS_scripts
 ┣ 📂 AWS-terraform-vpn/     # VPN deployment with Terraform
 ┣ 📂 AWS_S3_website/        # Static website hosting on S3
 ┣ 📂 AWS_delete_resources/  # AWS resource cleanup scripts
 ┣ 📜 LICENSE               # Project license
 ┗ 📜 README.md             # Documentation file
```

## 🚀 Getting Started

Follow these steps to set up and start using this repository.

### ⚙️ Prerequisites

Ensure you have the following installed before proceeding:

- 🛠️ [Terraform](https://www.terraform.io/downloads.html) - for infrastructure automation
- 🌍 [AWS CLI](https://aws.amazon.com/cli/) - for AWS service interaction
- 🔑 AWS account with the required permissions
- 🏗️ Configured AWS credentials on your local machine

### 📥 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/volodymyrshyshelov/various_AWS_scripts.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd various_AWS_scripts
   ```

## 📖 Usage

Each subdirectory contains a specific project or set of scripts. Navigate to the relevant directory and follow the provided instructions.

### 🔹 Example: Deploying a VPN using Terraform

1. **Go to the `AWS-terraform-vpn` directory:**
   ```bash
   cd AWS-terraform-vpn
   ```

2. **Initialize Terraform:**
   ```bash
   terraform init
   ```

3. **Create a deployment plan:**
   ```bash
   terraform plan
   ```

4. **Apply the configuration:**
   ```bash
   terraform apply
   ```
   Confirm the deployment when prompted by typing `yes`.

5. **Retrieve deployment outputs:**
   After successful deployment, Terraform will provide output variables such as the VPN server’s public IP address. Use these details to configure your VPN client.

## 🤝 Contributing

We welcome contributions! To contribute:
1. **Fork** this repository.
2. **Create a new branch**: (`git checkout -b feature-branch`).
3. **Make your changes** and commit them: (`git commit -m "Added a new feature"`).
4. **Push the branch**: (`git push origin feature-branch`).
5. **Submit a pull request**.

## 📜 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

## 📧 Contact

For issues or suggestions, open a GitHub [issue](https://github.com/volodymyrshyshelov/various_AWS_scripts/issues) or reach out via email: ✉️ **vladimir.shyshelov@gmail.com**.

---

🚀 Happy cloud computing with AWS! 🌍☁️

