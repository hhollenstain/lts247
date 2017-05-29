# Forked from mondedie/docker-flarum

 Adapated from: https://github.com/mondediefr/docker-flarum
![logo](https://i.imgur.com/Bjrtbsc.png "logo")

### What is this ?

Flarum is the next-generation forum software that makes online discussion fun. It's simple, fast, and free. http://flarum.org/

### Features

- Lightweight & secure image
- Based on Alpine Linux with **nginx** and **PHP 7.1**
- Latest Flarum Beta (v0.1.0-beta.6)
- MySQL/Mariadb driver
- OPCache extension configured

### Build-time variables

- **VERSION** = Version of flarum (default: *v0.1.0-beta.6*)

### Ports

- **8888**

### Volume

- **/flarum/app/assets** : Flarum assets directory
- **/flarum/app/extensions** : Flarum extension directory

### Environment variables

| Variable | Description | Type | Default value |
| -------- | ----------- | ---- | ------------- |
| **UID** | Flarum user id | *optional* | 991
| **GID** | Flarum group id | *optional* | 991
| **DEBUG** | Flarum debug mode | *optional* | false
| **FORUM_URL** | Forum URL | **required** | none
| **DB_HOST** | MariaDB instance ip/hostname | *optional* | mariadb
| **DB_USER** | MariaDB database username | *optional* | flarum
| **DB_NAME** | MariaDB database name | *optional* | flarum
| **DB_PASS** | MariaDB database password | **required** | none
| **DB_PREF** | Flarum tables prefix | *optional* | none

## Installation

#### 1 - PreRequisites

Following needs to bee setup on your local environment:
- docker
  https://docs.docker.com/engine/installation/
- Docker-compose
  https://docs.docker.com/compose/install/
- python ~ 2.7
- python-pip
  If on ubuntu:  ```bash sudo apt install python-pip```

#### 2 load python requirements

Currently only need to install docker sdk library, but all requirements are
placed in requirements.txt

```bash
pip install -r requirements.txt
```


#### 5 - build the infrastructure :tada:

You can now run Flarum :

```bash
./install.py build
```

### Upgrade newly added extensions to repo

```bash
./install.py update
```


### Install custom extensions

**Flarum extensions list :** https://packagist.org/search/?q=flarum-ext

#### Install an extension

```
docker exec -ti flarum extension require some/extension
```

#### Remove an extension

```
docker exec -ti flarum extension remove some/extension
```

#### List all extensions

```
docker exec -ti flarum extension list
```

### Custom error pages

To use custom error pages, add your .html files in `/mnt/docker/flarum/assets/errors` folder :

```
mkdir -p /mnt/docker/flarum/assets/errors
touch 403.html 404.html 500.html 503.html
chown -R 991:991 /mnt/docker/flarum
```

### Custom composer repositories

To use the composer repository system, add your repo name and json representation in `/mnt/docker/flarum/extensions/composer.repositories.txt` :

```
my_private_repo|{"type":"path","url":"extensions/*/"}
my_public_repo|{"type":"vcs","url":"https://github.com/my/repo"}
```

https://getcomposer.org/doc/03-cli.md#modifying-repositories

### Screenshot

#### Installation

![flarum-installation](http://i.imgur.com/e3Hscp4.png)

#### Home page

![flarum-home](http://i.imgur.com/6kH9iTV.png)
