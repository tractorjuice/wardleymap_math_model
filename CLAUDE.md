# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a documentation-only research repository containing mathematical models and frameworks for Wardley Mapping. There is no code, build system, or tests - the repository consists entirely of markdown files presenting theoretical work on quantifying Wardley Maps.

## Content Structure

The repository contains research documents exploring how to formalize Wardley Mapping mathematically:

- **Core Mathematical Model** (`Part 1 - Core Mathematical Model for Wardley Mapping.md`, `A Prototype Math Model for Wardley Mapping.md`): Defines a Wardley Map as a tuple $\mathcal{M} = (V, E, U, \nu, \varepsilon, t)$ where V is components, E is dependency edges, U ⊆ V is the anchor set (one or more user-need nodes), $\nu$ is visibility function (Y-axis), and $\varepsilon$ is evolution function (X-axis)

- **Cheat-Sheet Scoring** (`Part 6 - Cheat-Sheet Evolution Scoring.md`): Reproduces Wardley's canonical 19-row evolution cheat sheet and formalizes the scoring procedure as $\varepsilon(v) = \sum_r w_r \cdot m(s_r(v))$ with an uncertainty estimate from per-row disagreement.

- **Inertia** (`Inertia - Forms of Resistance to Evolution.md`): Enumerates the 17 forms of inertia Wardley publishes (14 consumer + 3 supplier) and replaces the single $c_v(t)$ scalar from Part 1's dynamics with a structured sum. Note: FUD, Lobbying, and Bundling are **gameplays**, not inertia — don't confuse the taxonomies.

- **Multi-Wave Evolution** (`Multi-Wave Evolution and Punctuated Equilibrium.md`): Replaces the single-logistic dynamics with per-generation S-curves, cross-generation cannibalisation, and chasms. Matches Wardley's "evolution is multi-wave" framing.

- **Component Types** (`Component Types and the Type Function.md`): Extends the tuple with $\tau: V \to \{A, P, D, K\}$ and type-dependent evolution rates. Adds the "practices co-evolve with activities" constraint.

- **Gameplay Catalogue** (`Gameplay Catalogue - 61 Plays with Math-Model Effects.md`): Wardley's 61 gameplays across 12 categories, each with a structured effect on the math model's parameters.

- **Doctrine** (`Doctrine - 40 Principles as Model Constraints.md`): Wardley's 40 doctrine principles across 4 phases and 6 categories, with math-model readings showing which principles are constraints on the model and which are organisational practices outside it.

- **Comprehensive Framework** (`The Mathematical Framework of Wardley Mapping.md`): Extended treatment covering graph theory, game theory, probability, and machine learning applications

- **Strategy & Gameplay** (`Strategic Mastery: Creating Math Models for Wardley Mapping Gameplays.md`, `Mathematical Models for Wardley Mapping Gameplay...`): Quantitative approaches to strategic decision-making

- **Series Documents** (`Part 2-5`, `Wardley Strategy Cycle`, `Weak Signals & Evolution`): Progressive development of specific model aspects including evolution dynamics, visibility layers, and signal detection

## Key Mathematical Concepts

- **Visibility (Y-axis)**: Computed as distance from user node, typically $\nu(v) = 1/(1+d(v))$ where $d(v)$ is graph distance
- **Evolution (X-axis)**: Continuous score $\varepsilon(v) \in [0,1]$ mapping to stages: Genesis $[0,0.25)$, Custom Built $[0.25,0.5)$, Product (+rental) $[0.5,0.75)$, Commodity (+utility) $[0.75,1]$. Canonical determination is by cheat sheet, not by time — see the climatic pattern *"you cannot measure evolution over time or adoption."*
- **Evolution Dynamics**: logistic S-curve $d\varepsilon/dt = r\varepsilon(1-\varepsilon)$ where $r$ incorporates market forces and strategic actions. The repo labels this as a stylized extension; Wardley's own climatic patterns say *"you cannot measure evolution over time or adoption."*
- **Dependencies**: Directed graph where $(a,b) \in E$ means "a depends on b", with constraint $\nu(a) \ge \nu(b)$

## Working with This Repository

When editing documents:
- Mathematical notation uses GitHub-native LaTeX: inline with `$...$` and display with `$$...$$`
- Maintain consistent terminology: "evolution" (X-axis), "visibility" (Y-axis), "components" (nodes)
- Documents reference Simon Wardley's original qualitative framework as the conceptual foundation
