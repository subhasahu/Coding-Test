terraform {
  required_version = "~> 1.1.0" # which means any version equal & above 1.1.0 and less than 1.1.2
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.0"
    }
  }
}

# Provider Block
provider "aws" {
  region  = var.aws_region
  #profile = "default"
}
