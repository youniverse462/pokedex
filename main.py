import streamlit as st
from api import fetch_data

st.title("Pokémon Info App")

name = st.text_input("Name des Pokémons von Interesse?")

if name:
    data = fetch_data(name)
    if data:
        st.header("Informationen")

        # Name
        st.subheader(f"Name: {data['name'].capitalize()}")

        # Gewicht und Größe
        weight = data['weight']
        height = data['height']
        st.write(f"Gewicht: {weight} kg")
        st.write(f"Größe: {height} dm")

        # Fähigkeiten
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        st.write("Fähigkeiten:")
        for ability in abilities:
            st.write(f"- {ability.capitalize()}")

        # Bild wie im pokedex
        
        image_url = data['sprites']['front_default']
        if image_url:
            st.image(image_url, caption=data['name'].capitalize())
    else:
        st.error("Pokémon nicht gefunden. Bitte überprüfe den Namen.")
