output "ec2_public_ip" {
  value = aws_instance.app.public_ip
}

output "rds_endpoint" {
  value = aws_db_instance.mysql.endpoint
}

output "ecr_frontend" {
  value = aws_ecr_repository.frontend.repository_url
}

output "ecr_backend" {
  value = aws_ecr_repository.backend.repository_url
}
