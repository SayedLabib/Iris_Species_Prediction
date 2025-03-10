# Iris Detection API

This project is a FastAPI application for detecting Iris flower species based on input features. It utilizes a trained machine learning model to make predictions and provides an API for users to interact with the model.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/iris-detection-api.git
   cd iris-detection-api
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables in the `.env` file as needed.

## Usage

To run the FastAPI application, execute the following command:
```bash
uvicorn src.main:app --reload
```

You can access the API documentation at `http://127.0.0.1:8000/docs`.

## Endpoints

- **POST /predict**: Make a prediction based on the input features.

## Testing

To run the tests, use the following command:
```bash
pytest
```

## License

This project is licensed under the MIT License.