# --- OPTION B : CONTACT WHATSAPP DIRECT ---
mon_numero = "2250XXXXXXXX" # REMPLACEZ PAR VOTRE NUMÉRO SANS LE +
message_auto = "Bonjour Maître, je souhaite acheter un code pour générer ma vidéo VIP (5.000 FCFA)."

st.subheader("💳 Obtenir un Code d'Accès")
st.write("Le paiement se fait par Wave, Orange Money ou MTN.")

if st.button("🚀 Commander mon code via WhatsApp"):
    link = f"https://wa.me/{mon_numero}?text={message_auto.replace(' ', '%20')}"
    st.markdown(f'<a href="{link}" target="_blank" style="text-decoration:none;"><button style="background-color:#25D366;color:white;padding:10px 20px;border:none;border-radius:5px;cursor:pointer;">Cliquez ici pour payer par WhatsApp</button></a>', unsafe_allow_dom=True)
    st.info("Une fois le paiement effectué, je vous enverrai votre code secret immédiatement.")
