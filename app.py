import streamlit as st
import replicate
import os

# Remplace les xxxx par ta clé Replicate r8_...
REPLICATE_API_TOKEN = "TA_CLE_R8_ICI" 

st.set_page_config(page_title="VidéoGénérateur Pro", page_icon="🎬")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 25px; height: 3.5em; background-color: #6C63FF; color: white; font-weight: bold; border: none; }
    .wa-btn { background-color: #25D366; color: white; padding: 15px; text-align: center; border-radius: 25px; display: block; text-decoration: none; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("🎬 VidéoGénérateur Pro")
st.subheader("Créez des clips vidéos uniques avec l'IA")

# Système de crédit gratuit
if 'video_done' not in st.session_state:
    st.session_state.video_done = False

prompt = st.text_area("Maître, décrivez la vidéo à générer :", placeholder="Ex: Un lion qui marche sous la pluie en slow motion...")

if st.button("Lancer la création Vidéo 🚀"):
    if not prompt:
        st.warning("Veuillez entrer une description.")
    elif st.session_state.video_done:
        st.error("❌ Essai gratuit terminé !")
    else:
        with st.spinner("Le serveur Pro génère votre film..."):
            try:
                os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_TOKEN
                # Utilisation du modèle Stable Video Diffusion
                output = replicate.run(
                    "stability-ai/stable-video-diffusion:3f0457a4",
                    input={"prompt": prompt}
                )
                st.video(output[0])
                st.session_state.video_done = True
                st.success("Vidéo terminée ! Passez VIP pour continuer.")
            except:
                st.error("Vérifiez votre solde sur Replicate.")

st.write("---")
st.markdown(f'<a href="https://wa.me/2250554178128" class="wa-btn">Commander un pack Vidéo (WhatsApp)</a>', unsafe_allow_html=True)
