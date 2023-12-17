from openai import OpenAI

client = OpenAI()

for numero in range(4, 49):
    url = f"https://raw.githubusercontent.com/paulvl/48img/b7cbfd86f55dc0d60c78cabb19f541a7a7170484/img/ley_{numero}.JPG"
    print(f"Procesando imagen {numero}...")
    response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
        "role": "user",
        "content": [
            {"type": "text", "text": '''
    Extrae el texto en el siguiente formato:
    Ley X

    TITULO LEY

    TEXTO DEL CRITERIO'''},
            {
            "type": "image_url",
            "image_url": {
                "url": url,
            },
            },
        ],
        }
    ],
    max_tokens=300,
    )

    ocred = response.choices[0].message.content
    print("Imagen procesada. Escribiendo en archivo...")
    print("")

    # Abre el archivo en modo "append" (agregar)
    with open("leyes.txt", "a") as archivo:
        texto_a_agregar = f"{ocred}\n-----------------\n"
        archivo.write(texto_a_agregar)