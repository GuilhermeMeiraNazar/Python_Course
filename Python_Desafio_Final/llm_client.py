from openai import OpenAI

# Configuração para o LM Studio local
client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm-studio"
)

def buscar_analise_llm(texto_entrada):
    resposta_do_llm = client_openai.chat.completions.create(
        model="meta-llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system", 
                "content": (
                    "Você é um extrator de dados especializado. Sua única tarefa é converter arquivos TXT em JSON estruturado. "
                    "Responda APENAS o JSON puro, sem saudações ou explicações. "
                    "Cada item deve conter: 'Usuario', 'Resenha Original', 'Resenha_pt-br', 'Avaliacao'. "
                    "Traduza a resenha para Português do Brasil no campo 'Resenha_pt-br'. "
                    "No campo 'Avaliacao', use apenas: 'Positiva', 'Negativa' ou 'Neutra'."
                )
            },
            {
                "role": "user", 
                "content": f"Converta o seguinte conteúdo para o formato JSON solicitado: {texto_entrada}"
            }
        ],
        temperature=0.1,
    )
    # Retorna apenas o texto da resposta (o JSON)
    return resposta_do_llm.choices[0].message.content