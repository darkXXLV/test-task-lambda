resource "aws_s3_bucket" "lblogs" {
  bucket = "nedarita"
}

resource "aws_s3_bucket_acl" "example" {
  bucket = aws_s3_bucket.lblogs.id
  acl    = "private"
}

resource "aws_s3_bucket_policy" "allow_access_for_alb" {
  bucket = aws_s3_bucket.lblogs.id
  policy = data.aws_iam_policy_document.s3_bucket_lb_write.json
}

resource "aws_iam_role" "i_am_s3_role" {
  name = "iam_for_s3_aimas"

  assume_role_policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": {
                "Service": "s3.amazonaws.com"
            },
            "Action": "sts:AssumeRole"
        }
    ]
}
EOF
}

resource "aws_iam_role_policy" "i_am_s3_role_policy" {
  name = "esnezinuvaiIES"
  role = aws_iam_role.i_am_s3_role.id
  policy = file("s3_iam_policy.json")
}

resource "aws_iam_role_policy" "s3_lambda_policy2" {
  name = "s3_lambda_policy2"
  role = aws_iam_role.iam_for_lambda.id
  policy = file("s3_lambda_poilcy.json")
}

data "aws_elb_service_account" "main" {}

data "aws_iam_policy_document" "s3_bucket_lb_write" {
  policy_id = "s3_bucket_lb_logs"

  statement {
    actions = [
      "s3:PutObject",
    ]
    effect = "Allow"
    resources = [
      "${aws_s3_bucket.lblogs.arn}/*",
    ]

    principals {
      identifiers = ["${data.aws_elb_service_account.main.arn}"]
      type        = "AWS"
    }
  }

  statement {
    actions = [
      "s3:PutObject"
    ]
    effect = "Allow"
    resources = ["${aws_s3_bucket.lblogs.arn}/*"]
    principals {
      identifiers = ["delivery.logs.amazonaws.com"]
      type        = "Service"
    }
  }


  statement {
    actions = [
      "s3:GetBucketAcl"
    ]
    effect = "Allow"
    resources = ["${aws_s3_bucket.lblogs.arn}"]
    principals {
      identifiers = ["delivery.logs.amazonaws.com"]
      type        = "Service"
    }
  }
}

output "bucket_name" {
  value = "${aws_s3_bucket.lblogs.bucket}"
}
