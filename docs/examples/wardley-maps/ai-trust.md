# ai-trust (Wardley reference, Mermaid rendering)

Source: [`/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare/eval-ai-trust/wardley-reference.owm`](../../../skills/wardley-map-workspace/arc-kit-compare/eval-ai-trust/wardley-reference.owm)

Converted from OWM via `scripts/owm_to_mermaid.py`.

```mermaid
wardley-beta
title AI, TRUST, JUNE 2023
anchor individuals [0.93, 0.26]
anchor government [0.93, 0.66]
anchor business [0.93, 0.44]
component Safety [0.81, 0.29]
component Competitive advantage [0.83, 0.52]
component Reputation [0.82, 0.38]
component Power [0.84, 0.76]
component Enforcement [0.43, 0.04]
component Regulations [0.43, 0.14]
component Objectively evaluatable [0.41, 0.79]
component Believed [0.41, 0.59]
component OUTPUT [0.43, 0.70]
component Algorithm and Model [0.58, 0.61]
component Policy [0.53, 0.09]
component DATA [0.20, 0.70]
component Input DATA [0.18, 0.61]
component Training [0.18, 0.79]
component ACCESS [0.68, 0.30]
component Bias [0.06, 0.65]
component Quality [0.10, 0.46]
component CONTROLS [0.29, 0.15]
component Leading [0.27, 0.11]
component Lagging [0.27, 0.19]
component Computation [0.05, 0.75]
component Feedback Loop [0.11, 0.05]
component constitution [0.22, 0.03]
component Ranking Reputation Engine and Trust Broker [0.30, 0.35]
component Checks and balances Guardrails [0.16, 0.31]
component Forensics [0.15, 0.13]
component Audits [0.10, 0.17]
component Benchmarks [0.04, 0.37]
component Defend IP [0.66, 0.39]
component Transparency [0.66, 0.21]
component Technologists [0.04, 0.18]
component Source [0.07, 0.55]
component Asymmetrical [0.73, 0.22]
component Computation language [0.24, 0.28]
Reputation -> CONTROLS
Transparency -> Algorithm and Model
business -> Safety
government -> Safety
Competitive advantage -> Algorithm and Model
individuals -> Safety
government -> Power
government -> Competitive advantage
business -> Competitive advantage
Safety -> OUTPUT
government -> Reputation
business -> Reputation
Safety -> Algorithm and Model
Safety -> Input DATA
DATA -> Quality
Lagging -> Checks and balances Guardrails
Lagging -> Audits
Algorithm and Model -> CONTROLS
Input DATA -> CONTROLS
OUTPUT -> CONTROLS
Lagging -> Forensics
Algorithm and Model -> DATA
Competitive advantage -> ACCESS
Safety -> Transparency
DATA -> Transparency
Power -> Policy
Policy -> Regulations
Policy -> Enforcement
Policy -> constitution
constitution -> CONTROLS
constitution -> Feedback Loop
constitution -> Technologists
CONTROLS -> Computation language
Computation language -> Computation
Computation language -> constitution
Regulations -> Computation language
Safety -> CONTROLS
Enforcement -> CONTROLS
DATA -> Bias
Ranking Reputation Engine and Trust Broker -> Benchmarks
Quality -> Benchmarks
DATA -> Source
Algorithm and Model -> Ranking Reputation Engine and Trust Broker
Competitive advantage -> Asymmetrical
Asymmetrical -> ACCESS
note "+Speed:human->computation" [0.17, 0.01]
```
