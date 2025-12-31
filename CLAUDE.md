# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This is a documentation-only research repository containing mathematical models and frameworks for Wardley Mapping. There is no code, build system, or tests - the repository consists entirely of markdown files presenting theoretical work on quantifying Wardley Maps.

## Content Structure

The repository contains research documents exploring how to formalize Wardley Mapping mathematically:

- **Core Mathematical Model** (`Part 1 - Core Mathematical Model for Wardley Mapping.md`, `A Prototype Math Model for Wardley Mapping.md`): Defines a Wardley Map as a tuple $\mathcal{M} = (V, E, u, \nu, \varepsilon, t)$ where V is components, E is dependency edges, $\nu$ is visibility function (Y-axis), and $\varepsilon$ is evolution function (X-axis)

- **Comprehensive Framework** (`The Mathematical Framework of Wardley Mapping.md`): Extended treatment covering graph theory, game theory, probability, and machine learning applications

- **Strategy & Gameplay** (`Strategic Mastery: Creating Math Models for Wardley Mapping Gameplays.md`, `Mathematical Models for Wardley Mapping Gameplay...`): Quantitative approaches to strategic decision-making

- **Series Documents** (`Part 2-5`, `Wardley Strategy Cycle`, `Weak Signals & Evolution`): Progressive development of specific model aspects including evolution dynamics, visibility layers, and signal detection

## Key Mathematical Concepts

- **Visibility (Y-axis)**: Computed as distance from user node, typically $\nu(v) = 1/(1+d(v))$ where $d(v)$ is graph distance
- **Evolution (X-axis)**: Continuous score $\varepsilon(v) \in [0,1]$ mapping to stages: Genesis $[0,0.25)$, Custom $[0.25,0.5)$, Product $[0.5,0.75)$, Commodity $[0.75,1]$
- **Evolution Dynamics**: S-curve model $d\varepsilon/dt = r(1-\varepsilon)$ where $r$ incorporates market forces and strategic actions
- **Dependencies**: Directed graph where $(a,b) \in E$ means "a depends on b", with constraint $\nu(a) \ge \nu(b)$

## Working with This Repository

When editing documents:
- Mathematical notation uses GitHub-native LaTeX: inline with `$...$` and display with `$$...$$`
- Maintain consistent terminology: "evolution" (X-axis), "visibility" (Y-axis), "components" (nodes)
- Documents reference Simon Wardley's original qualitative framework as the conceptual foundation
