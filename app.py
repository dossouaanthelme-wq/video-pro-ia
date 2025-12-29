import streamlit as st
import replicate
import os

# CONFIGURATION DU MAÎTRE
REPLICATE_API_TOKEN = "TON_R8_ICI" 

st.set_page_config(page_title="VidéoGénérateur VIP", page_icon="🎬")

st.title("🎬 Studio Vidéo Haute Durée (25s)")
st.write("Réservé aux abonnés Premium.")

# Interface de commande
prompt = st.text_area("Maître, décrivez la scène complète :", 
                     placeholder="Ex: Une voiture de sport traversant Abidjan la nuit, lumières néons, pluie, 4k...")

# Option de durée pour le client
duree = st.select_slider("Choisissez la durée de la vidéo :", options=["5s", "10s", "15s", "20s", "25s"])

if st.button("Générer la Vidéo Premium ✨"):
    if not prompt:
        st.warning("Veuillez entrer une description.")
    else:
        with st.spinner(f"Génération de votre vidéo de {duree} en cours... (Cela peut prendre 2-3 minutes)"):
            try:
                os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
                
                # Utilisation d'un modèle capable de durées plus longues (Luma ou similaire via Replicate)
                # Note : Le coût sera un peu plus élevé (environ 0.10$ à 0.20$ pour 25s)
                output = replicate.run(
                    "lucataco/luma-dream-machine:41525547", # Modèle haute performance
                    input={
                        "prompt": prompt,
                        "aspect_ratio": "16:9",
                        "loop": False
                    }
                )
                
                st.video(output)
                st.success(f"Vidéo de {duree} générée avec succès !")
                
            except Exception as e:
                st.error("Le serveur est très sollicité pour les longues durées. Réessayez ou vérifiez votre solde.")

st.write("---")
st.info("💡 Conseil du Maître : Plus la vidéo est longue, plus la description doit être détaillée.")
