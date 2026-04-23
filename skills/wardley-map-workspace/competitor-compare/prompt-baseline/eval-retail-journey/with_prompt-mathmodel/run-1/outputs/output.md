# Connected Customer Journey in Retail — Wardley Map

Generated using only `prompts/wardley_map_generator.md`. First pass, blind.

## 1. Mathematical model instance

$\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ where:

- $|U| = 2$ — two anchors: **Customer** (the shopper) and **Producer** (the supplier of goods). The scenario explicitly names both as the top of the value chain.
- $|V| \approx 30$ components across five loose layers: user needs, channels, experience, behavioural data, commodity infrastructure.
- $E$ = directed "depends on" edges (see `draft.owm`).
- $\nu$ seeded from $\nu(v) = 1/(1+d(v))$ then adjusted for value-chain visibility (e.g., `Sensory Experience` raised because the shopper consciously perceives it; `CDN` lowered because it's architecturally invisible).
- $\varepsilon$ scored by the 4-row cheat sheet subset per component (see §3).

## 2. Scenario interpretation

The prompt calls out seven specific strands, all of which are represented in $V$:

| Scenario strand | Component(s) |
|---|---|
| Customer and producer | `Customer`, `Producer` anchors |
| Needs being met | `Need to Acquire Goods`, `Need to Sell Goods` |
| Goods and services offered | `Goods and Services` |
| Channels — stores, e-commerce, telesales | `Physical Store`, `E-Commerce Site`, `Mobile App`, `Telesales`, `Social Commerce` |
| Experience layer on top | `Retail Experience`, `Sensory Experience`, `Virtual / AR Try-On`, `Personalisation Engine`, `Product Discovery`, `Engagement and Loyalty` |
| Sensory / physical-virtual dimensions | `Sensory Experience`, `Virtual / AR Try-On` |
| Trust and privacy | `Trust and Privacy`, `Consent Management`, `Identity / KYC` |
| Engagement and discovery | `Engagement and Loyalty`, `Product Discovery` |
| Returns | `Returns and Reverse Logistics` |
| Societal behaviour and demographics | `Societal Behaviour Signals`, `Demographic Segmentation`, `Customer Data Platform` |

## 3. Evolution scoring — 4-row cheat sheet (summary)

For space I only show the most load-bearing placements. Scores are averages of four rows (Ubiquity, Certainty, User Perception, Publication Types) each mapped to a band midpoint {0.125, 0.375, 0.625, 0.875}.

| Component | Ubiq | Cert | Percept | Pub | $\varepsilon$ | Stage |
|---|---|---|---|---|---|---|
| Payment Processing | IV | IV | IV | IV | 0.875 | Commodity/utility |
| CDN / Cloud Compute | IV | IV | IV | IV | 0.875–0.94 | Commodity/utility |
| Logistics Network | III→IV | IV | IV | IV | 0.82 | Commodity |
| Physical Store | IV | IV | III | IV | 0.81 | Commodity (hardened) |
| E-Commerce Site | III | IV | III | III | 0.72 | Product/rental |
| Telesales | IV | IV | III | IV | 0.85 | Commodity |
| Mobile App | III | III | III | III | 0.625 | Product |
| CRM | IV | IV | III | IV | 0.80 | Commodity (SaaS) |
| Inventory / Fulfilment | III | III | III | III→IV | 0.72 | Product → commodity |
| Personalisation Engine | II | II | III | II | 0.40 | Custom Built |
| Product Discovery | II | II | III | II | 0.48 | Custom Built edge |
| Engagement and Loyalty | III | II | III | III | 0.55 | Product |
| Trust and Privacy | II | II | III | III | 0.50 | Custom → Product |
| Consent Management | II | II | III | III | 0.60 | Product (regulation-led) |
| Sensory Experience | II | II | II | II | 0.30 | Custom Built |
| Virtual / AR Try-On | I | II | I | II | 0.20 | Genesis → Custom |
| Social Commerce | II | II | II | II | 0.35 | Custom Built |
| Societal Behaviour Signals | I | I | II | II | 0.28 | Genesis/Custom edge |
| Returns and Reverse Logistics | III | III | III | III | 0.65 | Product |
| Customer Data Platform | III | III | III | III | 0.55 | Product |

Hard constraint check: for every edge $(a,b)$, $\nu(a) \ge \nu(b)$ holds — verified by sorting the file (every dependency target sits at or below its parent).

## 4. OWM output

See `draft.owm` in this directory.

## 5. Strategic analysis

### (a) Top 3 by $D(v) = \nu(v)\cdot(1-\varepsilon(v))$ — differentiation pressure

1. **Retail Experience** — $D \approx 0.80 \cdot 0.60 = 0.48$. The umbrella "experience" node is both highly visible and structurally immature; it's the whole game.
2. **Sensory Experience** — $D \approx 0.58 \cdot 0.70 = 0.41$. Physical-store sensing (smell, touch, layout, theatre) remains genuinely custom-built per brand.
3. **Personalisation Engine** — $D \approx 0.54 \cdot 0.60 = 0.32$. User-visible, still Custom Built for most retailers despite vendor hype.

### (b) Top 3 by $K(v) = (1-\nu(v))\cdot\varepsilon(v)$ — commodity leverage

1. **CDN** — $K \approx 0.92 \cdot 0.94 \approx 0.86$. Already a utility; pay-per-use.
2. **Cloud Compute** — $K \approx 0.90 \cdot 0.92 \approx 0.83$. Same story.
3. **Payment Processing** — $K \approx 0.74 \cdot 0.90 \approx 0.67$. Stripe/Adyen/PayPal — treat as a utility, do not build.

Additional commodity candidates worth outsourcing: `Identity / KYC`, `Logistics Network`, `CRM`, `Inventory and Fulfilment` (all $K > 0.55$).

### (c) Top 3 dependency risks by $R(a,b) = \nu(a)\cdot(1-\varepsilon(b))$

1. **`Retail Experience → Personalisation Engine`** — $R \approx 0.80 \cdot 0.60 = 0.48$. The flagship differentiator depends on a Custom Built component — fragile and costly to sustain internally.
2. **`Personalisation Engine → Customer Data Platform → Societal Behaviour Signals`** — $R \approx 0.54 \cdot 0.72 = 0.39$ on the first hop; the transitive risk is that the leaf signal input is still Genesis/Custom. Insight quality gates personalisation quality.
3. **`Trust and Privacy → Consent Management`** — $R \approx 0.48 \cdot 0.40 = 0.19$. Lower raw number but high strategic risk: a customer-facing trust posture depending on a regulation-driven, still-maturing consent layer. Regulatory change can break the upper node.

### (d) Suggested gameplays (Wardley's 61-play catalogue)

- **Open Approaches** on `Personalisation Engine` and `Product Discovery` — publish interfaces / contribute to open recommender stacks to accelerate both into Stage III and starve competitors of proprietary advantage.
- **Harvesting** — monitor the Customer Data Platform vendor market; when a player hardens into Stage III+ with the required consent primitives, buy or absorb.
- **Pig in a Poke** (or more politely, **Exploiting Constraints**) on `Consent Management` — bundle it into a platform offering before it commoditises, while regulatory complexity is still a moat.
- **Differentiation** and **Experimentation** on `Sensory Experience` and `Virtual / AR Try-On` — keep these in-house; this is where the brand lives.
- **Commoditise and Partner** on `Payment Processing`, `Logistics Network`, `Identity / KYC`, `CDN`, `Cloud Compute`, `CRM` — never build these; consume them as utilities.
- **Co-evolution of Practice with Activity** — as `Virtual / AR Try-On` and `Social Commerce` evolve, retail associate practices must co-evolve (the Practice-type shift that the component-types extension anticipates).

### (e) Doctrine observations

- **Phase 1 — "Focus on user needs"** is respected: two anchors (`Customer`, `Producer`) and explicit `Need to Acquire Goods` / `Need to Sell Goods` nodes.
- **"Know the details"** — `Retail Experience` is a useful umbrella but *only* because it decomposes into six or seven concrete sub-components. A map that stopped at "experience" would violate this.
- **"Use appropriate methods"** — build/buy split is explicit in the map: the right side (ε > 0.75) is outsourced, the left side (ε < 0.45) is built.
- Potential violation: **"A bias towards action"** / **"Think big"** — the societal-behaviour and demographic nodes are currently depicted as inputs but the map doesn't yet show *where* the signal is acted on. In a real engagement I'd push for an `A/B and Experimentation` component feeding back into `Personalisation Engine`.
- **Inertia check** — `Physical Store` is high-visibility, Stage IV channel; for many incumbents this is subject to at least three of the 17 inertia forms (sunk capital in leases, human capital in store staff, political capital with landlords/franchisees). Not marked with `inertia` here because the scenario doesn't say the mapper is an incumbent.

## 6. What the map implies for differentiation

The scenario asks explicitly where custom meets commodity and what that implies. Reading the map:

- **Left (custom) side** concentrates around the **experience layer**: sensory, AR/VR, personalisation, societal-behaviour sensing, discovery, engagement. This is where retailers still have genuine optionality and where brand is constructed. Keep, invest, differentiate.
- **Right (commodity) side** is infrastructure and basic channels: payments, logistics, CRM, KYC, cloud, CDN, physical-store fit-out, telesales operations. Rent, don't build.
- **The middle ground** — `Trust and Privacy`, `Consent Management`, `Returns and Reverse Logistics`, `Customer Data Platform` — is where product-stage components sit. These *will* commoditise, but for now they're the most fragile dependencies. Watch them; they're the most likely sources of evolution shocks over the next 3–5 years.
- **The diagonal from `Retail Experience` down through `Personalisation Engine` and `Customer Data Platform` to `Societal Behaviour Signals`** is the single most important strategic column: visible, differentiating at the top, but resting on immature foundations. This is where to invest and where to watch competitors closely.
