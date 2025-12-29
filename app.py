import streamlit as st

# --- CONFIGURATION DU MAÎTRE ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬")

# --- STYLE DU BOUTON WHATSAPP ---
# On définit le bouton ici pour éviter les erreurs de syntaxe précédentes
message_whatsapp = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA) pour ma vidéo."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={message_whatsapp.replace(' ', '%20')}"

# --- INTERFACE PRINCIPALE ---
st.title("🎬 IA Studio Pro : Vidéos 25s")
st.write("Transformez vos idées en vidéos cinématographiques grâce à l'IA.")

# --- BARRE LATÉRALE (SIDEBAR) ---
st.sidebar.header("💳 ACHETER UN ACCÈS")
st.sidebar.write("Le pack de génération (1 vidéo HD) est à **5 000 FCFA**.")

# Bouton de redirection simple et efficace
if st.sidebar.button("🚀 PAYER PAR WAVE / WHATSAPP"):
    st.sidebar.markdown(f'<a href="{lien_wa}" target="_blank">Cliquez ici pour ouvrir WhatsApp</a>', unsafe_allow_dom=True)
    st.sidebar.success("Lien prêt ! Cliquez juste au-dessus.")

st.sidebar.info("Après paiement sur Wave, envoyez la capture sur WhatsApp pour recevoir votre code.")

# --- SECTION GÉNÉRATION ---
st.divider()
code_client = st.text_input("🔑 Entrez votre Code Secret ici :", type="password")

if code_client:
    if code_client == CODE_VALIDE:
        st.success("✅ Code valide ! Prêt pour la génération.")
        prompt = st.text_area("Décrivez votre vidéo (ex: Un lion samouraï sous la pluie à Abidjan) :")
        
        if st.button("🎥 Lancer la création de 25 secondes"):
            if prompt:
                st.warning("⏳ Connexion au serveur de génération... (Cela peut prendre 2 à 5 minutes)")
            else:
                st.error("Veuillez décrire votre vidéo.")
    else:
        st.error("❌ Code incorrect. Cliquez sur le bouton à gauche pour en obtenir un.")

# --- PIED DE PAGE ---
st.divider()
st.caption("© 2025 IA Studio Pro - Abidjan, Côte d'Ivoire")
