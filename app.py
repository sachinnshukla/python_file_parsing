from flask import Flask, render_template, request, send_file
import csv
import os
import json

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def read_products_from_file(file_path):
    """So, this function reads data from text file uploaded by user."""
    products = []
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            # Check if file is empty
            if len(lines) == 0:
                print("Error: File is empty.")
                return []
            for i in range(0, len(lines), 4):
                # Skip empty lines
                if not lines[i:i+4]:
                    continue
                product = {
                    "ProductID": lines[i].split(': ')[1].strip(),
                    "Name": lines[i+1].split(': ')[1].strip(),
                    "Price": lines[i+2].split(': ')[1].strip(),
                    "InStock": lines[i+3].split(': ')[1].strip()
                }
                products.append(product)
        # Check if any products were found
        if not products:
            print("Error: No products found in the file.")
            return []
        return products[0]
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return []
    except IndexError:
        print("Error: Incorrect file format or missing data.")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []


def read_csv_file(filename):
    """So, this function reads data from CSV file uploaded by user."""
    try:
        # Check if file exists
        if not os.path.exists(filename):
            print(f"Error: File '{filename}' not found.")
            return []
        # Check if file is empty
        if os.path.getsize(filename) == 0:
            print(f"Error: File '{filename}' is empty.")
            return []
        with open(filename, 'r', newline='') as file:
            csv_reader = csv.reader(file)
            data = []
            for row in csv_reader:
                # Skip blank lines
                if len(row) == 0 or all(cell.isspace() for cell in row):
                    continue
                data.append(row)
            return data[0]
    except Exception as e:
        print(f"Error reading CSV file: {e}")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    """this is method used to verify the files uploaded by users and then saves it in upload folder"""
    # Check if files were uploaded
    if 'csv_file' not in request.files or 'text_file' not in request.files:
        return "Error: Please upload both CSV and text files."

    csv_file = request.files['csv_file']
    text_file = request.files['text_file']

    # Check if files have valid extensions
    if csv_file.filename == '' or not csv_file.filename.endswith('.csv'):
        return "Error: Please upload a CSV file."
    if text_file.filename == '' or not text_file.filename.endswith('.txt'):
        return "Error: Please upload a text file."

    # Save uploaded files
    csv_filename = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
    text_filename = os.path.join(app.config['UPLOAD_FOLDER'], text_file.filename)
    csv_file.save(csv_filename)
    text_file.save(text_filename)

    # Check if both files were uploaded
    if not os.path.exists(csv_filename) or not os.path.exists(text_filename):
        return "Error: Files were not uploaded successfully."

    # Read data from files
    keys = read_csv_file(csv_filename)
    print(keys)
    valuess = read_products_from_file(text_filename)
    values = list(valuess.values())

    data = {}
    for key, value in zip(keys, values):
        data[key] = value
    print(data)
    # Convert data to JSON
    json_string = json.dumps(data, indent=4)

    output_filename = 'output.json'
    with open(output_filename, 'w') as json_file:
        json_file.write(json_string)

    return render_template('result.html', json_string=json_string)

@app.route('/download')
def download():
    filename = 'output.json'
    return send_file(filename, as_attachment=True)
if __name__ == '__main__':
    app.run(debug=True)
