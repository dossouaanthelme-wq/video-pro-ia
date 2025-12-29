import streamlit as st
import replicate
import time

# --- CONFIGURATION DU MAÎTRE ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬")

# --- BARRE LATÉRALE ---
st.sidebar.header("💳 ESPACE PAIEMENT")
st.sidebar.write("Obtenez un code VIP pour générer une vidéo HD.")
msg = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA)."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={msg.replace(' ', '%20')}"
st.sidebar.markdown(f"### [👉 PAYER 5.000F PAR WAVE]({lien_wa})")

# --- INTERFACE PRINCIPALE ---
st.title("🎬 IA Studio Pro")
st.write("Générez des vidéos cinématographiques professionnelles.")

code_client = st.text_input("🔑 Entrez votre Code Secret :", type="password")

if code_client == CODE_VALIDE:
    st.success("✅ Accès VIP activé.")
    
    prompt = st.text_area("Décrivez votre vidéo (en anglais) :", 
                          placeholder="A futuristic car driving through Abidjan, 4k, cinematic...")
    
    if st.button("🎥 LANCER LA GÉNÉRATION"):
        if prompt:
            try:
                # Connexion sécurisée
                api_token = st.secrets["REPLICATE_API_TOKEN"]
                client = replicate.Client(api_token=api_token)
                
                # Lancement de la génération
                with st.spinner("🚀 L'IA travaille... Cela prend 2-4 minutes."):
                    # Utilisation du modèle Stable Video Diffusion ou Luma
                    output = client.run(
                        "stability-ai/stable-video-diffusion:ac7327c2014dba223a6ca27c770337295832334901c137456d2965cc2af8189e",
                        input={"prompt": prompt, "video_length": "25_frames_with_svd_xt"}
                    )
                
                if output:
                    st.video(output)
                    st.balloons()
                    st.success("Terminé !")
            
            except Exception as e:
                st.error(f"Erreur : {e}")
        else:
            st.error("Veuillez écrire une description.")

elif code_client:
    st.error("❌ Code incorrect.")

st.divider()
st.caption("© 2025 IA Studio Pro")
