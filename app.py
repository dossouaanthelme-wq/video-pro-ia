import streamlit as st

# --- CONFIGURATION ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬")

# --- INTERFACE ---
st.title("🎬 IA Studio Pro : Vidéos 25s")
st.write("Créez vos vidéos cinématographiques avec l'IA.")

# --- BARRE LATÉRALE (SIDEBAR) ---
st.sidebar.header("💳 ACHETER UN ACCÈS")
st.sidebar.write("Pack VIP : **5 000 FCFA**")

# Construction du lien WhatsApp
msg = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA)."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={msg.replace(' ', '%20')}"

# MÉTHODE 100% SÉCURISÉE (Sans HTML complexe)
st.sidebar.write("---")
st.sidebar.markdown(f"### [👉 PAYER PAR WAVE ICI]({lien_wa})")
st.sidebar.write("---")

st.sidebar.info("Cliquez sur le lien bleu ci-dessus pour me contacter sur WhatsApp.")

# --- SECTION GÉNÉRATION ---
st.divider()
code_client = st.text_input("🔑 Entrez votre Code Secret ici :", type="password")

if code_client:
    if code_client == CODE_VALIDE:
        st.success("✅ Code valide !")
        prompt = st.text_area("Décrivez votre vidéo :")
        if st.button("🎥 Lancer la création"):
            st.warning("⏳ Lancement de l'IA en cours...")
    else:
        st.error("❌ Code incorrect.")

st.divider()
st.caption("© 2025 IA Studio Pro")
