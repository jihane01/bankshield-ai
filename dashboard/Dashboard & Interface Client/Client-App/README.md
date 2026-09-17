# 📱 BankShield Pay — Application Mobile de Simulation Client

> **Projet :** BankShield AI — Moteur d'évaluation des risques et détection de fraude en temps réel (Sujet 6)  
> **Formation :** Gen AI & IoT — Tronc Commun (Smart Automation Challenge)  
> **Équipe de Réalisation :** Jihane Majdoul, Salma Boukhlal, Abdelouahed Ahnid, Yassine Hadrane, Youssef Ait Bakrim  
> **Document Word Officiel :** [`DOCUMENTATION_CLIENT_APP.docx`](./DOCUMENTATION_CLIENT_APP.docx) et [`Livrables/DOCUMENTATION_CLIENT_APP.docx`](../../Livrables/DOCUMENTATION_CLIENT_APP.docx)

---

## 1. Vue d'Ensemble & Objectifs

Le module **Client-App** constitue le simulateur applicatif mobile client de la solution **BankShield AI**. Il reproduit fidèlement l'interface d'une application bancaire moderne sur smartphone (iOS / Android) permettant d'initier et d'injecter des transactions financières vers la base PostgreSQL managée (Supabase) et vers l'orchestrateur de détection de fraude en temps réel (AbaFusion AI).

### Fichiers du Module :
1. [`index.html`](./index.html) : Application web monopage (SPA) sans framework lourd (Tailwind CSS CDN, FontAwesome, JavaScript ES6+ natif).
2. [`cors_proxy.py`](./cors_proxy.py) : Serveur mandataire HTTP (Port 8001) résolvant de manière transparente les blocages CORS du navigateur lors de l'appel au webhook Fusion AI.

---

## 2. Fonctionnalités Clés de l'Application Mobile

- **Châssis Smartphone Virtuel :** Encadrement réaliste aux dimensions iPhone 15 Pro avec encoche Dynamic Island / Notch, barre d'état dynamique (horloge temps réel, batterie, WiFi).
- **Synchronisation Dynamique des Clients :** Connexion directe à l'API REST Supabase (`customers`) pour charger les 10 profils marocains réels (`CUST-1001` à `CUST-1010`) et basculer de profil en 1 clic.
- **Carte Virtuelle Personnalisée :** Affiche le solde en MAD, le plafond journalier, le RIB sur 24 chiffres, le nom du titulaire, le CIN, le terminal habituel et les bénéficiaires favoris.
- **Moteur de Routage Triple-Mode :**
  - `Base de Données Seule` : Écriture SQL directe dans la table `transactions` via Supabase REST API.
  - `Webhook Seul` : Envoi direct du payload JSON vers l'orchestrateur Fusion AI.
  - `Les Deux` : Envoi simultané aux deux cibles pour synchronisation intégrale.
- **7 Scénarios Démo Jury en 1 Clic :**
  1. *🛒 1. Marjane :* 350 MAD, Pos Terminal, Normal (Score 0/100, Approuvé).
  2. *🚨 2. Dakar Nuit :* 22 000 MAD, Virement Web, Déplacement impossible Haversine (2380 km en 15m), Réseau Tor (Score 100/100, Bloqué).
  3. *⚡ 3. Binance P2P :* 28 000 MAD, Virement Web, Risque Crypto P2P à 02h45 du matin, dépassement du plafond journalier (Score 90/100, Bloqué).
  4. *📺 4. Electroplanet :* 7 990 MAD, TPE Carte, Faux positif éliminé grâce à la saisie du code PIN physique à Casablanca (Score 25/100, Approuvé).
  5. *🏨 5. Hôtel Agadir :* 3 200 MAD, TPE Carte, Saut géographique Fès -> Agadir en 2h (Score 45/100, Défi 2FA SMS).
  6. *🛍️ 6. US E-Commerce :* 6 400 MAD, Paiement Web international (Score 55/100, Défi 2FA OTP).
  7. *📱 7. SIM-Swap Dakar :* 18 500 MAD, Virement Web après changement suspect de terminal (Score 95/100, Fraude Confirmée).
- **Inspecteur de Payload JSON :** Visualisation en temps réel de la structure exacte du message JSON transmis.
- **Résilience & Fallback SQL :** Création garantie de la transaction dans Supabase afin d'éviter toute violation de clé étrangère (`SQL 23503`) dans `fraud_alerts`.

---

## 3. Guide de Démarrage Rapide

### 1. Lancer le Proxy CORS (Port 8001)
```bash
cd Main_Project/Client-App
python cors_proxy.py
```

### 2. Lancer le Serveur Web Local (Port 8000)
Dans un second terminal :
```bash
cd Main_Project/Client-App
python -m http.server 8000
```

### 3. Accéder au Simulateur
Ouvrir un navigateur web à l'adresse :
👉 **`http://localhost:8000/index.html`**
