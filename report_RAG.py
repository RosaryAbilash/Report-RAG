import streamlit as st
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings



st.title("Report RAG")
st.markdown("Powered By LLama 3")

def main():
# Loading Embedding
    embedding = HuggingFaceEmbeddings(
        model_name="../models/all-MiniLM-L6-v2"
    )

    # Loading Vector DB
    vectorDB = FAISS.load_local(
        "Faiss_Report",
        embedding,
        allow_dangerous_deserialization=True
    )


    # Retriever
    retriever = vectorDB.as_retriever(search_kwargs={"k": 2})

    # LLM
    llm = OllamaLLM(model="llama3.2:3b")

    query = st.text_input("Ask a Query")
    if st.button('Ask') and query:
        
        # Augmentation
        docs_context = retriever.invoke(query)
        context = "\n\n".join(d.page_content for d in docs_context)

        answer = ask_question(query, context, llm)
        st.write('Question:', query)
        st.write('Answer:', answer)  


        st.write("Retrieved Context:")
        for d in docs_context:
            st.write(d.page_content)


def ask_question(query, context, llm):

    

    answer = llm.invoke(f"""
        Answer ONLY from the given context. If not found, say 'Not available': {context}
        Question : {query}
    """)
    return answer



if __name__ == '__main__':
    main()











