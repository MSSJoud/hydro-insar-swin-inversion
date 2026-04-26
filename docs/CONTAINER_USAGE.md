# Container usage

## Build

```bash
docker compose build
```

## Validate config

```bash
docker compose run --rm app hisi check-config /workspace/configs/emilia_romagna.example.yaml
```

## Show parsed paths

```bash
docker compose run --rm app hisi show-paths /workspace/configs/emilia_romagna.example.yaml
```

## Open a shell

```bash
docker compose run --rm app bash
```

## Start Jupyter Lab

```bash
docker compose up notebook
```

The notebook server is exposed on:

- `http://localhost:8888`

## Mount model

The compose file assumes:

- repo mounted at `/workspace`
- local `./data` mounted at `/data`
- local `./outputs` mounted at `/workspace/outputs`

This keeps code, data, and outputs clearly separated.

