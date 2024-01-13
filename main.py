from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_community.llms import AI21
from langchain_community.document_loaders import PyPDFLoader
from flask import Flask

app = Flask(__name__)



AI21_API_KEY = "iXThS2R7XxGxo6ABgrqN0HLlzj7ET2fw"

# template = """Question: {question}

# Answer: Let's think step by step."""

# prompt = PromptTemplate(template=template, input_variables=["question"])

# llm = AI21(ai21_api_key=AI21_API_KEY)

# llm_chain = LLMChain(prompt=prompt, llm=llm)

# question = "What NFL team won the Super Bowl in the year Justin Beiber was born?"

# res = llm_chain.invoke(question)
# print(res)


def fetch_document(pdf_link):
    loader = PyPDFLoader(pdf_link)
    pages = loader.load_and_split()
    for page in pages:
        print(len(page.page_content))
    

def summarize_document():  
    pass

fetch_document("https://suresuccess.ng/wp-content/uploads/2021/04/the-life-changer-jamb-novel-pdf.pdf")


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"



if __name__ == "__main__":
    app.run(debug=True)