import requests


def main():
    response = requests.get("http://localhost:8000/users/")
    print(response.json())
    headers = {"Content-Type": "application/json"}
    response = requests.post(
        "http://localhost:8000/new-subscription",
        data={
            "username": "string",
            "monthly_fee": 0,
            "start_date": "2025-09-25T17:51:32.717Z",
        },
        headers=headers,
    )
    print(response.json())


if __name__ == "__main__":
    main()
