import api
import memory

def main():
    print("Welcome to the chatbot! How can I help you today?")
    
    while True:
        chat = input(">>> ")
        
        if chat == "exit":
            print("Thank you for using the chatbot! Goodbye!")
            break

        messages = memory.load_memory()

        messages.append({"role": "user", "content": chat})  

        context = [
    {"role": "system", "content": "You are a helpful assistant."},] + messages[-10:]

        
#print the messages sent to the api,only for debugging purposes
#TODO: remove this after debugging
        print("MESSAGES SENT TO API:")
        for m in context:
            print(m)
        print("-"*50)

        response = api.get_response(context)

        messages.append({"role": "assistant", "content": response})

        memory.save_memory(messages)

        print(">>>", response)

if __name__ == "__main__":
    main()