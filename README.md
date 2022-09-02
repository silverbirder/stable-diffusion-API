# stable-diffusion-API

API using [Stability-AI/stability-sdk](https://github.com/Stability-AI/stability-sdk).

## Getting Started

### Prepare

```
$ cp .env.sample .env
# Copy the API Key from https://beta.dreamstudio.ai/membership and paste it into the STABILITY_KEY value.
```

## Run on Local

```
$ python3 -m venv pyenv
$ pyenv/bin/pip3 install -r requirements.txt
$ flask run
```

Go to http://localhost:8080/?prompt=bird

## Run on Docker

```
$ docker build -t stable-diffusion-api:latest .
$ docker run --rm --env-file .env -p 8080:8080 stable-diffusion-api:latest
```

Go to http://localhost:8080/?prompt=bird