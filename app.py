import streamlit as st

# --- CONFIGURATION ---
VOTRE_NUMERO_WA = "2250554178128" 
CODE_VALIDE = "MASTER25"

st.set_page_config(page_title="IA Studio Pro", page_icon="🎬")

# --- INTERFACE ---
st.title("🎬 IA Studio Pro : Vidéos 25s")
st.write("Créez vos vidéos cinématographiques avec l'IA.")

# --- BARRE LATÉRALE ---
st.sidebar.header("💳 ACHETER UN ACCÈS")
st.sidebar.write("Le pack (1 vidéo HD) est à **5 000 FCFA**.")

# Construction du lien WhatsApp
message_wa = "Bonjour Maître, je souhaite acheter un code VIP (5.000 FCFA)."
lien_wa = f"https://wa.me/{VOTRE_NUMERO_WA}?text={message_wa.replace(' ', '%20')}"

# AFFICHAGE DIRECT DU LIEN (Pas de bouton complexe qui fait planter)
st.sidebar.markdown(f"""
<div style="text-align: center;">
    <a href="{lien_wa}" target="_blank" style="text-decoration: none;">
        <div style="background-color: #25D366; color: white; padding: 15px; border-radius: 10px; font-weight: bold; font-size: 18px;">
            💬 PAYER PAR WAVE ICI
        </div>
    </a>
</div>
""", unsafe_allow_dom=True)

st.sidebar.write("") # Espace
st.sidebar.info("Cliquez sur le bouton vert ci-dessus pour me contacter sur WhatsApp et payer par Wave.")

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
