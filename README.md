# 🛡️ BankShield AI – Détection d'Opérations Bancaires Inhabituelles

**Smart Automation Challenge – Sujet 6**  
**Détection de fraude bancaire en temps réel au Maroc**

[![Supabase](https://img.shields.io/badge/Supabase-PostgreSQL%2015-green)](https://supabase.com)
[![Realtime](https://img.shields.io/badge/Realtime-WebSocket-blue)]()
[![License](https://img.shields.io/badge/License-MIT-yellow)]()

---

## 👥 Équipe

| Membre |
|--------|
| **Jihane Majdoul** 
| **Salma Boukhlal** 
| **Yassine Hadrane** 
| **Youssef Ait Bakrim** 
| **Abdelouahed Ahnid** 

**Encadrement** : M. Achmi Gnae Diby

---

## 📌 Description

BankShield AI est un système de **détection en temps réel des opérations bancaires suspectes**, combinant :

- 🎯 **Un moteur de scoring à 12 règles** (temps réel, < 200 ms)
- 🤖 **Un Agent IA AML** (Google Gemini) pour le diagnostic bilingue FR/AR
- 📊 **Un dashboard temps réel** (Supabase Realtime + WebSocket)
- 🔔 **Des notifications Slack** instantanées pour les alertes critiques
- 🗄️ **Une base de données Supabase** (PostgreSQL 15) avec 4 tables normalisées

---

## 🎯 Contexte

Sous l'impulsion de **Bank Al-Maghrib (BAM)**, le paysage financier marocain vit une digitalisation accélérée :

- **+150 millions de transactions/an** via le CMI (Centre Monétique Interbancaire)
- **+30% de croissance annuelle** des paiements digitaux
- **85-90% de faux positifs** avec les systèmes à règles statiques
- **24 à 48h de délai** de détection → fonds déjà évaporés

**BankShield AI** répond à ce problème avec une approche temps réel (< 3 secondes) et une réduction drastique des faux positifs (< 15%).

---

## 🏗️ Architecture


🔗 Liens Utiles
🌐 Dashboard en ligne : bankshield-dashboard.vercel.app

