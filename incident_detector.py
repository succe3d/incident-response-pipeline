provider "aws" {
  region = "us-west-2"
}

resource "aws_cloudwatch_log_group" "incident_log_group" {
  name = "incident-log-group"
  retention_in_days = 14
}

resource "aws_cloudwatch_log_stream" "incident_log_stream" {
  name           = "incident-log-stream"
  log_group_name = aws_cloudwatch_log_group.incident_log_group.name
}

resource "aws_iam_role" "lambda_role" {
  name = "incident_detector_lambda_role"

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

resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_lambda_function" "incident_detector" {
  function_name = "incident_detector"
  role          = aws_iam_role.lambda_role.arn
  handler       = "incident_detector.lambda_handler"
  runtime       = "python3.10"

  filename         = "${path.module}/incident_detector.zip"
  source_code_hash = filebase64sha256("${path.module}/incident_detector.zip")

  environment {
    variables = {
      LOG_GROUP_NAME  = aws_cloudwatch_log_group.incident_log_group.name
      LOG_STREAM_NAME = aws_cloudwatch_log_stream.incident_log_stream.name
    }
  }
}
