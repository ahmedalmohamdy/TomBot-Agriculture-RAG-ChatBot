# app.py
from chat1 import embedding_function
from chat2 import  setup_retrieval_qa
from langchain_chroma import Chroma


# call the vector store
db = Chroma(persist_directory="./Agriculture_db", embedding_function=embedding_function)



# Set up the RetrievalQA chain

chain = setup_retrieval_qa(db)

def ask_question(chain):
    first_time = True  

    while True:
        if first_time:
            query = input("🤖 Hello, Ask me Anything About Agriculture or enter q to End Chat \n🧑‍🌾 ").strip().lower()
            first_time = False
        else:
            query = input("🧑‍🌾 You: ").strip().lower()

        if query in ["exit", "q"]:
            print("🤖 Good Bye 👋\n")
            break

        if query in ["who developed you", "who created you", "who made you"]:
            print("\n 🤖 I was developed by CropPiolt Team  ❤️\n")
            continue

        response = chain.invoke(query)
        print(f"\n 🤖 {response['result']} \n")



if __name__ == "__main__":
    ask_question(chain)

    