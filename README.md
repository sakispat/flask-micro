# Flask Microservices

```bash
    # virtualenv
    python -m venv venv
    sourve venv/bin/activate    (Linux)
    env\Scripts\activate        (Windows)

    # install packages
    pip install -r requirements.txt

    # copy .env.example to .env
    cp .env.example .env

    # secret key
    python -c 'import secrets;print(secrets.token_urlsafe(your_number))'

    # Docker build
    ./build.sh

    # Docker stop
    ./stop.sh

    # run server
    flask run
```
