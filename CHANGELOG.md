# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) 

## [Unreleased]

## [0.1.3] - 2018-08-20
### Added
* Demo database (was accidentally removed)

### Changed
* Change to Python 3.6-alpine for docker build from 3.7 - reduced image size by 1GB
* WSGI.py is no longer in debug for production use. 

## [0.1.2] - 2018-08-18
### Added
* environment variables for Docker-Compose to support using nginx-proxy and [letsencrypt-nginx-proxy-companion](https://hub.docker.com/r/jrcs/letsencrypt-nginx-proxy-companion/)
* requirements for development and production

### Changed
* update of Docker-Compose to support more environment variables (domain name, replica sets for swarm, CPU and memory, restart policy)
* not all ENV are used in docker-compose. Some are for Swarm settings, which is not currently being used in my setup.
* update to Flask-Appbuilder 1.11.1

### Moved
- docker-compose to main directory

## [0.X.X] - 
### Added
- previous versions did not have a change log. Note commits

    * more edits to the readme for clarity and better explanation of how to…  …
    * change of readme to markdown
    * edits for bullets
    * moved readme to top directory
    * added latest tag and update of readme for docker pull
    * mapping of ports to 5000 as it is the default for flask vs 8080 for f…  …
    * add of pynote demo app
    * wrote the app....
