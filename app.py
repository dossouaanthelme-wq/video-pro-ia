import streamlit as st
import replicate
import time

# --- CONFIGURATION DU MAÎTRE ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬", layout="centered")

# --- BARRE LATÉRALE ---
st.sidebar.header("💳 ESPACE PAIEMENT")
st.sidebar.write("Pack VIP : **5 000 FCFA**")
msg = "Bonjour Maître, je souhaite acheter un code VIP."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={msg.replace(' ', '%20')}"
st.sidebar.markdown(f"### [👉 PAYER PAR WAVE]({lien_wa})")
st.sidebar.divider()
st.sidebar.info("Le code secret vous sera envoyé sur WhatsApp après votre transfert Wave.")

# --- INTERFACE PRINCIPALE ---
st.title("🎬 IA Studio Pro")
st.write("Le premier studio de génération vidéo par IA en Côte d'Ivoire.")

# --- SECTION DÉMONSTRATION (AVEC VOTRE VIDÉO) ---
st.subheader("📺 Exemple de ce que notre IA peut créer :")
# Voici votre vidéo YouTube intégrée
st.video("https://youtu.be/q3xaGATnLHk")
st.caption("Vidéo futuriste générée par IA Studio Pro.")

st.divider()

# --- ZONE CLIENT ---
st.subheader("🚀 Prêt à créer votre propre vidéo ?")
saisie = st.text_input("🔑 Entrez votre Code Secret pour débloquer le moteur :", type="password")
code_client = saisie.strip().upper() 

if code_client == CODE_VALIDE:
    st.success("✅ ACCÈS ACTIVÉ. Vous pouvez maintenant utiliser l'IA.")
    
    prompt = st.text_area("Décrivez votre scène (en anglais) :", 
                          placeholder="Ex: A futuristic luxury car driving through Abidjan, 4k, cinematic...")
    
    if st.button("🎥 LANCER LA GÉNÉRATION"):
        if prompt:
            try:
                api_token = st.secrets["REPLICATE_API_TOKEN"]
                client = replicate.Client(api_token=api_token)
                
                with st.spinner("🚀 L'IA travaille... Patientez environ 2 minutes."):
                    # Utilisation du modèle LUMA RAY
                    output = client.run(
                        "luma/ray",
                        input={"prompt": prompt}
                    )
                
                if output:
                    st.video(output)
                    st.balloons()
                    st.download_button("📥 Télécharger en HD", output, file_name="video_ia.mp4")
            
            except Exception as e:
                st.error("Erreur de crédit : Le réservoir de l'IA est vide.")
                st.info("Maître, vous devez ajouter 5$ sur Replicate pour activer la génération automatique.")
        else:
            st.error("Veuillez écrire une description.")

elif saisie:
    st.error("❌ Code incorrect. Cliquez sur 'PAYER PAR WAVE' à gauche pour en obtenir un.")

st.divider()
st.caption("© 2025 IA Studio Pro - Abidjan, Côte d'Ivoire")
