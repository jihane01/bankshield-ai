# Architecture BankShield AI

## 🏗️ Vue d'ensemble

BankShield AI est un système de détection de fraude bancaire en temps réel, composé de **3 couches** :
┌─────────────────────────────────────────────────────────────┐
│ SIMULATION / SOURCES DE DONNÉES │
│ (Postman / Webhook / Cron / API bancaire) │
└──────────────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ WORKFLOW FUSION AI  │
│ │
│ 1. Ingestion transactions (is_cheked = false) │
│ 2. Enrichissement client (customers) │
│ 3. Scoring 12 règles (RG-01 → RG-12) │
│ 4. Diagnostic IA bilingue (Google Gemini) │
│ 5. Insertion risk_evaluations + fraud_alerts │
│ 6. Notification Slack │
└──────────────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ SUPABASE (PostgreSQL 15) │
│ │
│ ┌──────────────┐ ┌──────────────────┐ │
│ │ customers │───▶│ transactions │ │
│ │ (20 lignes) │ │ (100 lignes) │ │
│ └──────────────┘ └────────┬─────────┘ │
│ │ │
│ ┌──────────┴──────────┐ │
│ ▼ ▼ │
│ ┌──────────────────┐ ┌──────────────┐ │
│ │ risk_evaluations │ │ fraud_alerts │ │
│ └──────────────────┘ └──────────────┘ │
│ │
│ Realtime activé sur : transactions, fraud_alerts, │
│ risk_evaluations │
└──────────────────────────────┬──────────────────────────────┘
│
▼
┌─────────────────────────────────────────────────────────────┐
│ DASHBOARD BANKSHIELD AI (HTML/JS) │
│ │
│ • Écoute Realtime (WebSocket) │
│ • 7 KPIs temps réel │
│ • Graphiques (évolution, répartition, règles) │
│ • Tableau des alertes + arbitrage analyste │
└─────────────────────────────────────────────────────────────┘