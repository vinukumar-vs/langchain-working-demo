import openai;
from envVariables import getEnv;
from langchain_openai import ChatOpenAI;
from langchain_core.prompts import ChatPromptTemplate;
from langchain_core.output_parsers import StrOutputParser

output_parser = StrOutputParser()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are world class technical documentation writer."),
    ("user", "{input}")
])
openaiKey = getEnv("OPENAI_API_KEY")
print("openaiKey:", openaiKey)

llm = ChatOpenAI(openai_api_key=openaiKey)



def getData(input):
    chain = prompt | llm | output_parser
    response = chain.invoke(input)
    print(response)
