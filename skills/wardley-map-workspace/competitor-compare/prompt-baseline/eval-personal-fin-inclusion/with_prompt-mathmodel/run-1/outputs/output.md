# Digital Financial Inclusion — Individual in an Underbanked Region

## 1. Scenario framing

Perspective: a single person in an underbanked region. Anchor set U = {Individual} with the five named needs (Options, Trade, Equality, Sustainability, Inclusion) modelled as directly-dependent components just below the anchor rather than as separate anchors, because they are facets of one user rather than distinct user types.

The map traces a single value chain downward: Needs → identity/trust/risk/behaviour → markets, exchange protocols, authority, redistribution → banking provision and currency → technology stack → network topology → energy. The question "where is the stack commoditised globally vs. where does local landscape still dominate?" is answered in the visual split — see §5.

## 2. Component list V and anchor U

**Anchor U:** Individual.

**Needs layer (closest to user):** Options, Trade, Equality, Sustainability, Inclusion.

**Institutional / behavioural layer:** Identity, Trust, Risk Assessment, Behavioural Patterns, Markets, Exchange Protocols, Centralised Authority, Decentralised Authority, Redistribution.

**Banking provision:** Bank Branches (inertia), Banking Services, Online Payments, Financial Infrastructure.

**Currency:** Fiat Currency, Cryptocurrency, CBDC.

**Technology stack:** Mobile Device, Internet Access, Consensus Algorithms, Computing Infrastructure.

**Network topology:** 5G, Satellite, Mesh Networks, Copper (inertia).

**Energy:** Minigrids, Renewable Energy, Fossil Energy (inertia).

## 3. OWM Output

See `draft.owm` in this directory. Key design choices:

- Single anchor `Individual` to stay faithful to the prompt ("from the perspective of an individual").
- The five named needs are placed immediately below the anchor at ν ≈ 0.95 — they are the user's own dimensions of value, not separate components further down the chain.
- Branches, Copper, and Fossil Energy carry the `inertia` marker (sunk capital + re-architecture cost forms, per the 17 inertia forms) because they are the dominant-but-receding incumbents at each of their layers.
- CBDC, Cryptocurrency, Mesh Networks, Minigrids, and Consensus Algorithms carry `evolve` directives to signal the expected Stage-II → Stage-III transitions (labelled as scenario, not forecast).

## 4. Visibility and evolution scoring notes

### Visibility ν

Seeded from `d(v) = min shortest-path distance from Individual` and then adjusted:

- Needs (Options/Trade/…) were lifted to ν ≈ 0.95 — they are mental categories the user literally thinks about, so they override the pure graph distance.
- Fiat Currency is raised above banking services it technically sits under, because in an underbanked context the note/coin is extremely visible to the user while bank branches may not be.
- CDN-equivalents (Computing Infrastructure, Copper) were lowered because they are architecturally invisible — the user never sees them.
- The hard constraint ν(a) ≥ ν(b) for every edge (a,b) was checked by hand. The only near-violations were at the currency/banking interface (Fiat Currency is close in ν to Banking Services); the chosen numbers maintain the ordering.

### Evolution ε

Applied the quick 4-row cheat sheet (Ubiquity, Certainty, User Perception, Publication Types) per component. Representative scores:

| Component | Ubiquity | Certainty | User Perception | Publication Types | ε |
|---|---|---|---|---|---|
| Fiat Currency | IV | IV | IV | IV | 0.875 → nudged to 0.92 (global infrastructure) |
| Bank Branches | IV | IV | IV | IV | 0.875 → 0.82 (declining in underbanked regions, so just below pure commodity) |
| Online Payments | III/IV | IV | III/IV | IV | ~0.75 → 0.78 |
| CBDC | I | II | I | I | 0.18 → 0.25 (pilots and policy papers dominate publications) |
| Cryptocurrency | II | III | II | III | ~0.44 → 0.45 (Stage II–III, in transition) |
| Consensus Algorithms | II | III | II | III | ~0.44 → 0.40 |
| Mesh Networks | II | II | II | II | 0.375 → 0.30 (still largely leading-edge in underbanked deployment) |
| Minigrids | II | III | II | II | 0.40 |
| Renewable Energy | III | III | III | III | 0.625 → 0.55 (rapidly increasing but not yet commodity globally) |
| Fossil Energy | IV | IV | IV | IV | 0.92 |

Where rows disagreed — especially for Cryptocurrency, CBDC, Mesh Networks — components are flagged as "in transition" and positioned at the midpoint of the rows' disagreement range.

## 5. Commoditised-vs-local split (the prompt's core question)

**Globally commoditised (ε > 0.75, should be bought / treated as utility):**

- Fiat Currency (0.92), Copper (0.95, receding), Fossil Energy (0.92), Online Payments (0.78), Mobile Device (0.88), Computing Infrastructure (0.90), Bank Branches (0.82), Financial Infrastructure (0.80), Internet Access (0.78), Centralised Authority (0.80).

**Locally constrained (ε < 0.5 but high D — where local landscape dominates):**

- Identity (0.45), Trust (0.30), Mesh Networks (0.30), Minigrids (0.40), CBDC (0.25), Cryptocurrency (0.45), Decentralised Authority (0.35), Consensus Algorithms (0.40), Redistribution (0.30).
- The anchor-adjacent needs themselves (Options/Equality/Sustainability/Inclusion at ε = 0.20–0.30) are also inherently local — what *counts* as "inclusion" depends on local context.

Visually: the bottom-left quadrant (low ν, low ε — mesh networks, minigrids, consensus) and the top-left quadrant (high ν, low ε — user needs, identity, trust) are both where local landscape dominates. The middle-right band (payments, banking services, mobile devices, fiat, computing) is where the stack is already globally commoditised. The notes in the map mark these zones explicitly.

## 6. Strategic analysis

### a. Top 3 by D (differentiation pressure) = ν · (1 − ε)

Excluding the anchor and the five needs (which are definitionally high-D and not targets in the usual sense):

1. **Trust** — D ≈ 0.80 × 0.70 = **0.56**. Visible, pre-commodity — reputation systems, community vouching, custodial safeguards.
2. **Behavioural Patterns** — D ≈ 0.88 × 0.60 = **0.53**. Alternative credit scoring, mobile-money usage signals — directly determines who gets financial access.
3. **Identity** — D ≈ 0.80 × 0.55 = **0.44**. Digital ID programmes (Aadhaar-style) are the archetype; the single biggest lever for inclusion.

### b. Top 3 by K (commodity leverage) = (1 − ν) · ε

1. **Fossil Energy** — K ≈ 0.94 × 0.92 = **0.86**. Already a utility but flagged with inertia because the sustainability need argues against leaning on it.
2. **Copper** — K ≈ 0.84 × 0.95 = **0.80**. Commoditised and inertia-laden. Leverage only where it exists; do not extend.
3. **Computing Infrastructure** — K ≈ 0.75 × 0.90 = **0.68**. Pure utility; buy via hyperscaler.

### c. Top 3 by R (dependency risk) = ν(a) · (1 − ε(b))

1. **(Inclusion, Trust)** — R = 0.95 × 0.70 = **0.67**. Highest-R edge on the map. Trust is more fragile than identity in this context.
2. **(Inclusion, Identity)** — R = 0.95 × 0.55 = **0.52**. The headline user-need depends on an immature identity layer.
3. **(Trade, Risk Assessment)** — R = 0.95 × 0.45 = **0.43**. Trade depends on risk/fraud logic that is still behavioural and context-specific.

### d. Suggested gameplays (from the 61-play catalogue)

- **Open Approaches (accelerator)** on Identity and Consensus Algorithms — publish open-ID specs and open consensus protocols to drag both up the evolution axis. Target: reduce R on the top-3 risky edges by commoditising the fragile foundation.
- **Cooperation** around Mesh Networks and Minigrids — pool local infrastructure through community ownership rather than waiting for carrier rollout.
- **Harvesting** on Online Payments — once a local stack gets traction (M-Pesa-style), acquire the infrastructure rather than rebuild.
- **Directed investment** on CBDC pilots and Behavioural Patterns analytics — these are differentiation candidates with policy backing.
- **Exploiting constraint** on Renewable Energy — underbanked regions with high solar yield can leapfrog the fossil layer entirely.
- **Pig in a poke** caution — do not buy into proprietary "digital inclusion" stacks that lock identity + payments + currency into one vendor.

### e. Doctrine observations (from the 40 principles)

- **Focus on user needs** (Phase I) — well covered. Five named needs sit immediately below the anchor.
- **Know your users** (Phase II) — only one user type modelled. Multi-anchor maps (e.g., Individual + Agent + Regulator) would be a natural extension but are out of scope for the prompt.
- **Use appropriate methods** (Phase III) — the Identity / Trust / Behaviour layer is labelled but underspecified in Knowledge terms. A τ extension could mark these as K-type (Knowledge) rather than Activities, which would clarify why they are harder to commoditise.
- **Manage inertia** (Phase IV) — three inertia markers (Branches, Copper, Fossil Energy) are the visible legacy drag. Each corresponds to sunk-capital + re-architecture-cost forms from the 17-form taxonomy.
- **A bias towards action** (Phase V) — the evolve directives sketch five components (Identity, CBDC, Crypto, Mesh, Minigrids, Consensus) as the active playground. These are scenario, not forecast.

## 7. Key takeaway

The underbanked-region individual sits above a stack that is two-tone: the middle of the chain (payments, banking, fiat, mobile, computing, centralised authority) is already globally commoditised and should be bought; the top (identity, trust, behaviour, the needs themselves) and the bottom-left corner (mesh, minigrids, consensus, CBDC) are where local landscape dominates and where differentiation lives. Strategy for the individual's ecosystem (government, NGO, cooperative, fintech) should be: *ride the commodity middle, invest in the local top and bottom-left corners*.
