import ollama

def get_response(context):
    response = ollama.chat(
        model='llama3',
        messages= context
    )

    return response['message']['content']