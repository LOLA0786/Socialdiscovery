🌐 Social Discovery

Real-time intent → intelligence platform

Social Discovery is a real-time social discovery system that captures what people are thinking right now, transforms it into live intelligence, and surfaces it to users and brands — without relying on followers, feeds, or historical data.

This is not social media.
This is live intent intelligence.

  What It Does
For Users

Join live discovery rooms around emerging topics

See conversations form in real time

Experience momentum, not history

For Brands

Observe live demand signals

Track trending topics & words

Monitor typing velocity (momentum)

Read AI-generated insights & ideas

Zero PII. Fully privacy-safe.
**
  Core Concept
**
Moments, not posts. Momentum, not likes.

People expressing intent at the same time create ephemeral moments.
Those moments decay, but the insight is captured instantly.

🏗️ Architecture Overview
User Intent
   ↓
Intent Engine
   ↓
Moment Creation (Ephemeral)
   ↓
AI Summary + Signals
   ↓
Brand Intelligence Dashboard

  Monorepo Structure
Socialdiscovery/
├── backend/                   # FastAPI backend
│   ├── app/
│   │   ├── api/               # REST + WebSocket APIs
│   │   ├── services/          # Intent, matching, summary, typing engines
│   │   ├── models/            # SQLAlchemy models
│   │   └── realtime/          # WebSocket room logic
│   └── tests/
│
├── socialdiscovery-frontend/  # Next.js frontend
│   ├── app/
│   │   ├── page.tsx           # Social discovery UI
│   │   └── brand/             # Brand intelligence dashboard
│   └── components/
│
└── README.md

🔧 Backend Features

Intent ingestion (POST /intent)

Ephemeral moments with decay

AI summaries (GET /summary)

Typing velocity / momentum

Brand intelligence APIs

Trending topics

Trending words

AI-derived themes

Opportunity ideas

Stack

FastAPI

SQLite (dev)

WebSockets

AI-ready architecture (LLM pluggable)

Privacy-first by design

  Frontend Features

ChatGPT-style layout

Live discovery rooms

Right-side insight panel

Real-time momentum display

Brand dashboard (/brand)

Stack

Next.js (App Router)

React

Tailwind (optional extension)

WebSocket + polling hybrid

  Privacy & Safety

No user identity tracking

No message storage required

Only aggregated, anonymized signals

Designed for compliance from day one

  Why This Is Different
Traditional Social	Social Discovery
Followers	Live intent
Likes	Momentum
Feeds	Moments
History	Now
Vanity metrics	Demand signals
  Running Locally
Backend
cd backend
python3 -m uvicorn app.main:app --reload

Frontend
cd socialdiscovery-frontend
npm run dev

  Vision

To become the world’s real-time discovery layer —
where ideas, needs, and intent surface the moment they are born.

2026–2030: Social Discovery becomes the default way the world understands what matters now.

  Status

  Active development
Core system working end-to-end
  AI-ready
  Brand monetization layer live





  Social Discovery

Real-time intent → intelligence platform












Moments, not posts. Momentum, not likes.

Social Discovery captures what people are thinking right now, transforms it into live intelligence, and surfaces it to users and brands — without feeds, followers, or historical baggage.

🚀 What It Does
For Users

Discover live topics forming right now

Join ephemeral discovery rooms

See momentum instead of popularity

For Brands

Observe real-time demand signals

Track trending topics & words

Monitor typing velocity (momentum)

Read AI-generated insights & ideas

Zero PII. Fully privacy-safe.

🧠 Core Insight

Intent has a half-life. Capture it before it decays.

Social Discovery treats intent as a real-time signal, not a post to be stored forever.

🏗️ System Architecture (High Level)
┌─────────────┐
│   Users     │
│ (Web / Ext) │
└──────┬──────┘
       │  live intent
       ▼
┌────────────────────┐
│   Intent Engine    │
│  (classification) │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│   Moment Engine    │
│ (ephemeral state)  │
└──────┬─────────────┘
       │
       ▼
┌────────────────────┐
│ AI Summary Engine  │
│ + Signal Extract   │
└──────┬─────────────┘
       │
       ▼
┌─────────────────────────┐
│ Brand Intelligence APIs │
│ trends · momentum · AI  │
└─────────────────────────┘

⚡ Real-Time Layer (Typing & Momentum)
User typing
   ↓ (WebSocket)
Typing Event
   ↓
10s Rolling Window
   ↓
Velocity Score
   ↓
LOW / MEDIUM / HIGH


This creates a momentum signal that brands care about far more than likes or comments.

🧠 Data Philosophy (Privacy-First)
User Text  →  Intent  →  Aggregation  →  Insight
   ❌ PII      ✅ Yes      ✅ Yes         ✅ Yes


No identity tracking

No long-term message storage

Only aggregated signals survive

📦 Monorepo Structure
Socialdiscovery/
├── backend/
│   ├── app/
│   │   ├── api/               # REST + WebSocket APIs
│   │   ├── services/          # Intent, matching, summary, typing engines
│   │   ├── models/            # SQLAlchemy models
│   │   └── realtime/          # WebSocket room logic
│   └── tests/
│
├── socialdiscovery-frontend/
│   ├── app/
│   │   ├── page.tsx           # Social discovery UI
│   │   └── brand/             # Brand intelligence dashboard
│   └── components/
│
└── README.md

🔧 Backend Capabilities

POST /intent — ingest live intent

GET /summary — AI-generated live insight

GET /brand/insights — trends, topics, ideas

GET /typing/{room} — momentum signal

Stack

FastAPI

SQLite (dev)

WebSockets

AI-ready (LLMs pluggable)

Privacy-first by design

🎨 Frontend Capabilities

ChatGPT-style layout

Live discovery rooms

Real-time insight panel

Momentum indicator

Brand dashboard (/brand)

Stack

Next.js (App Router)

React

WebSockets + polling hybrid

💡 Why This Is Different
Traditional Social	Social Discovery
Followers	Live intent
Likes	Momentum
Feeds	Moments
History	Now
Vanity metrics	Demand signals
🧪 Running Locally
Backend
cd backend
python3 -m uvicorn app.main:app --reload

Frontend
cd socialdiscovery-frontend
npm run dev

🌍 Vision

To become the world’s real-time discovery layer —
where ideas, needs, and intent surface the moment they are born.

2026–2030: Social Discovery rules “what’s happening now.”

📬 Status

🚧 Active development
🔥 End-to-end system live
🧠 AI-ready
💰 Brand monetization layer implemented




# Phase-2 verified
