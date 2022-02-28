# resource "aws_s3_bucket" "lblogs" {
#   bucket = "nedarita"
# }

# resource "aws_s3_bucket_acl" "example" {
#   bucket = aws_s3_bucket.lblogs.id
#   acl    = "private"
# }

# resource "aws_s3_bucket_policy" "allow_access_from_another_account" {
#   bucket = aws_s3_bucket.lblogs.id
#   policy = file("s3_policy.json")
# }
