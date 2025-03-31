# Script to Remove AWS Resources

This Python script is designed to remove specific AWS resources from your account. It can be used to remove API Gateways, CloudFront distributions, Lambda functions, and S3 buckets.

**Note: Please use this script with caution as it will permanently delete the specified resources. Make sure you have appropriate permissions and double-check the resources you want to remove before executing the script.**

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

To install the necessary Python dependencies, use the following command:

```bash
pip install boto3
```


## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the script is located.
3. Run the script using the following command:

   ```bash
   python main.py
   ```

4. The script will start removing the specified AWS resources.
5. You may be prompted for confirmation when deleting certain resources. Confirm the deletion by typing "yes" and pressing Enter.

## Important Considerations

- This script assumes that you have appropriate permissions to delete the specified AWS resources. Make sure you have the necessary access rights before executing the script.
- Take extra care when choosing the resources to remove. Deleting resources is irreversible, and it may lead to data loss or impact your applications if not done correctly.
- The script will only remove resources within the AWS account associated with the provided access credentials.


## License

This script is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](LICENSE) file for more details.
