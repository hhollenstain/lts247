#!/bin/bash
#Simple local config/install script. Requires docker/docker-compose already installed

#starting up containers
composeUp() {
  docker-compose up -d
}

#Installing extensions from the extensions listed in extension.list
installExtensions() {
  for ext in $(cat extension.list);
    do docker exec -ti flarum extension require $ext;
    done;
}

#Loading proxy config
proxyConfig() {
  sudo cp local-configs/localhost.conf /mnt/docker/nginx/conf
}


#very Basic run
composeUp
installExtensions
proxyConfig
