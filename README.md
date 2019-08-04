# Recommender

Small recommendation engine to suggest potential tagas based on a collaborative filtering

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Installing

What things you need to install the software and how to install them


#### Docker:
```
brew install docker
```

#### Neo4j:
```
docker pull neo4j
docker run --publish=7474:7474 --publish=7687:7687 --env=NEO4J_AUTH=none --volume=$HOME/neo4j/data:/tmp/neo4j -v $HOME/neo4j/import:/var/lib/neo4j/import neo4j
```

#### Python:

```
brew install pyenv
pyenv install 3.7.4
pip install virtualenv
virtualenv venv374 -p /Users/username/.pyenv/versions/3.7.4/bin/python3.7
pip install -r requirements.txt
```

## Built With

* [Python3](https://www.python.org/)
* [Neo4j](https://neo4j.com/)
* [Docker](https://www.docker.com/)

## Authors

* **Pedro Puertas** - [GitHub](https://github.com/ppuerta)




