provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "incident_logs" {
  bucket = "your-bucket-name"
}

resource "aws_cloudwatch_log_group" "incident_logs" {
  name = "/aws/lambda/incident_logs"
}

resource "aws_sns_topic" "incident_response" {
  name = "IncidentResponseTopic"
}

resource "aws_lambda_function" "incident_handler" {
  filename         = "lambda.zip"
  function_name    = "incidentHandler"
  role             = aws_iam_role.lambda_exec.arn
  handler          = "lambda_function.lambda_handler"
  source_code_hash = filebase64sha256("lambda.zip")
  runtime          = "python3.8"
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Sid    = ""
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      },
    ]
  })
}

resource "aws_iam_role_policy" "lambda_exec_policy" {
  name   = "lambda_exec_policy"
  role   = aws_iam_role.lambda_exec.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
        Effect   = "Allow"
        Resource = "*"
      },
      {
        Action = "sns:Publish"
        Effect = "Allow"
        Resource = "arn:aws:sns:us-west-2:123456789012:IncidentResponseTopic"
      },
    ]
  })
}
