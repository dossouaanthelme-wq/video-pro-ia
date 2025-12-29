import streamlit as st

# --- CONFIGURATION DU MAÎTRE ---
# REMPLACEZ ICI PAR VOTRE NUMÉRO (Exemple: 2250707070707)
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬")

st.title("🎬 IA Studio Pro : Vidéos 25s")
st.write("Transformez vos idées en vidéos cinématographiques grâce à l'IA.")

# --- SECTION PAIEMENT WHATSAPP ---
st.sidebar.header("💳 ACHETER UN ACCÈS")
st.sidebar.write("Le pack de génération (1 vidéo HD) est à **5 000 FCFA**.")

message_whatsapp = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA) pour ma vidéo."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={message_whatsapp.replace(' ', '%20')}"

# Affichage du bouton WhatsApp stylé
st.sidebar.markdown(f'''
    <a href="{lien_wa}" target="_blank">
        <button style="width:100%; background-color:#25D366; color:white; padding:12px; border:none; border-radius:10px; font-weight:bold; cursor:pointer;">
            🚀 PAYER PAR WAVE / WHATSAPP
        </button>
    </a>
''', unsafe_allow_dom=True)

st.sidebar.info("Après paiement, je vous envoie le code secret ici.")

# --- SECTION GÉNÉRATION ---
st.divider()
code_client = st.text_input("🔑 Entrez votre Code Secret ici :", type="password")

if code_client:
    if code_client == CODE_VALIDE:
        st.success("✅ Code valide ! Prêt pour la génération.")
        prompt = st.text_area("Décrivez votre vidéo (ex: Un lion samouraï sous la pluie à Abidjan) :")
        
        if st.button("🎥 Lancer la création de 25 secondes"):
            if prompt:
                st.warning("⏳ Génération en cours... (Cela peut prendre 2 à 5 minutes)")
                # Ici le code de génération se lancera
            else:
                st.error("Veuillez décrire votre vidéo.")
    else:
        st.error("❌ Code incorrect. Contactez le Maître sur WhatsApp pour en obtenir un.")

# --- PIED DE PAGE ---
st.divider()
st.caption("© 2024 IA Studio Pro - Abidjan, Côte d'Ivoire")
