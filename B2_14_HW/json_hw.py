def main():
    import json

    with open("data/users.txt", 'r') as file:
        users = json.load(file)
        first_user = None
        last_user = None
        for user in users:
            if first_user is None or user["registered"] < first_user["registered"]:
                first_user = user
            elif last_user is None or user["registered"] > last_user["registered"]:
                last_user = user
    print(first_user)
    print(last_user)


if __name__ == "__main__":
    main()