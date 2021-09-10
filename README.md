# react-flask-mongo-starter

run full stack
```
docker-compose up
```

## Flask API
```
docker build -f Dockerfile.api -t ppawletta/flask-api .
docker push ppawletta/flask-api
```

## Nginx with React app
```
docker build -f Dockerfile.client -t ppawletta/nginx-react .
docker push ppawletta/nginx-react
```