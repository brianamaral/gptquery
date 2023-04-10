from langchain.chains import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI

def load_chain():
    _DEFAULT_TEMPLATE = """Given an input question, define what tables will be used in sql query and return the answer. The possible tables are: orders, customers, orders_payment
    Return the used table names separated by comma.
    
    Question: {input}"""

    prompt = PromptTemplate(
        input_variables=["input"], template=_DEFAULT_TEMPLATE
    )

    llm = OpenAI(temperature=0)

    return LLMChain(llm=llm, prompt=prompt)

chain = load_chain()

user_input = input("What is your question? ")

print(chain.run(user_input))


