import api
def main():
    chat = input("How You feeling today?")
    response = api.get_response(chat)
    print(response)

if __name__ == "__main__":
    main()