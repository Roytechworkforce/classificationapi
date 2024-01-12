# Classification API with InceptionV3 🚀

Welcome to the Classification API, utilizing the InceptionV3 model for image recognition! 🌟 This API is built with TensorFlow 2.11.0, Python 3.8.0, and can be easily deployed using Docker Compose. Let's get started!

## Installation 🛠️

### Prerequisites
- Make sure you have Docker and Docker Compose installed on your system. You can download Docker [here](https://www.docker.com/get-started) and Docker Compose [here](https://docs.docker.com/compose/install/).

### Clone the Repository
```bash
git clone https://github.com/Roytechworkforce/classificationapi.git
cd classificationapi
```

### Build and Run with Docker Compose
```bash
docker-compose up --build
```

The API will be accessible at `http://localhost:3000`.

## API Endpoints 🚀
### 1. Register For Api
- **Endpoint:** `/register`
- **Method:** `POST`
- **Request:**
  - Form Data:
    - `username`: user name.
    - `password`: password.
### 2. Refill Tokens to make Api Calls
- **Endpoint:** `/refill`
- **Method:** `POST`
- **Request:**
  - Form Data:
    - `username`: user name.
    - `admin_pw`: abc123.
    - `amount`: 10

### 3. Upload Image for Classification
- **Endpoint:** `/predict`
- **Method:** `POST`
- **Request:**
  - Form Data:
    - `image`: Upload the image file for classification.

## Example Usage 💡

### Using Python Requests
```python
import requests
import json

# Replace 'your-image-file.jpg' with the path to your image file
url = "localhost:3000/classify"

payload = json.dumps({
  "username": "test",
  "password": "secure",
  "admin_pw": "abc123",
  "url": "https://cdn.pixabay.com/photo/2018/04/13/21/24/lion-3317670_1280.jpg",
  "amount": 4
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

# Print the result
print(json.loads(response.content))
```

## Acknowledgements 🙌

This API is powered by TensorFlow's InceptionV3 model. Special thanks to the TensorFlow team for providing this amazing resource.

## Contributing 🤝

If you'd like to contribute, please fork the repository and create a pull request. Feel free to open issues for feature requests, bug reports, or general feedback.

Happy coding! 🚀🔍📷
