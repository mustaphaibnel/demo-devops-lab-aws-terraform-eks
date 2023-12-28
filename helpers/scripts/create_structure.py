#!/usr/bin/env python3
import os

def create_project_structure(base_path):
    """
    Create the directory structure for the Terraform project.
    """
    directories = [
        "environments/dev",
        "environments/qa",
        "environments/prod",
        "modules/eks",
        "modules/vpc",
        "modules/cloudfront",
        "modules/api_gateway",
        "modules/cognito",
        "modules/ec2",
        "modules/s3_backup",
        "modules/security_group",
        "modules/aws_vault",
        "global/iam",
        "global/s3_state_storage",
        "scripts"
    ]

    for directory in directories:
        path = os.path.join(base_path, directory)
        os.makedirs(path, exist_ok=True)
        # Create basic Terraform files in each module and environment
        for file in ["main.tf", "variables.tf", "outputs.tf"]:
            open(os.path.join(path, file), 'a').close()

    # Create README.md at the root
    open(os.path.join(base_path, "README.md"), 'a').close()

# Assuming the script is executed in the repository root directory
repo_root_path = os.getcwd()
create_project_structure(repo_root_path)

