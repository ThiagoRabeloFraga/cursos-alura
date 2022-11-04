# app-exemplo

## docker build

```
docker build -t <seu-nome-de-usuario-do-docker-hub>/app-node:1.0
```

## docker run com volume

```
docker run -it --mount type=bind,source=<diretorio-do-volume>,target=/app ubuntu bash
```

```
docker run -it --mount type=bind,source=meu-novo-volume,target=/app ubuntu bash
```

## tmpfs

```
docker run -it --tmpfs=/app ubuntu bash
```

```
docker run -it --mount type=tmpfs,target=/app ubuntu bash
```
