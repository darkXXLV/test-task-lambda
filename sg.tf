resource "aws_security_group" "lb_sg" {
  name        = "lb_sg"
  description = "Application Load Balancer for lambda invocation"
  vpc_id      = aws_vpc.main.id

  ingress {
    description      = "astondesmitais ports"
    from_port        = 80
    to_port          = 80
    protocol         = "tcp"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }

  tags = {
    Name = "lb_sg"
  }
}