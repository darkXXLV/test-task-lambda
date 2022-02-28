resource "aws_lb" "justForTesting" {
  name               = "test-lb-tf"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.lb_sg.id]
  subnets            = ["subnet-028177bc4b27450dc", "subnet-0591ab2bf707ce98c"]


  enable_deletion_protection = true

  access_logs {
    bucket  = aws_s3_bucket.lblogs.bucket
    prefix  = "test-lb-tf"
    enabled = true
  }

  tags = {
    Environment = "production"
  }
}

resource "aws_lambda_permission" "with_lb" {
  statement_id  = "AllowExecutionFromlb"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.test_lambda.arn
  principal     = "elasticloadbalancing.amazonaws.com"
  source_arn    = aws_lb_target_group.lambda-example.arn
}


resource "aws_lb_target_group" "lambda-example" {
  name        = "testLambda"
  target_type = "lambda"
}

resource "aws_lb_listener" "front_end" {
  load_balancer_arn = aws_lb.justForTesting.arn
  port              = "80"
  protocol          = "HTTP"
  

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.lambda-example.arn
  }
}


resource "aws_lb_target_group_attachment" "test" {
  target_group_arn = aws_lb_target_group.lambda-example.arn
  target_id        = aws_lambda_function.test_lambda.arn
  depends_on       = [aws_lambda_permission.with_lb]
}