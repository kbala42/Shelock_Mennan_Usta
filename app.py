import streamlit as st

# Sayfa Ayarları
st.set_page_config(page_title="Neo-Sherlock AI Academy", layout="wide", page_icon="🕵️‍♂️")

# CSS: Siber-Punk Tema
st.markdown("""
<style>
    .main { background-color: #0e1117; color: #00ff41; }
    h1, h2, h3 { color: #00ff41 !important; font-family: 'Courier New', monospace; }
    .stButton>button { color: #0e1117; background-color: #00ff41; border: none; }
    .stMarkdown { font-family: 'Courier New', monospace; }
</style>
""", unsafe_allow_html=True)

# --- YAN MENÜ ---
st.sidebar.image("https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Sherlock_Holmes_Silhouette.svg/1200px-Sherlock_Holmes_Silhouette.svg.png", width=100)
st.sidebar.title("🕵️‍♂️ GÖREV MENÜSÜ")

# Mennan Usta'nın Defteri (Rehber)
with st.sidebar.expander("📔 Mennan Usta'nın Defteri", expanded=False):
    st.markdown("*Evlat, makine makinedir. Sıkıştığında buraya bak.*")
    st.caption("""
    **Vaka 1:** Çeşme başını tutan, köye hakim olur. (Merkezilik)
    **Vaka 2:** Gürültü kalabalıktır, arıza yalnızdır. (Frekans)
    **Vaka 3:** Hızlı koşan düşer, duran donar. (Learning Rate)
    **Vaka 4:** İki elinle basmazsan pres inmez. (Bias/Ağırlık)
    **Vaka 5:** Üzüm üzüme baka baka kararır. (GNN)
    """)

selection = st.sidebar.radio("Dosya Seç:", 
    ["Ana Üs (Giriş)", 
     "Vaka 1: Hayalet Protokol", 
     "Vaka 2: Dijital Parazit", 
     "Vaka 3: Karanlık Vadi", 
     "Vaka 4: Siber Nöron",
     "Vaka 5: Örümcek Ağı"])

st.sidebar.divider()
st.sidebar.caption("Neo-Baker Street 221B v3.0")

# --- YÖNLENDİRMELER ---
if selection == "Ana Üs (Giriş)":
    st.title("NEO-SHERLOCK AKADEMİSİ")
    st.image("https://miro.medium.com/v2/resize:fit:1400/1*9QT2gEa0v7kO4t5qN2w2sg.jpeg", caption="Siber-Londra 2026")
    st.markdown("""
    ### 🛑 DURUM RAPORU
    **Düşman:** Moriarty Ağı (Merkeziyetsiz Yapay Zeka).
    **Görevin:** Sezgisel Mühendislik yeteneklerini kullanarak ağı çökertmek.
    
    Soldaki menüden **Vaka 1** ile başla. Mennan Usta'nın sezgisi ve Sherlock'un mantığı seninle olsun.
    """)

elif selection == "Vaka 1: Hayalet Protokol":
    try: from cases import case_patient_zero; case_patient_zero.run()
    except ImportError: st.error("Dosya bulunamadı: cases/case_patient_zero.py")

elif selection == "Vaka 2: Dijital Parazit":
    try: from cases import case_whispering_walls; case_whispering_walls.run()
    except ImportError: st.error("Dosya bulunamadı: cases/case_whispering_walls.py")

elif selection == "Vaka 3: Karanlık Vadi":
    try: from cases import case_blind_mountaineer; case_blind_mountaineer.run()
    except ImportError: st.error("Dosya bulunamadı: cases/case_blind_mountaineer.py")

elif selection == "Vaka 4: Siber Nöron":
    try: from cases import case_mind_palace; case_mind_palace.run()
    except ImportError: st.error("Dosya bulunamadı: cases/case_mind_palace.py")

elif selection == "Vaka 5: Örümcek Ağı":
    try: from cases import case_spider_web; case_spider_web.run()
    except ImportError: st.error("Dosya bulunamadı: cases/case_spider_web.py")