output "public_ip" {
  description = "Public IP of k3s EC2 instance"
  value       = aws_instance.k3s.public_ip
}