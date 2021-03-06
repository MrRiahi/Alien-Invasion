# Alien_Invasion

This repository contains `Alien Invasion` game from "Python Crash Course".


## Install

### Clone Repository

Clone repo and install requirements.txt in a Python==3.8.3 environment.

```bash
git clone git@github.com:MrRiahi/Alien-Invasion.git
cd Alien-Invasion
```

### Virtual Environment
Python virtual environment will keep dependant Python packages from interfering with other Python projects on your
system.

```bash
python -m venv venv
source venv/bin/activate
``` 

### Requirements

Install python requirements.

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## Run
To play the game, run the `alien_invasion.py`.

```bash
python alien_invasion.py
```

## Docker
Build the alien_invasion docker image with the following command:

```bash
$ docker \
    build \
    --tag alien_invasion \
    .
```

To run the image in a container:

```bash
$ docker container run \
	-it \ 
	--rm \
	--name alien_invasion \
	 alien_invasion
```

## TODO
- [x] Refactor with PEP 8 coding style
- [x] Create a Dockerfile
- [ ] Add unit tests
- [ ] Add TDD
- [ ] Add new features
- [ ] Use RL model to learn how to play the game
