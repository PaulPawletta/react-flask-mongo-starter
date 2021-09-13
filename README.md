# react-flask-mongo-starter

## Development

start backend in dev mode
````
docker-compose -f docker-compose-dev.yml up --build
````

start frontend in dev mode
````
cd client
yarn start
````

### Production

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