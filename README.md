# halbrd.com

## Install requirements

```
pipenv install
```

## Run

### Development

```
python main.py
```

### Production: Gunicorn

```
gunicorn -b 0.0.0.0:<port> main:app
```

### Production: Docker

```
docker build . -t halbrd.com
docker run -p 80:80 halbrd.com
```
