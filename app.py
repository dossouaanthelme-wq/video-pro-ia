import streamlit as st
import replicate
import time

# --- CONFIGURATION DU MAÎTRE ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

# Configuration de la page
st.set_page_config(page_title="IA Studio Pro", page_icon="🎬", layout="centered")

# --- BARRE LATÉRALE ---
st.sidebar.header("💳 ESPACE PAIEMENT")
st.sidebar.write("Pack VIP : **5 000 FCFA**")
msg = "Bonjour Maître, je souhaite acheter un code VIP."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={msg.replace(' ', '%20')}"
st.sidebar.markdown(f"### [👉 PAYER PAR WAVE]({lien_wa})")
st.sidebar.divider()
st.sidebar.info("Après paiement, entrez votre code secret au milieu de l'écran.")

# --- INTERFACE PRINCIPALE ---
st.title("🎬 IA Studio Pro")
st.write("Créez des vidéos cinématographiques professionnelles en quelques minutes.")

# Saisie du code
saisie = st.text_input("🔑 Entrez votre Code Secret :", type="password")
code_client = saisie.strip().upper() 

if code_client == CODE_VALIDE:
    st.success("✅ Accès VIP activé. Le moteur est prêt.")
    
    prompt = st.text_area("Décrivez votre vidéo (en anglais pour un meilleur résultat) :", 
                          placeholder="Ex: A cinematic flyover of Abidjan at night, neon lights, 4k, hyper-realistic...")
    
    if st.button("🎥 LANCER LA GÉNÉRATION"):
        if prompt:
            try:
                # Récupération sécurisée du Token dans les secrets
                api_token = st.secrets["REPLICATE_API_TOKEN"]
                client = replicate.Client(api_token=api_token)
                
                with st.spinner("🚀 L'IA travaille... Patientez environ 120 secondes."):
                    # Utilisation du modèle LUMA RAY (Le plus puissant actuellement)
                    output = client.run(
                        "luma/ray",
                        input={"prompt": prompt}
                    )
                
                if output:
                    # Affichage du résultat final
                    st.video(output)
                    st.balloons()
                    st.success("Vidéo terminée ! Vous pouvez faire un clic droit pour l'enregistrer.")
                    st.download_button("📥 Télécharger la vidéo HD", output, file_name="ma_video_pro.mp4")
            
            except Exception as e:
                # Si l'erreur 422 revient, c'est probablement un manque de fonds sur Replicate
                st.error(f"Oups ! Une erreur est survenue : {e}")
                st.info("💡 Maître, vérifiez que votre compte Replicate est bien crédité d'au moins 5$.")
        else:
            st.error("Veuillez entrer une description pour votre vidéo.")

elif saisie:
    st.error("❌ Code incorrect. Contactez le Maître sur WhatsApp.")

# Pied de page
st.divider()
st.caption("© 2025 IA Studio Pro - Service Premium")
