import requests

def fetch_random_user():
    url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
    response = requests.get(url)
    fetched_data = response.json()

    # success is object within data but data is a tree of itself within fetched_data

    if fetched_data["success"] and "data" in fetched_data:
        user_data = fetched_data["data"]
        user_login = user_data["login"]["username"]
        user_coordinates = user_data["location"]["coordinates"]["latitude"]
        return user_login, user_coordinates
    else:
        raise Exception("Failed to fetch data!!")

def main():
    try:
        username,coordinates = fetch_random_user()
        print(f"Username:{username}\nCoordinates:{coordinates}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()