import streamlit as st
import replicate
import time

# --- CONFIGURATION DU MAÎTRE ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬", layout="centered")

# --- STYLE ---
st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #FF4B4B; color: white; }
    </style>
    """, unsafe_allow_dom=True)

# --- BARRE LATÉRALE ---
st.sidebar.header("💳 ESPACE PAIEMENT")
st.sidebar.write("Obtenez un code VIP pour générer une vidéo HD de 25s.")
msg = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA)."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={msg.replace(' ', '%20')}"
st.sidebar.markdown(f"### [👉 PAYER 5.000F PAR WAVE]({lien_wa})")
st.sidebar.info("Le code vous est envoyé immédiatement après le transfert.")

# --- INTERFACE PRINCIPALE ---
st.title("🎬 IA Studio Pro")
st.subheader("Générez des vidéos cinématographiques")

code_client = st.text_input("🔑 Entrez votre Code Secret :", type="password")

if code_client == CODE_VALIDE:
    st.success("✅ Accès VIP activé. L'IA est prête.")
    
    prompt = st.text_area("Décrivez votre vidéo en détail (en anglais pour de meilleurs résultats) :", 
                          placeholder="Ex: A futuristic car driving through Abidjan at night, cinematic lighting, 4k...")
    
    if st.button("🎥 LANCER LA GÉNÉRATION"):
        if prompt:
            try:
                # Connexion au jeton que vous avez mis dans les Secrets
                client = replicate.Client(api_token=st.secrets["REPLICATE_API_TOKEN"])
                
                with st.status("🚀 L'IA prépare votre vidéo...", expanded=True) as status:
                    st.write("Analyse de la demande...")
                    
                    # On utilise le modèle Luma Ray (très haute qualité)
                    prediction = client.models.predictions.create(
                        version="luma/ray",
                        input={"prompt": prompt}
                    )
                    
                    # Attente de la fin de la génération
                    while prediction.status != "succeeded":
                        time.sleep(2)
                        prediction.reload()
                        if prediction.status == "failed":
                            st.error("Désolé, la génération a échoué. Réessayez.")
                            break
                    
                    status.update(label="✅ Vidéo générée avec succès !", state="complete", expanded=False)
                
                # Affichage et téléchargement
                video_url = prediction.output
                st.video(video_url)
                st.balloons()
                st.download_button("📥 Télécharger la vidéo HD", video_url, file_name="ma_video_ia.mp4")
                
            except Exception as e:
                st.error(f"Erreur de connexion : {e}")
                st.info("Vérifiez que vous avez bien ajouté le jeton REPLICATE_API_TOKEN dans les Secrets de Streamlit.")
        else:
            st.error("Veuillez entrer une description avant de lancer.")

elif code_client:
    st.error("❌ Code incorrect. Contactez le Maître sur WhatsApp pour en obtenir un valide.")

# --- PIED DE PAGE ---
st.divider()
st.caption("© 2025 IA Studio Pro - Service Premium")
