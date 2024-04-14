
# Python file parsing

This is a Flask web application that allows users to upload a CSV file and a text file, processes the data from these files, and generates a JSON file as output and also gives option to download the file.

## How It Works

### `read_products_from_file(file_path)`

This function reads product data from a text file located at the specified `file_path`. The text file is assumed to have a specific format where each product's information is separated by lines.

### `read_csv_file(filename)`

This function reads data from a CSV file specified by the `filename`. It skips blank lines and returns the data from the first non-blank row.

### `index()`

This route renders the index HTML page, which contains a form for uploading CSV and text files.

### `upload()`

This route handles the file upload process. It checks if both a CSV file and a text file are uploaded, saves them to the server, reads their data, generates a JSON string, and renders the result HTML page with the JSON string.

### `download()`

This route allows users to download the generated JSON file (`output.json`) as an attachment.

## How to Run the Application

1. Clone this repository to your local machine:
git clone https://github.com/sachinnshukla/python_file_parsing.git


2. Navigate to the project directory:

cd python_file_parsing


3. Install the required dependencies using pip:

pip install -r requirements.txt


4. Run the Flask application:

python app.py or python3 app.py


5. Open a web browser and go to `http://127.0.0.1:5000/` to access the application.

6. Upload a CSV file and a text file from folder static "this folder contains 2 files one is csv and text file" you get this folder when you clone the repository.

7. Optionally, you can download the generated JSON file by clicking the download link.

## Requirements

- Python 3.x
- Flask
- Other dependencies listed in `requirements.txt`





## Demo

link where you can see how this application works.

https://photos.app.goo.gl/Q95syLkHD5qjNxPa8