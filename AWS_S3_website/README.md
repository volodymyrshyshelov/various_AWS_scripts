# S3 Bucket Creation and Website Calculator Deployment

This Python script automates the process of creating an Amazon S3 bucket, configuring the necessary policies, and uploading a website calculator built with JavaScript. It simplifies the setup process and allows you to quickly deploy the calculator on AWS.

## Prerequisites

Before running the script, make sure you have the following:

- Python 3.x installed on your machine.
- AWS CLI (Command Line Interface) installed and configured with appropriate access credentials.
- Configure the AWS CLI: Run the following command in the terminal or command prompt:

   ```bash
   aws configure
   ```
- Provide the requested information:

   - Enter your AWS access key ID.
   - Enter your AWS secret access key.
   - Set the default region name (e.g., `us-west-2`) that matches your AWS resources' location.
   - Set the default output format (e.g., `json`) for command output. This can be left empty for the default format.

   Note: The access key ID, secret access key, and region you provide during the configuration will be used as the default values for subsequent AWS CLI commands.

## Installation

Install the required Python packages by running the following command in your terminal:

```bash
pip install boto3
```

## Usage
1. Open a terminal and navigate to the project directory.

2. Execute the Python script using the following command:

```bash
python main.py
```

3. Once the script completes, it will output the URL of the deployed website calculator.

## Configuration

Set your variable values in the variables.py file.

    - aws_access_key_id
    - aws_secret_access_key
    - region_name
    - user_name
    - aws_account_id
    - bucket_name

## License

This script is released under the [MIT License](LICENSE).
