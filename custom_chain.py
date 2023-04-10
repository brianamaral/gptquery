from langchain.chains import LLMChain
from langchain.prompts.prompt import PromptTemplate
from langchain.llms import OpenAI

def load_chain():
    _DEFAULT_TEMPLATE = """Given an input question, first create a syntactically correct sqlite query to run, then look at the results of the query and return the answer.
    Use the following format. :
    
    "SQLQuery": "SQL Query to run"
    "TablesUsed": "The tables queried"

    Use this csv that represent the table metadata:

    ColumnName,Description,TableName
    order_id,"unique identifier of the order.",orders
    customer_id,"key to the customer dataset. Each order has a unique customer_id.",orders
    order_status,"Reference to the order status (delivered, shipped, etc).",orders
    order_purchase_timestamp,"Shows the purchase timestamp.",orders
    order_approved_at,"Shows the payment approval timestamp.",orders
    order_delivered_carrier_date,"Shows the order posting timestamp. When it was handled to the logistic partner.",orders
    order_delivered_customer_date,"Shows the actual order delivery date to the customer.",orders
    order_estimated_delivery_date,"Shows the estimated delivery date that was informed to customer at the purchase moment.",orders
    customer_id,"key to the orders dataset. Each order has a unique customer_id.",customers
    customer_unique_id,"unique identifier of a customer.",customers
    customer_zip_code_prefix,"first five digits of customer zip code",customers
    customer_city,"customer city name",customers
    customer_state,"customer state",customers
    order_id,"unique identifier of an order.",orders_payment
    payment_sequential,"a customer may pay an order with more than one payment method. If he does so, a sequence will be created to",orders_payment
    payment_type,"method of payment chosen by the customer.",orders_payment
    payment_installments,"number of installments chosen by the customer.",orders_payment
    payment_value,"transaction value.",orders_payment

    Question: {input}"""

    prompt = PromptTemplate(
        input_variables=["input"], template=_DEFAULT_TEMPLATE
    )

    llm = OpenAI(temperature=0)

    return LLMChain(llm=llm, prompt=prompt)


