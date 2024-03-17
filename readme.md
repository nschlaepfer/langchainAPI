gunicorn -w 4 -b :$PORT app:app

run python app.py for dev.

or local 
gunicorn -w 4 -b :8000 app:app