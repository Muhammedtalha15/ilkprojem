meme_dict = {

    "LOL": "Komik bir şeye verilen cevap",

    "CRINGE": "Garip ya da utandırıcı bir şey",

    "ROFL": "Bir şakaya karşılık verilen cevap (gülmekten yerlere yatmak)",

    "SHEESH": "Onaylamamak veya şaşkınlık belirtmek",

    "CREEPY": "Korkunç, ürkütücü",

    "AGGRO": "Agresifleşmek, sinirlenmek"

}

 

word = input("Anlamadığınız bir kelime yazın: ").upper()

 

if word in meme_dict:

    print(meme_dict[word])

else:

    print("Bu kelime sözlükte bulunmuyor.")
