from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv
load_dotenv()

# Initialize the language model

groqAPI = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    model="gemma2-9b-it",
    max_tokens=512,
    temperature=0.1,
    api_key=groqAPI
)

# Set up the retrieval QA chain
def setup_retrieval_qa(db):
    retriever = db.as_retriever(similarity_score_threshold=0.6)

    # Define the prompt template
    prompt_template = """ Your name is TomBot, Please answer questions related to Agriculture. Try explaining in simple words. Answer in less than 150 words. If you don't know the answer, simply respond with 'Don't know.'
     CONTEXT: {context}
     QUESTION: {question}"""

    PROMPT = PromptTemplate(template=f"[INST] {prompt_template} [/INST]", input_variables=["context", "question"])

    # Initialize the RetrievalQA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type='stuff',
        retriever=retriever,
        input_key='query',
        return_source_documents=True,
        chain_type_kwargs={"prompt": PROMPT},
        verbose=False
    )
    return chain
