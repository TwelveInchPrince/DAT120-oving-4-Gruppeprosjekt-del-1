def lengste_null_sekvens(liste):
    maks_lengde = 0  # Variabel for den maksimale lengden av nullsekvensen
    gjeldende_lengde = 0  # Variabel for den gjeldende lengden av nullsekvensen

    for num in liste:
        if num == 0:
            gjeldende_lengde += 1
        else:
            gjeldende_lengde = 0  # Nullstiller gjeldende lengde hvis vi møter et annet tall enn 0

        # Oppdaterer maks_lengde hvis gjeldende lengde er større
        if gjeldende_lengde > maks_lengde:
            maks_lengde = gjeldende_lengde

    return maks_lengde

min_liste = [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
resultat = lengste_null_sekvens(min_liste)
print("Den lengste sammenhengende nullsekvensen av 0 er:", resultat)
