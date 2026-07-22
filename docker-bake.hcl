variable "IMAGE" {
  default = "YOUR_DOCKERHUB_USERNAME/diabetic-prediction-model-deeplearning-main:latest"
}

group "default" {
  targets = ["app"]
}

target "app" {
  context = "."
  dockerfile = "Dockerfile"
  tags = [IMAGE]
  platforms = ["linux/amd64"]
}
