#!/usr/bin/env bash
up() {
  echo "Creating Container..."

  docker-compose up -d
  
  sudo chmod -R 777 dags
}

case $1 in
  up)
    up
    ;;
  *)
    echo "Usage: $0 {up}"
    ;;
esac