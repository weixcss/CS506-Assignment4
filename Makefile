Makefile:

install:
	pip install -r requirements.txt

run:
	flask run --host=0.0.0.0 --port=3000

requirements.txt:

flask
scikit-learn
numpy
nltk