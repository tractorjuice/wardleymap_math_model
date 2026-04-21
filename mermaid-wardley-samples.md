# Mermaid Wardley Map samples — GitHub rendering test

Four increasingly-featured examples to verify GitHub's Mermaid renderer (v11.44-ish) handles the `wardley` diagram type introduced in mermaid 11.14. Syntax reference: [mcraddock — Bringing Wardley Maps to Mermaid](https://medium.com/@mcraddock/bringing-wardley-maps-to-mermaid-a-journey-from-idea-to-open-source-contribution-8fe5009eafd3).

Coordinates are `[visibility, evolution]` on $[0, 1]$ — same convention as OWM. Top-right corner is the anchor; bottom-left is commodity infrastructure.

---

## 1. Minimal — anchor + three components

Tests the smallest possible diagram.

```mermaid
wardley
title Minimal example
anchor User [0.95, 0.50]
component Service [0.75, 0.45]
component API [0.50, 0.60]
component Database [0.20, 0.85]
User -> Service
Service -> API
API -> Database
```

---

## 2. Classic Tea Shop

Simon Wardley's canonical worked example, matching the [Part 3 doc](docs/core/part-3-tea-shop-example.md).

```mermaid
wardley
title Tea Shop Value Chain
anchor Business [0.95, 0.63]
component Cup of Tea [0.79, 0.61]
component Tea [0.63, 0.81]
component Hot Water [0.52, 0.80]
component Kettle [0.43, 0.35]
component Power [0.10, 0.70]
Business -> Cup of Tea
Cup of Tea -> Tea
Cup of Tea -> Hot Water
Hot Water -> Kettle
Kettle -> Power
evolve Kettle 0.62
evolve Power 0.89
note Standardising power allows Kettles to evolve faster [0.30, 0.49]
```

---

## 3. SaaS product — mid-complexity

Tests `evolve` movement arrows, multiple `note` annotations, and a deeper dependency graph.

```mermaid
wardley
title B2B SaaS — Observability Product
anchor Engineering Team [0.95, 0.60]
component Dashboards [0.85, 0.55]
component Alerting [0.82, 0.50]
component Query Language [0.72, 0.40]
component Log Pipeline [0.60, 0.65]
component Metrics Store [0.55, 0.70]
component Trace Store [0.50, 0.40]
component Object Storage [0.25, 0.90]
component Compute [0.15, 0.92]
component Network [0.10, 0.95]
Engineering Team -> Dashboards
Engineering Team -> Alerting
Dashboards -> Query Language
Alerting -> Query Language
Query Language -> Log Pipeline
Query Language -> Metrics Store
Query Language -> Trace Store
Log Pipeline -> Object Storage
Metrics Store -> Object Storage
Trace Store -> Object Storage
Object Storage -> Compute
Compute -> Network
evolve Query Language 0.62
evolve Trace Store 0.70
note Dashboards are common expectation; differentiation is in query power [0.75, 0.35]
note Trace stores are rapidly commoditising — buy, don't build [0.45, 0.65]
```

---

## 4. Multi-anchor — team + platform users

Tests a map with two anchors (valid in Wardley practice and in our skill's generated outputs). Also tests longer component names with punctuation.

```mermaid
wardley
title Internal Developer Platform
anchor Product Engineer [0.96, 0.55]
anchor Platform Engineer [0.92, 0.40]
component Service Template [0.82, 0.30]
component CI/CD Pipeline [0.78, 0.55]
component Deployment Gateway [0.72, 0.45]
component Observability Stack [0.65, 0.60]
component Secrets Management [0.55, 0.70]
component Kubernetes Platform [0.40, 0.72]
component Container Runtime [0.28, 0.88]
component Cloud IaaS [0.15, 0.95]
Product Engineer -> Service Template
Product Engineer -> CI/CD Pipeline
Platform Engineer -> Deployment Gateway
Platform Engineer -> Kubernetes Platform
Service Template -> CI/CD Pipeline
CI/CD Pipeline -> Deployment Gateway
Deployment Gateway -> Kubernetes Platform
Observability Stack -> Kubernetes Platform
Secrets Management -> Kubernetes Platform
Kubernetes Platform -> Container Runtime
Container Runtime -> Cloud IaaS
evolve Service Template 0.50
evolve Observability Stack 0.78
note Service Templates are differentiating today, commoditising fast [0.75, 0.55]
```

---

**What to check on GitHub:**
1. Does each block render as a diagram (not as raw text)?
2. Are all four stages (Genesis / Custom / Product / Commodity) labelled on the X-axis?
3. Do `evolve` arrows appear pointing to the target evolution position?
4. Do `note` annotations render in-position on the canvas?
5. Do both anchors in example 4 sit at the top, with their dependency paths visible?

If any syntax doesn't render, note which example fails and I'll iterate.
