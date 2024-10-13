# Latent Semantic Analysis (LSA) Search Engine

## Overview
This project is an interactive web application that implements a basic search engine using Latent Semantic Analysis (LSA). The application takes a user's query, applies LSA on a predefined dataset, and returns the most relevant documents based on cosine similarity.

You can watch a demonstration of the project in this video: [LSA Search Engine Demo](https://youtu.be/qAmbsn4ONnU).

## Features
- **Document Retrieval**: Users can enter a query, and the system will return the top 5 documents that are most similar to the query.
- **Visualization**: A bar chart shows the cosine similarity of the top retrieved documents to the query.
- **User Interface**: A clean and responsive UI that allows users to enter a query and see the results along with similarity scores and a visualization.

## Technologies Used
- **Flask**: Backend framework for handling requests and serving the web application.
- **Scikit-learn**: Used for TF-IDF transformation, Singular Value Decomposition (SVD), and cosine similarity calculations.
- **Plotly.js**: Used for visualizing the similarity scores as a bar chart.
- **HTML/CSS/JavaScript**: Frontend components for the user interface.

## How to Run the Project
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd CS506-Assignment4
   ```
3. Create a virtual environment and activate it:
   ```
   python -m venv venv
   . venv/bin/activate
   ```
4. Install the required dependencies:
   ```
   make install
   ```
5. Run the application locally:
   ```
   make run
   ```
6. Open your browser and go to [http://localhost:3000](http://localhost:3000) to use the search engine.

## Project Structure
- **app.py**: The main Flask application file that sets up routes and handles requests.
- **templates/index.html**: The main HTML file containing the structure of the web interface.
- **static/style.css**: The CSS file that styles the webpage.
- **static/main.js**: JavaScript file that handles form submissions and updates the UI.
- **Makefile**: Used to automate the installation and running of the application.
- **requirements.txt**: Lists the Python dependencies required for the project.

## Demonstration
Watch the video below to see a full demonstration of the LSA Search Engine in action:
[![LSA Search Engine Demo](https://img.youtube.com/vi/qAmbsn4ONnU/0.jpg)](https://youtu.be/qAmbsn4ONnU)

## License
This project is licensed under the MIT License.

