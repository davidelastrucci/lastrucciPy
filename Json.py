import json

libri = {
    "comico" : {"titolo":"Guida_galattica_per_autostoppisti","autore":"Douglas_Adams","casa editrice":"PanBook","prezzo":"11,87$"},
    "horror" : {"titolo":"IT","autore":"Stephen_King","casa editrice":"Vicking_Press","prezzo":"17,50$"},
    "fantascienza" : {"titolo":"Io_robot","autore":"Isaac_Asimov","casa editrice":"Gnome_press","prezzo":"8$"},
    "avventura": {"titolo":"Viaggio_al_centro_della_terra","autore":"Jules_Verne","casa editrice":"Pierre-Jules_Hetzel","prezzo":"8,55$"},
    "giallo" : {"titolo":"Uno_studio_in_rosso","autore":"Conan_doyle","casa editrice":"Ward_Lock_&_Co","prezzo":"7,40$"},
    "fantasy" : {"titolo":"Harry_Potter","autore":"J.K_Rowling","casa editrice":"Bloomsbury_Publishing_Plc","prezzo":"15,45$"},
    "romantico" : {"titolo":"Orgoglio_e_Pregiudizio","autore":"Jane_Austen","casa editrice":"Thomas_Egerton","prezzo":"8$"},
    "classico" : {"titolo":"Se_questo_è_un_uomo","autore":"Primo_Levi","casa editrice":"Giulio_Einaudi","prezzo":"6,99$"},
    "narrativo" : {"titolo":"L'amico_ritrovato","autore":"Fred_Uhlman","casa editrice":"Feltrinelli","prezzo":"11$"},
    "fiaba" : {"titolo":"Pollicino","autore":"Charles_Perrault","casa editrice":"Giunti","prezzo":"13,52$"},
}


with open("data.json", "w") as f:
    json.dump(libri, f)

f.close()

# estrapolo da file

with open("data.json", "r") as f:
    dati_da_file = json.load(f)

f.close()

print("stampa il file intero: ",dati_da_file)