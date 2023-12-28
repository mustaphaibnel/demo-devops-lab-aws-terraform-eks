terraform {
  backend "s3" {
    bucket = "my-terraform-state-bucket-dev"
    key    = "dev/terraform.tfstate"
    region = "us-west-2"
  }
}
