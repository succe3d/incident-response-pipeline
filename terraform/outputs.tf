output "log_group_name" {
  value = aws_cloudwatch_log_group.incident_log_group.name
}

output "log_stream_name" {
  value = aws_cloudwatch_log_stream.incident_log_stream.name
}

output "lambda_function_name" {
  value = aws_lambda_function.incident_lambda.function_name
}
