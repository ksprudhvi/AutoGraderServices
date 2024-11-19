from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace these with your Azure Document Intelligence endpoint and API key
AZURE_ENDPOINT = "https://docintprudhvi.cognitiveservices.azure.com/"
API_KEY = "C5MpFIwSPmkCZcWhOc65a753bQmoCtNeF9m8TfTD8IhXTAzZ3oi7JQQJ99AKACYeBjFXJ3w3AAALACOGfgpD"

@app.route('/analyze-document', methods=['POST'])
def analyze_document():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']

    if file.filename == '':
        return jsonify({"error": "No file selected"}), 400

    # Set up the request to Azure Document Intelligence
    url = f"{AZURE_ENDPOINT}documentintelligence/documentModels/prebuilt-layout:analyze?api-version=2024-02-29-preview&features=formulas"
    headers = {
        "Ocp-Apim-Subscription-Key": API_KEY,
        "Content-Type": file.content_type  # Ensure this matches the file type (e.g., "application/pdf" or "image/jpeg")
    }

    # Send the file to Azure Document Intelligence
    response = requests.post(url, headers=headers, data=file.read())

    # Check the response from Azure
    if response.status_code == 200:
        return jsonify(response.json()), 200
    else:
        return jsonify({"error": "Failed to process document", "details": response.text}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
