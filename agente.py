from groq import Groq
import streamlit as st
from dotenv import load_dotenv
import os



load_dotenv()


st.title("AGENTE de musica 🎲")



client = Groq(api_key=os.getenv("GROQ_API_KEY"))

pergunta = st.text_input("Digite sua pergunta...")

if pergunta:
    resposta = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "system",
                "content": "Você é um Profissional em música, sabe sobre todos os estilos possíveis e ama todos."
            },
            {
                "role": "user",
                "content": pergunta
            }
        ]
    )
    
    st.write(resposta.choices[0].message.content)
