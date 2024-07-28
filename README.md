# Detection and Incident Response Pipeline

![image](https://github.com/user-attachments/assets/71368807-aa80-4911-9bf6-07fd461d22ec)

## Objective

The objective of this project is to understand the intricacies of CI/CD pipelines and how to create a detection and response system using AWS resources and GitHub Actions. This project demonstrates the process of setting up automated incident detection, logging incidents to CloudWatch Logs, and deploying resources using Infrastructure as Code (IaC) with Terraform. Through this project, we aim to:
- Gain hands-on experience with AWS services.
- Learn how to automate deployments using GitHub Actions.
- Understand the integration of Terraform for IaC.
  
## Tools Needed ##

-	Git: For version control
- GitHub Actions for CI/CD
- AWS: For cloud infrastructure
- Terraform: For infrastructure as code (IaC)
- AWS S3: For storing logs and other relevant data.
- AWS CloudWatch: For monitoring and alerting.
- AWS Lambda: For serverless computing to handle incident response

## Steps to Execute the Project

### 1. Set Up AWS Resources

1. **Create an AWS Account:**
   - Sign up for an AWS account at [AWS Signup](https://aws.amazon.com/).

2. **Create IAM User:**
   - Navigate to the IAM service in the AWS Management Console.
   - Create a new IAM user with `AdministratorAccess` policy and enable programmatic access by generating an access key and secret key.
   - Configure the AWS CLI with the IAM user credentials using the command:
     ```sh
     aws configure
     ```

3. **Install AWS CLI:**
   - Download and install the AWS CLI from the [AWS CLI Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
   - Verify the installation by running:
     ```sh
     aws --version
     ```

### 2. Create the Python Script for Incident Detection

1. **Write the Python Script:**
   - Create a [incident_detector.py](https://github.com/succe3d/incident-response-pipeline/blob/main/terraform/incident_detector.py) script with the following structure:
     - Import necessary libraries.
     - Create a function to simulate incident detection.
     - Log the detected incidents to CloudWatch Logs.

2. **Package the Script:**
   - Package the script into a `lambda_function_payload.zip` file for deployment using:
     ```sh
     zip lambda_function_payload.zip incident_detector.py
     ```

### 3. Set Up Terraform Configuration

1. **Install Terraform:**
   - Download and install Terraform from the [Terraform Installation Guide](https://learn.hashicorp.com/tutorials/terraform/install-cli).
   - Verify the installation by running:
     ```sh
     terraform --version
     ```

2. **Create Terraform Files:**
   - Create [main.tf](https://github.com/succe3d/incident-response-pipeline/blob/main/terraform/main.tf) and [outputs.tf](https://github.com/succe3d/incident-response-pipeline/blob/main/terraform/outputs.tf) files with the following configurations:
     - Define AWS provider configuration.
     - Define resources such as CloudWatch Log Group, Lambda Function, and CloudWatch Event Rule.

3. **Initialize and Apply Terraform:**
   - Initialize Terraform in the project directory:
     ```sh
     terraform init
     ```
   - Apply the Terraform configuration to create resources:
     ```sh
     terraform apply
     ```

### 4. Set Up GitHub Actions for CI/CD

1. **Create GitHub Repository:**
   - Create a new GitHub repository to store your project files.

2. **Add Project Files:**
   - Add the Python script, Terraform files, and GitHub Actions workflow file to the repository.

3. **Configure GitHub Secrets:**
   - Add your AWS credentials as secrets in the GitHub repository settings (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`).

4. **Create GitHub Actions Workflow:**
   - Define workflow [main.yml](https://github.com/succe3d/incident-response-pipeline/blob/main/.github/workflows/main.yml) in `.github/workflows/main.yml` to automate the deployment process using GitHub Actions.

### 5. Verify Deployment

1. **Check GitHub Actions:**
   - Ensure the GitHub Actions workflow runs successfully and deploys the resources. Check the Actions tab in your GitHub repository for workflow status.

2. **Check AWS Management Console:**
   - Log in to the AWS Management Console and navigate to the CloudWatch service to verify the creation of resources such as:
     - CloudWatch Log Group
     - Lambda Function
     - CloudWatch Event Rule
     - Log Stream

3. **Verify CloudWatch Logs:**
   - Navigate to CloudWatch Logs and check for detailed incident logs in the specified log stream. The logs should contain detailed information about the incidents detected.
     ![image](https://github.com/user-attachments/assets/571af944-2796-485d-bcdf-559666b30aa0)
 
## Conclusion

The project successfully demonstrates the setup and execution of an automated incident detection and response pipeline using AWS resources and GitHub Actions for CI/CD. Through this project, we explored the use of Infrastructure as Code (IaC) with Terraform, automated deployments with GitHub Actions, and incident logging with AWS CloudWatch. This hands-on experience provides valuable insights into the workings of CI/CD pipelines and the implementation of detection and response systems in the cloud.

- **GitHub Actions Workflow**: Automates the deployment process by triggering on code changes.
  - **Triggers**: Code push events.
  - **Steps**: Checkout code, configure AWS credentials, and run Terraform commands to deploy resources.

- **AWS Resources**:
  - **CloudWatch Log Group**: Stores logs for detected incidents.
  - **Log Stream**: Individual stream within the log group for detailed logs.
  - **Lambda Function**: Executes the incident detection script.
  - **CloudWatch Event Rule**: Triggers the Lambda function based on specific events or schedules.
 
    
By completing this project, we gained a deeper understanding of:
- Configuring AWS resources for automated incident detection.
- Implementing Infrastructure as Code (IaC) to manage cloud resources.
- Automating deployments and workflows with GitHub Actions.
- Logging and monitoring incidents using AWS CloudWatch.

This knowledge equips us with the foundational skills needed to build robust and automated detection and response systems in real-world scenarios.
