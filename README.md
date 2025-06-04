# reward-network-mvp
The People's Wealth Engine
# Reward Network MVP – Local Implementation

From Scroll to Soar: This project is a transparent, community-driven reward system where two new winners are selected every month once we reach 1 million TikTok followers.

## 📁 Projektstruktur
```
reward-network-mvp/
├── frontend/
│   └── streamlit_frontend_mvp.py
├── backend/
│   ├── apify_scraper_tiktok.py
│   ├── apify_tiktok_workflow.py
│   ├── webhook_contract_trigger.py
│   └── tiktok_profile_data.json
├── contracts/
│   └── RewardPool.sol
├── data/
│   ├── winner_export.json
│   └── participants_local.json
├── scripts/
│   └── test_draw_logic.py
├── .env
├── requirements.txt
└── README.md
```

## 🔧 Setup
### Voraussetzungen
- Python 3.10+
- Node.js + Solidity Compiler (für Smart Contract Testing)

### Installation
```bash
# Repo klonen
git clone https://github.com/youniverse462/reward-network-mvp.git
cd reward-network-mvp

# virtuelle Umgebung aktivieren (optional)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Abhängigkeiten installieren
pip install -r requirements.txt
```

### .env Datei anlegen
```
OPENAI_API_KEY=sk-...
WEB3_PROVIDER=https://...
PRIVATE_KEY=0x...
ACCOUNT_ADDRESS=0x...
CONTRACT_ADDRESS=0x...
```

## 🚀 Ausführung
```bash
# Starte Streamlit UI
streamlit run frontend/streamlit_frontend_mvp.py

# Starte Webhook Listener
python backend/webhook_contract_trigger.py

# Führe TikTok-Follower-Check aus
python backend/apify_tiktok_workflow.py
```

## 📜 Lizenz
MIT – Open Source & Community-powered.

## 🤝 Mitwirken
Starte mit Pull Requests, Issues oder Ideen – dieses Projekt wächst durch kollektive Intelligenz.
