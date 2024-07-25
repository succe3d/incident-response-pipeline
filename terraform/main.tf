provider "aws" {
  region = "us-west-2"
}

resource "aws_cloudwatch_log_group" "incident_log_group" {
  name = "incident-response-log-group"
  retention_in_days = 14
}

resource "aws_cloudwatch_log_stream" "incident_log_stream" {
  name           = "incident-response-log-stream"
  log_group_name = aws_cloudwatch_log_group.incident_log_group.name
}

resource "aws_iam_role" "lambda_role" {
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

resource "aws_iam_role_policy" "lambda_policy" {
  name = "lambda_policy"
  role = aws_iam_role.lambda_role.id

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
    ]
  })
}

resource "aws_lambda_function" "incident_lambda" {
  filename         = "lambda_function_payload.zip"
  function_name    = "incidentResponseHandler"
  role             = aws_iam_role.lambda_role.arn
  handler          = "incident_detector.log_incident"
  runtime          = "python3.10"

  source_code_hash = filebase64sha256("lambda_function_payload.zip")

  environment {
    variables = {
      LOG_GROUP_NAME  = aws_cloudwatch_log_group.incident_log_group.name
      LOG_STREAM_NAME = aws_cloudwatch_log_stream.incident_log_stream.name
      AWS_REGION      = "us-west-2"
    }
  }
}

resource "aws_cloudwatch_event_rule" "every_minute" {
  name        = "every_minute"
  description = "Fires every minute"
  schedule_expression = "rate(1 minute)"
}

resource "aws_cloudwatch_event_target" "lambda_target" {
  rule      = aws_cloudwatch_event_rule.every_minute.name
  target_id = "lambda"
  arn       = aws_lambda_function.incident_lambda.arn
}

resource "aws_lambda_permission" "allow_cloudwatch" {
  statement_id  = "AllowExecutionFromCloudWatch"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.incident_lambda.function_name
  principal     = "events.amazonaws.com"
  source_arn    = aws_cloudwatch_event_rule.every_minute.arn
}
