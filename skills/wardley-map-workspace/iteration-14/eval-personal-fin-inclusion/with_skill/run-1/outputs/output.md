# Wardley Map — Digital Financial Inclusion (Emerging Markets)

**Scenario:** Landscape of expanding digital financial inclusion for under-banked populations in emerging markets. Covers basic account access, mobile money, agent networks, identity, credit scoring (alternative data), regulation, consumer protection, and support. Focus: what is differentiating, what is commoditising, and where is inclusion fragile.

The map uses **two anchors** (under-banked consumer and merchant / micro-business) because the strategic dynamics depend on both sides of the two-sided payment market reaching critical mass. Regulators appear as components, not anchors — they shape the landscape but aren't "served" by it in the user-need sense.

---

## Map (OWM)

```owm
title Digital Financial Inclusion (Emerging Markets)
style wardley

// Anchors — two user types
anchor Under-banked Consumer [0.99, 0.55]
anchor Merchant / Micro-business [0.96, 0.58]

// User-facing activities
component Basic Account Access [0.90, 0.65]
component Send / Receive Money (P2P) [0.88, 0.75]
component Merchant Payment (QR / Till) [0.86, 0.60]
component Bill Pay [0.84, 0.65]
component Airtime Top-up [0.82, 0.85]
component Savings Product [0.80, 0.42]
component Micro-credit [0.78, 0.32]
component Micro-insurance [0.74, 0.22]
component Customer Support [0.72, 0.55]
component Complaint Redress [0.68, 0.32]

// Mid-chain activities
component Agent Network (CICO) [0.66, 0.65]
component Mobile Money Wallet [0.64, 0.70]
component USSD / Feature-phone UX [0.60, 0.82]
component Smartphone App [0.58, 0.85]
component QR Rails [0.56, 0.70]
component eKYC / Digital Onboarding [0.54, 0.48]
component Tiered KYC Practice [0.52, 0.55]
component Biometric Auth [0.50, 0.62]
component Fraud Detection [0.48, 0.48]
component AML / Sanctions Screening [0.46, 0.70]
component Credit Scoring (Alternative Data) [0.44, 0.25]
component Alt-data Ingestion (telco, utility, psychometric) [0.40, 0.22]
component Interoperability Switch [0.42, 0.52]
component Transaction Routing [0.38, 0.78]
component Agent Liquidity Management [0.38, 0.38]
component Agent Onboarding & Training [0.36, 0.35]

// Consumer protection + education
component Financial Literacy / Education [0.56, 0.32]
component Consumer Protection Framework [0.34, 0.42]
component Dispute / Ombudsman Process [0.36, 0.38]

// Regulatory / institutional
component E-money / PSP Licensing [0.30, 0.55]
component Data Protection Law [0.28, 0.42]
component Trust Account / Deposit Safeguard [0.26, 0.45]
component Central Bank Oversight [0.24, 0.68]

// Data / foundational
component National Digital ID [0.30, 0.38]
component SIM / Mobile Number Registry [0.26, 0.62]
component Core Ledger / Wallet Database [0.22, 0.78]
component Settlement Rails [0.20, 0.68]
component Cash (Physical) [0.24, 0.82]
component Card Networks (limited reach) [0.22, 0.85]

// Utility infrastructure
component SMS Gateway [0.18, 0.90]
component Mobile Network (GSM / Data) [0.12, 0.88]
component Cloud Utilities [0.10, 0.92]

// Knowledge
component Double-entry Bookkeeping [0.06, 0.95]
component AML / FATF Guidance [0.08, 0.70]

// Dependencies — user layer
Under-banked Consumer->Basic Account Access
Under-banked Consumer->Send / Receive Money (P2P)
Under-banked Consumer->Bill Pay
Under-banked Consumer->Airtime Top-up
Under-banked Consumer->Savings Product
Under-banked Consumer->Micro-credit
Under-banked Consumer->Micro-insurance
Under-banked Consumer->Customer Support
Under-banked Consumer->Complaint Redress
Merchant / Micro-business->Merchant Payment (QR / Till)
Merchant / Micro-business->Basic Account Access
Merchant / Micro-business->Micro-credit
Merchant / Micro-business->Customer Support

// User-facing -> mid-chain
Basic Account Access->Mobile Money Wallet
Basic Account Access->Agent Network (CICO)
Basic Account Access->eKYC / Digital Onboarding
Send / Receive Money (P2P)->Mobile Money Wallet
Send / Receive Money (P2P)->Interoperability Switch
Merchant Payment (QR / Till)->QR Rails
Merchant Payment (QR / Till)->Mobile Money Wallet
Merchant Payment (QR / Till)->Agent Network (CICO)
Bill Pay->Mobile Money Wallet
Airtime Top-up->Mobile Money Wallet
Savings Product->Mobile Money Wallet
Savings Product->Trust Account / Deposit Safeguard
Micro-credit->Credit Scoring (Alternative Data)
Micro-credit->Mobile Money Wallet
Micro-insurance->Mobile Money Wallet
Micro-insurance->Alt-data Ingestion (telco, utility, psychometric)
Customer Support->Agent Network (CICO)
Customer Support->Financial Literacy / Education
Complaint Redress->Dispute / Ombudsman Process
Complaint Redress->Consumer Protection Framework

// Mid-chain internal
Mobile Money Wallet->USSD / Feature-phone UX
Mobile Money Wallet->Smartphone App
Mobile Money Wallet->Core Ledger / Wallet Database
Mobile Money Wallet->AML / Sanctions Screening
Mobile Money Wallet->Fraud Detection
Mobile Money Wallet->Biometric Auth
Agent Network (CICO)->Agent Liquidity Management
Agent Network (CICO)->Agent Onboarding & Training
Agent Network (CICO)->Cash (Physical)
Agent Network (CICO)->Mobile Money Wallet
eKYC / Digital Onboarding->Tiered KYC Practice
eKYC / Digital Onboarding->Biometric Auth
eKYC / Digital Onboarding->National Digital ID
eKYC / Digital Onboarding->SIM / Mobile Number Registry
Tiered KYC Practice->AML / FATF Guidance
QR Rails->Interoperability Switch
Interoperability Switch->Transaction Routing
Interoperability Switch->Settlement Rails
Transaction Routing->Core Ledger / Wallet Database
Fraud Detection->Core Ledger / Wallet Database
Fraud Detection->Alt-data Ingestion (telco, utility, psychometric)
AML / Sanctions Screening->AML / FATF Guidance
Credit Scoring (Alternative Data)->Alt-data Ingestion (telco, utility, psychometric)
Credit Scoring (Alternative Data)->Core Ledger / Wallet Database
Alt-data Ingestion (telco, utility, psychometric)->Mobile Network (GSM / Data)
Biometric Auth->National Digital ID

// Regulatory / oversight edges
Mobile Money Wallet->E-money / PSP Licensing
E-money / PSP Licensing->Central Bank Oversight
Trust Account / Deposit Safeguard->Central Bank Oversight
Consumer Protection Framework->Data Protection Law
Consumer Protection Framework->Central Bank Oversight
Dispute / Ombudsman Process->Consumer Protection Framework
Financial Literacy / Education->Consumer Protection Framework

// Infrastructure
USSD / Feature-phone UX->SMS Gateway
USSD / Feature-phone UX->Mobile Network (GSM / Data)
Smartphone App->Mobile Network (GSM / Data)
SMS Gateway->Mobile Network (GSM / Data)
Core Ledger / Wallet Database->Cloud Utilities
Settlement Rails->Cloud Utilities
Card Networks (limited reach)->Settlement Rails
Mobile Network (GSM / Data)->Cloud Utilities

// Knowledge edges
Core Ledger / Wallet Database->Double-entry Bookkeeping

// Evolve targets (scenario, not forecast)
evolve Credit Scoring (Alternative Data) 0.55
evolve Interoperability Switch 0.72
evolve National Digital ID 0.65
evolve Consumer Protection Framework 0.60
evolve QR Rails 0.82

// Notes
note Inclusion moat (differentiation) [0.55, 0.25]
note Fragile foundation (regulatory + ID) [0.28, 0.40]
note Utility layer [0.12, 0.92]
```

---

## Strategic Analysis

### a. Differentiation opportunities (top 3)

The frontier of inclusion sits at the bottom-left of the visible layer — products that are user-facing but still Genesis/Custom Built. Whoever industrialises these **captures the next wave of under-banked customers** rather than competing over the P2P transfer layer that is already commoditising.

1. **Micro-insurance** (Genesis) — visible to the consumer, almost entirely nascent in most emerging markets. Index-based crop insurance, hospitalisation cover, and embedded insurance on top of mobile wallets are all still being figured out. Highest differentiation leverage — both because `ν · (1 − ε)` is highest *and* because regulators have not yet locked in the shape. A provider who crosses the chasm here defines the category.
2. **Micro-credit** (Custom Built → Product (+rental)) — a live build-vs-buy question. Everyone offers it, no one has solved thin-file repayment risk at scale. The moat is the *data loop*: customers repay → data trains scoring → better offers → more customers. This is the classic **Sensing Engine (ILC)** shape.
3. **Savings Product** (Custom Built) — structurally under-supplied because under-banked consumers need very small-balance, high-frequency, goal-linked savings products; conventional bank deposit accounts don't fit. Behavioural-nudge products (committed savings, lock-boxes) are still Custom Built and differentiating.

Runners-up: **Complaint Redress** and **Financial Literacy / Education** are both user-visible and still Custom Built — they don't win you a user on day one but they retain and deepen trust, and trust is the binding constraint on inclusion.

### b. Commodity-leverage candidates (top 3) — rent, don't build

1. **Cloud Utilities** (Commodity +utility) — hyperscaler regions and local cloud now serve every emerging market. There is no case for building.
2. **Mobile Network (GSM / Data)** (Commodity +utility) — you consume this; you don't build it. The strategic question is instead *access pricing* and *reverse-billing arrangements* with MNOs, not infrastructure ownership.
3. **SMS Gateway** (Commodity +utility) — multiple aggregators (Africa's Talking, Twilio, Infobip) offer A2P SMS as a utility. USSD delivery is similarly commoditised through aggregators.

Also clearly Commodity (+utility) and in the "rent don't build" bucket: **Cash handling** (use cash-processing utilities / armoured-transport partners), **AML / Sanctions Screening** vendor layer (ComplyAdvantage, LexisNexis), and the **Core Ledger / Wallet Database** engine (Mambu, Temenos, Mifos — don't write your own ledger).

### c. Dependency risks (top 3)

Each risk is a user-visible product pinned to an immature foundation. These are where *inclusion is fragile* — the service promise to the consumer depends on a layer that hasn't industrialised yet.

1. **Micro-credit → Credit Scoring (Alternative Data)** — the entire thin-file credit proposition depends on a scoring layer that is still early Genesis. When the scoring layer fails (biased, gameable, or unstable across economic cycles), the loans default en masse and the provider collapses — as Kenya's digital lenders have repeatedly demonstrated. **This is the single most fragile dependency in the map.**
2. **Micro-insurance → Alt-data Ingestion (telco, utility, psychometric)** — index insurance and embedded cover depend on data pipes from MNOs and utilities that are not yet standardised. A single MNO policy change breaks the product.
3. **Basic Account Access → eKYC / Digital Onboarding** — the flagship activity (open an account) depends on an identity-verification layer that is, in most emerging markets, still Custom Built. If the national ID system is incomplete or excludes specific populations (rural women, refugees, informal-sector workers), **the inclusion proposition structurally fails for exactly the people it's supposed to serve**.

Secondary risks worth tracking: **Complaint Redress → Dispute / Ombudsman Process** (trust collapses silently when redress is Custom Built and slow); **Savings Product → Trust Account / Deposit Safeguard** (an E-money provider insolvency without proper safeguarding wipes out customer balances and sets the whole sector back — see real-world M-Pesa trust structure as a positive counter-example).

### d. Suggested gameplays (from the 61-play catalogue)

- **#36 Directed investment** on **Credit Scoring (Alternative Data)** and **Micro-insurance** — these are the top two D components and where platform-scale data and engineering should concentrate.
- **#43 Sensing Engines (ILC)** on **Micro-credit / Credit Scoring** — the Innovate-Leverage-Commoditise loop fits perfectly: observe repayment, train the model, push the model back into product. The data loop *is* the moat.
- **#45 Two factor** — the map is a two-sided market (consumer + merchant) and the defining play is reinforcing both sides. QR Rails + Agent Network + Mobile Money Wallet are the shared rails; invest so both sides see rising value.
- **#16 Exploiting Network Effects** on **Interoperability Switch** and **QR Rails** — each new participant raises the value to everyone. Push regulators toward mandated interoperability (India's UPI is the canonical example) to accelerate Stage III → IV.
- **#15 Open Approaches** on **Alt-data Ingestion** and **Tiered KYC Practice** — opening the data-ingestion layer (standardised schemas, consent APIs) and the tiered-KYC playbook industrialises them faster. Own the product, open the plumbing.
- **#29 Harvesting** on **Core Ledger / Wallet Database**, **SMS Gateway**, **AML Screening vendor layer** — let the vendors win, harvest the winners.
- **#41 Alliances** with MNOs and National ID authorities — these are the critical foundations you don't own. Multi-source data supply (several MNOs, not one) reduces the dependency risk on Alt-data Ingestion.
- **#56 First mover** on **Regulatory Sandbox / Licensing** — in markets that have just opened e-money regimes, first-mover licensed status is a genuine competitive asset (and a defence against the next play).
- **#12 FUD / #10 Fear, Uncertainty and Doubt** — expect *incumbent banks* to deploy FUD gameplays against new entrants ("mobile money is unsafe", "data is at risk"). Pre-empt by over-investing in the visible **Consumer Protection Framework** and **Trust Account / Deposit Safeguard** edges — turn these from fragile dependencies into proof points.
- **#42 Co-creation** with regulators — in jurisdictions with weak consumer-protection frameworks, co-designing the standard (rather than being regulated into one) protects both users and the business.

### e. Doctrine notes

- **#1 Focus on user needs** — two anchors are correctly identified (consumer + merchant). The map does not anchor on "shareholder return" or "product roadmap", which is the common failure mode in fintech.
- **#10 Know your users** — the two-anchor decomposition is essential here; a single "customer" anchor would hide that merchant acceptance is the chokepoint for the P2P → merchant-payment transition. The under-banked consumer anchor should arguably be split further (rural vs. urban, women vs. men, migrants vs. settled) — represented here by a single node, but practitioners should refine.
- **#13 Manage inertia** — on the under-banked side, **cash inertia** (consumer-side inertia forms #1 loss of familiarity, #6 confusion over method, #8 skill acquisition cost) is the single largest blocker to adoption. Financial Literacy / Education is the direct countermeasure.
- **#2 Use a systematic mechanism of learning** — Credit Scoring (Alt Data) only works if repayment outcomes feed back into training data, in a governed way. Providers without this feedback loop over-extend in good years and collapse in downturns.
- **#16 Design for constant evolution / #24 Strategy is iterative** — in regulated markets the map is not static; E-money Licensing, Data Protection Law, and Consumer Protection Framework all move. Plan re-mapping at least annually.
- **⚠ Possible violation of #19 Use appropriate methods** — if a provider builds bespoke cloud infrastructure, custom SMS aggregation, or a proprietary core ledger, they are treating Stage IV components as if they were differentiators. Common failure mode.

### f. Climatic context (which of the 27 patterns are shaping this map)

- **#3 Everything evolves** — every component is moving rightward on the X-axis; the question is rate and cannibalisation.
- **#15–17 Inertia (past success, changing practices, existing business models)** — incumbent banks and traditional MFIs experience all three. Their branch-based cost structures cannot compete with agent-network unit economics, but internal inertia keeps them building retail apps that mimic the branch.
- **#18 "You cannot measure evolution over time or adoption"** — the `evolve` arrows are scenarios only; the actual rate depends on regulatory posture, infrastructure, and who enters first. Don't treat them as forecasts.
- **#27 Product-to-utility punctuated equilibrium** — P2P transfers are already punctuating (M-Pesa, UPI, Pix); merchant payments and interoperability switches are the next punctuation; credit scoring and insurance will follow.
- **#4 Co-evolution of practice with activity** — Tiered KYC and Consumer Protection are **practices** co-evolving with the **activities** of eKYC and account opening. As the activity industrialises, the practice has to as well, or inclusion becomes exclusion (populations who cannot complete digital KYC get locked out).
- **#10 Efficiency enables innovation / componentisation** — commoditising Cloud, SMS, AML screening, and core ledgers is what enables the micro-insurance and micro-credit innovation at the top of the stack.

### g. Deep-placement notes

I did targeted reasoning (not live web searches in this pass) on four components where the cheat-sheet rows pulled in different directions or where the scenario is specialised enough that generic priors wouldn't hold:

- **Credit Scoring (Alternative Data)** — initial cheat-sheet placement was borderline (Genesis/Custom Built, rows disagreed between "rapid learning" and "poorly understood"). Considered the evidence: vendor landscape is still fragmented (Tala, Branch, JUMO, LenddoEFL, FICO alt-data, plus bank-internal builds), publications are a mix of "describe the wonder" and case studies, accuracy across economic cycles is still unproven, and no dominant standard exists. Settled at ε ≈ 0.25 (late Genesis) with an `evolve` to 0.55 scenario. Flagged as highest dependency risk because Micro-credit depends on it.
- **National Digital ID** — extreme variance by jurisdiction. India (Aadhaar) is effectively Stage IV; Nigeria (NIN) and Kenya (Huduma/Maisha Namba) are mid-Stage III with ongoing rollout friction; many Sub-Saharan markets are Stage II. Placed at ε ≈ 0.38 as a *weighted EM average* and gave an `evolve` to 0.65 — but noted the placement should be re-scored per country when the map is applied specifically. Widen uncertainty range on this node.
- **Interoperability Switch** — India (UPI) and Brazil (Pix) are effectively Stage IV utilities; most African markets still run bilateral sender–receiver agreements or first-generation mobile-money switches. Placed at ε ≈ 0.52 as an EM-wide average. The `evolve` to 0.72 reflects the policy pattern of regulator-mandated interoperability following the India / Brazil template — but this requires political will.
- **Agent Network (CICO)** — cheat-sheet scored Stage III ("common / expected"). Considered whether the cash-in/cash-out agent model is an industrialised product or still Custom Built. M-Pesa, MTN MoMo, bKash, GCash agent networks are mature operational products; agent liquidity management, supervisor structures, and commissions are standardised. But the *unit-level craft* — training, retention, fraud containment at the agent — remains Custom Built, which is why I kept **Agent Liquidity Management** and **Agent Onboarding & Training** as separate, less-evolved nodes. Agent Network itself sits at ε ≈ 0.65 (solid Stage III).

Components I deliberately *didn't* deep-place: **Cloud Utilities, Mobile Network, SMS Gateway, Card Networks, Cash, Double-entry Bookkeeping, AML / FATF Guidance** — all obvious Commodity (+utility) or accepted Knowledge; research would not move the placement. Likewise obvious Genesis bets (**Micro-insurance, Alt-data Ingestion**) where the scenario framing already signals the stage.

### h. Validation

Running the bundled validator against the draft:

```
python3 "${CLAUDE_SKILL_DIR}/scripts/validate_owm.py" ./draft.owm
→ OK: 46 components/anchors, 75 edges — no violations.
```

The visibility constraint `ν(a) ≥ ν(b)` holds for all 75 edges; three violations were found and fixed during iteration before shipping (Agent Network vs. Mobile Money Wallet ordering, Dispute Process vs. Consumer Protection Framework, Card Networks vs. Settlement Rails).

### i. Where is inclusion fragile? (synthesis)

The scenario asked specifically where inclusion is fragile. Three structural fragilities stand out from the map:

1. **The identity floor.** Basic Account Access depends on eKYC, which depends on National Digital ID. When the ID layer is incomplete — missing rural populations, migrants, women without tenure documents — *the fundamental access promise fails for the people inclusion exists to serve*. This is not a technical bug; it is a political-economy problem at the base of the stack.
2. **The credit-scoring gap.** Micro-credit's reach depends on Alternative Data scoring that is still Genesis. When this layer is fragile, providers mis-price risk, over-extend in good macro conditions, then collapse in downturns — taking customer trust and the sector's regulatory licence with them. This has happened repeatedly (Kenyan digital lenders, pre-regulation Chinese P2P).
3. **The trust and redress layer.** Consumer Protection Framework (ε ≈ 0.42), Dispute / Ombudsman Process (0.38), and Trust Account / Deposit Safeguard (0.45) are all still Custom Built. They are structurally invisible *until a provider fails or a scandal breaks* — and then they become the most visible thing in the market. Regulators and operators that industrialise these layers pre-emptively (not reactively) protect the whole sector.

The upside: **what's differentiating** (Micro-insurance, Micro-credit, Savings, Financial Literacy, Complaint Redress) and **what's commoditising** (Mobile Money Wallet, QR Rails, Agent CICO, SMS, Cloud, AML Screening) are now clearly separable on the map. The industry's next five years will be defined by **which players direct investment into the top-left differentiators while renting the utility layer** — and by whether regulators close the identity and redress gaps before a major bust forces them to.

### j. Caveat

Evolution trajectories (the `evolve` arrows and the prose rate predictions) are **scenarios, not forecasts**. Wardley's climatic pattern #18: *"you cannot measure evolution over time or adoption."* Rates depend on specific regulatory, infrastructural, and competitive conditions in each emerging market; the map above is a *composite EM view* and any specific country (Kenya, Nigeria, India, Indonesia, Brazil, Philippines) would shift multiple placements materially. Re-score before applying to a single market.
