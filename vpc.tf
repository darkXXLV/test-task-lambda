resource "aws_vpc" "main" {
  cidr_block       = "172.64.0.0/16"
  instance_tenancy = "default"
  enable_dns_hostnames = true

  tags = {
    Name = "main"
  }
}

resource "aws_subnet" "main" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "172.64.1.0/24"
  availability_zone = "eu-north-1a"
  tags = {
    Name = "test1"
  }
}

resource "aws_subnet" "main2" {
  vpc_id     = aws_vpc.main.id
  cidr_block = "172.64.2.0/24"
  availability_zone = "eu-north-1b"
  tags = {
    Name = "test2"
  }
}

resource "aws_internet_gateway" "gateway" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "main"
  }
}

# resource "aws_network_acl" "main" {
#   vpc_id = aws_vpc.main.id
#   default = true

#   egress {
#     protocol   = "-1"
#     rule_no    = 200
#     action     = "allow"
#     cidr_block = "127.0.0.0/24"
#     from_port  = 0
#     to_port    = 0
#   }

#   ingress {
#     protocol   = "-1"
#     rule_no    = 100
#     action     = "allow"
#     cidr_block = "127.0.0.0/24"
#     from_port  = 0
#     to_port    = 0
#   }

#   tags = {
#     Name = "main"
#   }
# }

# resource "aws_network_acl_association" "main" {
#   network_acl_id = aws_network_acl.main.id
#   subnet_id      = aws_subnet.main.id
# }

# resource "aws_network_acl_association" "main2" {
#   network_acl_id = aws_network_acl.main.id
#   subnet_id      = aws_subnet.main2.id
# }