from src.lambda_function import lambda_handler

if __name__ == "__main__":
    event = {
        "name": "Ranu",
        "source": "local-test"
    }
    context = None

    response = lambda_handler(event, context)
    print("Lambda Response:")
    print(response)
