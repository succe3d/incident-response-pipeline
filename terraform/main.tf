provider "aws" {
  region = "us-east-2"
}

resource "aws_s3_bucket" "lambda_bucket" {
  bucket = "incident-response-pipeline-bucket"
}

resource "aws_cloudwatch_log_group" "incident_log_group" {
  name = "incident-response-log-group"
  retention_in_days = 14
}

resource "aws_cloudwatch_log_stream" "incident_log_stream" {
  log_group_name = aws_cloudwatch_log_group.incident_log_group.name
  name           = "incident-response-log-stream"
}

resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
      }
    ]
  })
}

resource "aws_iam_role_policy" "lambda_policy" {
  name   = "lambda-policy"
  role   = aws_iam_role.lambda_role.id
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "s3:PutObject"
        ]
        Resource = "*"
      }
    ]
  })
}

resource "aws_lambda_function" "incident_lambda" {
  function_name    = "incidentResponseHandler"
  role             = aws_iam_role.lambda_role.arn
  handler          = "incident_detector.lambda_handler"
  runtime          = "python3.8"
  filename         = "lambda_function_payload.zip"
  source_code_hash = filebase64sha256("lambda_function_payload.zip")
}

resource "aws_cloudwatch_event_rule" "every_minute" {
  name                = "every_minute"
  schedule_expression = "rate(1 minute)"
}

resource "aws_cloudwatch_event_target" "incident_target" {
  rule      = aws_cloudwatch_event_rule.every_minute.name
  target_id = "incident_lambda"
  arn       = aws_lambda_function.incident_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.incident_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_minute.arn
}

output "lambda_function_name" {
  value = aws_lambda_function.incident_lambda.function_name
}
