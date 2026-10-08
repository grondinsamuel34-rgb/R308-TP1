"""Dictionnaire des étudiants : clé = nom (str), valeur = note (float)."""

etudiants: dict[str, float] = {
    "Alice": 15.5,
    "Bob": 12.0,
    "Charlie": 9.75,
}

if __name__ == "__main__":
    for nom, note in etudiants.items():
        print(f"{nom} : {note}")
