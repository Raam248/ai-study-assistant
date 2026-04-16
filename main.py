import api
import memory
def main():
    print("Welcome to the chatbot! How can I help you today?")
    while True:
     chat = input(">>> ")
     if chat == "exit":
        print("Thank you for using the chatbot! Goodbye!")
        break
     response = api.get_response(chat)
     messages = memory.load_memory()

     messages.append({"role": "user", "content": chat})
     messages.append({"role": "assistant", "content": response})

     memory.save_memory(messages)
     print(">>>",response)
    
if __name__ == "__main__":
    main()