install:
	# Install all necessary dependencies
	pip install -r requirements.txt

run:
	# Run the Flask app
	flask run --host=0.0.0.0 --port=3000
