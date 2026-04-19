# va-sample-python

Minimal Python HTTP application used as a sample deployment target by the
Valtunox provisioner. Uses [Flask](https://flask.palletsprojects.com/) with
Gunicorn as the production server.

## Endpoints

| Method | Path      | Returns                          |
|--------|-----------|----------------------------------|
| GET    | `/`       | HTML landing page (`index.html`) |
| GET    | `/health` | JSON health payload              |

## Configuration

| Env var    | Default | Purpose                   |
|------------|---------|---------------------------|
| `app_port` | `8000`  | Port the server binds to  |

## Build and run

### Docker

```
docker build -t va-sample-python .
docker run --rm -p 8000:8000 va-sample-python
```

Then open http://localhost:8000.

### Local

```
pip install -r requirements.txt
python app.py
```

## License

MIT — see [LICENSE](LICENSE).
