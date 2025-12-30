# SocialDiscovery — Intent-Governed Social Discovery

SocialDiscovery is a privacy-first social discovery system built around **explicit intent**, not followers or engagement metrics.

## Core Idea
Every discovery action (recommend, match, trend) is expressed as a **normalized intent** and evaluated by a deterministic policy engine **before execution**.

This enables:
- Replayable decisions
- Shadow-mode safety
- Policy-based control
- Auditability by design

## Architecture
- Intent emission (discovery layer)
- Intent evaluation (policy engine)
- Shadow / allow / block modes
- Tamper-evident audit log
- Deterministic replay

## Current Status
- Shadow-mode intent engine
- Deterministic policy evaluation
- Replay CLI
- Synthetic simulation tests

## Not Yet Included
- Blocking enforcement (intentional)
- UI coupling (intent is backend-first)
- Identity-based heuristics

## Philosophy
> Don’t explain decisions. Prove them.

Built for trust, not engagement.
## SocialDiscovery: Deterministic Discovery Infrastructure

SocialDiscovery is not a ranking algorithm.
It is a **policy-driven discovery system** designed to make social recommendation
**auditable, replayable, and abuse-resilient**.

### Core Principles

#### 1. Determinism over heuristics
Every discovery decision is reproducible from inputs.
No hidden state. No stochastic ML behavior.

#### 2. Signals ≠ Decisions
We strictly separate:
- **Signals** (velocity, decay, social distance)
- **Decisions** (ALLOW, SOFT_BLOCK)

This prevents over-blocking and enables transparent tuning.

#### 3. Velocity beats identity
Abuse is detected via **rate-of-change**, not user identity.
This resists bots, Sybil attacks, and coordinated spam without KYC.

#### 4. Warm-up is mandatory
New content must be allowed to explore.
Cold-start suppression is treated as a system failure.

#### 5. Replay is a first-class feature
Every decision can be replayed offline to answer:
“What did the system know at the time?”

---

## Discovery Policy Overview

All discovery decisions flow through a single policy:

- **Velocity Gate**  
  Detects unnatural engagement spikes (bot resistance)

- **Decay Gate (with warm-up)**  
  Prevents stale content dominance without killing new posts

- **Social Distance Signal**  
  Used for ranking and UI context, never as a hard block

The unified policy lives in:
`core/trending_policy.py`

---

## What This Is (and Isn’t)

✔ Infrastructure for Trust & Safety  
✔ Deterministic, auditable decision-making  
✔ Suitable for social, marketplaces, fintech, and ads  

✘ Not a black-box recommender  
✘ Not engagement-maximizing ML  
✘ Not identity-based moderation  

This system is designed to be *trusted*, not merely effective.
