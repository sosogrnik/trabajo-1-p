meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "CREEPY": "aterrador, siniestro",
            "SHEESH": "ligera desaprobación",
            "ROFL": "una respuesta a una broma",
            }
for i in range(5):
    word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
    if word in meme_dict.keys():
        print ("Esta palabra si existe" + word + meme_dict[word] )
    else:
        print ("la palabra no se encuentra")
