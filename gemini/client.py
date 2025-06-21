from google import genai

def iagen(function, cbo):
    # VARIABLES
    MY_KEY = 'AIzaSyAHhH0O1K4lMvfch-4ahkhpgPbhlJ1Y4xo'
    my_activity = function
    my_cbo = cbo
    context_order = f'Gere uma descrição curta para a atividade \
        "{my_activity}" com CBO "{my_cbo}". Essa descrição vai ser inserida em \
        uma descrição da função. Não gere título na resposta.'

    # CLIENT
    client = genai.Client(api_key=MY_KEY)

    response = client.models.generate_content(
        model='gemini-2.0-flash', contents=context_order
    )

    return response.text

if __name__ == '__main__':
    print(iagen(function='auxiliar de saúde bucal', cbo='3224-15'))