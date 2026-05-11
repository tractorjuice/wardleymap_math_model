```owm
anchor Individual User [0.98, 0.55]
anchor Government / Regulator [0.97, 0.35]
anchor Business Adopter [0.97, 0.60]

component Trust in AI System [0.90, 0.25]
component Reputation [0.88, 0.45]
component Competitive Advantage [0.85, 0.40]
component Demonstrable Safety [0.82, 0.20]

component Public Disclosure / Model Cards [0.78, 0.50]
component Third-Party Audit [0.75, 0.20]
component Certification Regime [0.72, 0.15]
component AI Regulation (EU AI Act draft) [0.74, 0.18]
component Liability Framework [0.70, 0.10]
component Procurement Policy [0.70, 0.55]

component Public Benchmark Suite [0.66, 0.55]
component Red-Team Evaluation [0.64, 0.30]
component Capability Eval Harness [0.62, 0.40]
component Safety Benchmark (HELM/BIG-bench) [0.62, 0.50]
component Bias / Fairness Test [0.60, 0.45]

component Constitutional Rules / Policy Spec [0.58, 0.30]
component RLHF Feedback Loop [0.56, 0.55]
component Constitutional AI Training [0.54, 0.25]
component Content Provenance (C2PA) [0.55, 0.20]
component Watermarking [0.53, 0.18]
component AI Forensics / Output Attribution [0.50, 0.10]
component Incident Reporting Registry [0.48, 0.12]

component Interpretability / Mechanistic Tools [0.46, 0.15]
component Alignment Research [0.44, 0.10]
component Guardrail / Moderation Layer [0.50, 0.60]
component System Prompt / Policy Layer [0.48, 0.65]

component Foundation Model [0.40, 0.55]
component Fine-Tuned Model [0.38, 0.60]
component Model Weights Distribution [0.36, 0.50]
component Open-Weights Ecosystem [0.34, 0.55]

component Training Algorithm (Transformer) [0.28, 0.75]
component Pre-Training Pipeline [0.26, 0.65]
component Human Preference Data [0.30, 0.40]
component Curated Training Corpus [0.24, 0.55]
component Web-Scale Scraped Data [0.22, 0.80]
component Data Provenance / Licensing [0.26, 0.20]

component GPU Compute [0.12, 0.78]
component Cloud Infrastructure [0.10, 0.92]
component Energy / Power [0.06, 0.96]
component Networking [0.08, 0.93]
```

Notes (outside the OWM block for the reader, not part of the map):

- Differentiating (left / pre-product): interpretability, alignment research, AI forensics, constitutional AI, liability frameworks, certification regimes, watermarking, provenance — all still Genesis / Custom-Built. Whoever industrialises these first owns the trust narrative.
- Commoditising (right): cloud, energy, networking, GPUs, the transformer architecture itself, and web-scale scraped data. None of these are a moat; all are table stakes.
- Fragile-trust zone: the components that are highly user-visible but still in Genesis/Custom-Built — Demonstrable Safety, Third-Party Audit, AI Regulation, Liability, Forensics. Users and regulators *need* these to trust AI, but in June 2023 they barely exist as products. That is the structural reason trust feels brittle: the trust-bearing components have not evolved to match the capability components below them.
