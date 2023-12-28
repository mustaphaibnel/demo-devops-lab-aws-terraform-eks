resource "aws_vpc" "eks_vpc" {
  cidr_block = "10.0.0.0/16"
  enable_dns_support   = true
  enable_dns_hostnames = true

  tags = {
    Name = "eks_vpc"
  }
}

resource "aws_subnet" "eks_subnet" {
  count = 2

  vpc_id            = aws_vpc.eks_vpc.id
  cidr_block        = count.index == 0 ? "10.0.1.0/24" : "10.0.2.0/24"
  availability_zone = "us-west-2a"  # Change to your availability zone

  tags = {
    Name = "eks_subnet_${count.index}"
  }
}
