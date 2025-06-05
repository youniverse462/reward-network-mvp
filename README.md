# reward-network-mvp
The People's Wealth Engine

# Whitepaper: The People's Wealth Engine [cite: 1]

**Project Name:** 

The People's Wealth Engine

## Vision

In a world of increasing inequality and digital exhaustion, this project offers a new form of social advancement[cite: 1]. It is a decentralized reward system that redistributes hope, not through elites or institutions, but through the power of a community[cite: 2].

## Problem Statement

* The majority consumes hours of content daily - without value in return[cite: 3].
* Financial opportunities are unequally distributed and often unattainable[cite: 3].
* Trust in traditional systems is dwindling, especially among younger generations[cite: 4].

## Our Solution

A global, blockchain-based network founded on fairness, transparency, and community[cite: 4]. Participants invest \$1 monthly[cite: 5]. Each month, a Smart Contract randomly selects two people to receive \$500,000 each - provided that 1 million people participate[cite: 5].

## System Logic

### Participation

* Monthly contribution: \$1 [cite: 6]
* Identity protection through pseudonymity + optional Proof-of-Humanity (KYC-light) [cite: 6]

### Distribution

* 2 winners per month via Chainlink VRF (Verifiable Random Function) [cite: 6]
* Automated payout via Smart Contract [cite: 6]
* Verification via Public Ledger [cite: 6]

### Community Dashboard

* Countdown to the drawing [cite: 6]
* Drawing history data [cite: 6]
* Gamification: Streaks, XP, extra tickets through engagement [cite: 6]

### Fund Usage

* $\ge95\%$ Prize money [cite: 6]
* $\le5\%$ Operating costs (openly viewable) [cite: 6]
* Optional: 1% Community Impact Fund / Treasury DAO [cite: 6]

## Technological Basis [cite: 6]

* **Blockchain:** Ethereum Layer 2 (e.g., Polygon, Base) [cite: 7]
* **Random Selection:** Chainlink VRF [cite: 7]
* **Frontend:** React Native / Flutter App [cite: 7]
* **Backend:** Supabase / Moralis / Custom Node [cite: 7]
* **Payments:** Stripe, Coinbase Commerce, Gnosis Safe [cite: 7]

## Legal Structure

* DAO structure planned (e.g., Wyoming DAO LLC or Liechtenstein model) [cite: 7]
* Regulatory framework for micropayments, lottery demarcation, KYC [cite: 7]

## Market Potential

* TikTok has >1 billion active users - our MVP only needs 1 million[cite: 7, 8].
* Viral network building through participatory stories[cite: 8].
* Monetization through Freemium, Referral-Rewards, Treasury participations[cite: 8].

## Roadmap (Phase 0-1)

1.  Mission & Community building (Telegram, Discord, TikTok) [cite: 8]
2.  MVP development (Smart Contract + Dashboard) [cite: 8]
3.  Security Audit & Public Launch [cite: 8]
4.  First drawings, viral campaigns [cite: 8]

## Conclusion

This project is more than a game[cite: 9]. It is a radical counter-design to the status quo - a social financial system that doesn't promise advancement, but delivers it[cite: 9]. Month after month. Person by person[cite: 10].

Two new millionaires per month. A new feeling of: I could be next[cite: 10].
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
