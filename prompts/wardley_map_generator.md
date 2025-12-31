# Wardley Map Generator Prompt

Use this prompt to create a mathematically-grounded Wardley Map for any domain, system, or business scenario. Outputs in OWM (Online Wardley Maps) format compatible with [onlinewardleymaps.com](https://onlinewardleymaps.com).

---

## Prompt

```
You are a Wardley Mapping expert using a formal mathematical model. Given a description of a system, business, or domain, create a Wardley Map by following this structured approach:

## Mathematical Model

A Wardley Map is defined as a tuple: M = (V, E, u, ν, ε)

Where:
- V = set of components
- E ⊆ V × V = directed dependency edges (a,b) means "a depends on b"
- u ∈ V = anchor node (user need)
- ν: V → [0,1] = visibility score (Y-axis)
- ε: V → [0,1] = evolution score (X-axis)

## Your Task

For the given scenario, produce:

### 1. Components (V)
List all components as concrete nouns. Include:
- The user/customer need (anchor node u)
- Activities, capabilities, data, systems
- Suppliers, practices, infrastructure

### 2. Dependencies (E)
For each component, list what it depends on using the format:
- (A, B) means "A depends on B"
Ensure dependencies form a directed acyclic graph flowing from user need downward.

### 3. Visibility Scores (ν)
Calculate visibility using graph distance from the user:
- d(v) = shortest path length from user to component v
- ν(v) = 1 / (1 + d(v))

This ensures:
- User need: ν = 1.0 (d=0)
- Direct dependencies: ν = 0.5 (d=1)
- Second level: ν ≈ 0.33 (d=2)
- Third level: ν = 0.25 (d=3)
- And so on...

### 4. Evolution Scores (ε)
Estimate evolution using these signals (score 0-1 for each, then average):
- Ubiquity: How widespread? (0=rare, 1=everywhere)
- Certainty: How standardized? (0=novel/uncertain, 1=well-defined)
- Number of suppliers: (0=single source, 1=many alternatives)
- Price transparency: (0=opaque, 1=clear market pricing)
- Change rate: (0=rapidly changing, 1=stable)

Evolution stages:
- Genesis: [0, 0.25) - Novel, uncertain, requires exploration
- Custom Built: [0.25, 0.5) - Emerging understanding, bespoke solutions
- Product: [0.5, 0.75) - Increasingly standardized, rental/product models
- Commodity: [0.75, 1.0] - Standardized, utility, interchangeable

### 5. Derived Metrics
Calculate strategic indicators:

**Differentiation Pressure:** D(v) = ν(v) × (1 - ε(v))
- High D = visible + immature = opportunity for competitive advantage

**Commodity Leverage:** K(v) = (1 - ν(v)) × ε(v)
- High K = hidden + mature = candidate for outsourcing/automation

**Dependency Risk:** R(a,b) = ν(a) × (1 - ε(b))
- High R = visible component depends on immature foundation = risk

### 6. Output in OWM Format

Output the map in OWM (Online Wardley Maps) format. This format uses [visibility, evolution] coordinates where both values are between 0 and 1.

**OWM Syntax:**
- `title Map Title` - The map title
- `anchor Anchor Name [visibility, evolution]` - The user need (top of map)
- `component Component Name [visibility, evolution]` - Each component
- `Component A->Component B` - Dependency arrows (A depends on B)
- `evolve Component Name target_evolution` - Show evolution movement
- `note Note text [visibility, evolution]` - Add annotations
- `style wardley` - Use Wardley styling

**Template:**
```owm
title [Map Name]
style wardley

// Anchor (user need)
anchor [User Need] [visibility, evolution]

// Components by visibility layer
component [Component 1] [visibility, evolution]
component [Component 2] [visibility, evolution]
component [Component 3] [visibility, evolution]
// ... more components

// Dependencies (component -> what it depends on)
[User Need]->[Component 1]
[Component 1]->[Component 2]
[Component 1]->[Component 3]
// ... more dependencies

// Evolution movements (optional)
evolve [Component Name] [target_evolution]

// Strategic notes (optional)
note High differentiation opportunity [0.7, 0.2]
note Commodity candidate [0.2, 0.85]
```

### 7. Strategic Analysis

After the OWM output, provide:

1. **Top 3 Differentiation Opportunities** (highest D scores)
2. **Top 3 Commodity/Outsource Candidates** (highest K scores)
3. **Top 3 Dependency Risks** (highest R scores)
4. **Recommended Strategic Moves**

---

Now analyze the following scenario and create a Wardley Map:

[INSERT YOUR SCENARIO HERE]
```

---

## Example Output

For an e-commerce handmade crafts business:

```owm
title Handmade Crafts E-Commerce
style wardley

// Anchor - User Need
anchor Customer Purchase [0.95, 0.58]

// High visibility components
component Online Storefront [0.78, 0.62]
component Product Discovery [0.75, 0.45]
component Shopping Cart [0.72, 0.71]

// Mid visibility components
component Product Catalog [0.55, 0.52]
component Artisan Onboarding [0.52, 0.35]
component Payment Processing [0.50, 0.82]
component Order Management [0.48, 0.55]

// Lower visibility components
component Shipping Integration [0.35, 0.72]
component Inventory System [0.32, 0.48]
component Customer Support [0.30, 0.45]

// Infrastructure
component Cloud Hosting [0.18, 0.89]
component Database [0.15, 0.85]
component CDN [0.12, 0.92]

// Dependencies
Customer Purchase->Online Storefront
Online Storefront->Product Discovery
Online Storefront->Shopping Cart
Online Storefront->Product Catalog
Product Discovery->Product Catalog
Shopping Cart->Payment Processing
Shopping Cart->Order Management
Product Catalog->Inventory System
Product Catalog->Artisan Onboarding
Order Management->Shipping Integration
Order Management->Inventory System
Customer Support->Order Management
Online Storefront->Cloud Hosting
Product Catalog->Database
Online Storefront->CDN

// Evolution targets
evolve Artisan Onboarding 0.55
evolve Product Discovery 0.60

// Strategic notes
note Differentiation opportunity [0.65, 0.30]
note Outsource candidate [0.25, 0.88]
```

---

## Customization Options

Add these to the prompt for specific needs:

**For evolution over time:**
```
Show future evolution using:
evolve [Component] [target_evolution]

Model movement using: dε/dt = r × (1 - ε)
Where r = baseline_pressure + your_actions - friction
```

**For inertia indicators:**
```
Add inertia markers for components resistant to change:
component [Name] [vis, evo] inertia
```

**For build/buy decisions:**
```
Mark components with build/buy annotations:
build [Component Name]
buy [Component Name]
outsource [Component Name]
```

**For pipelines:**
```
Group related components:
pipeline [Component] [start_evo, end_evo]
```

---

## OWM Format Reference

| Element | Syntax | Example |
|---------|--------|---------|
| Title | `title Name` | `title My Map` |
| Style | `style wardley` | `style wardley` |
| Anchor | `anchor Name [v, e]` | `anchor Customer Need [0.95, 0.5]` |
| Component | `component Name [v, e]` | `component API [0.45, 0.72]` |
| Dependency | `A->B` | `Website->API` |
| Evolution | `evolve Name target` | `evolve API 0.85` |
| Note | `note Text [v, e]` | `note Risk area [0.5, 0.3]` |
| Pipeline | `pipeline Name [s, e]` | `pipeline Platform [0.3, 0.8]` |
| Inertia | `component Name [v, e] inertia` | `component Legacy [0.4, 0.3] inertia` |
| Label | `component Name [v, e] label [-x, y]` | `component API [0.5, 0.7] label [-10, 5]` |

Coordinates: `[visibility, evolution]` where both are 0-1 scale.
- Visibility: 1.0 = top (user-facing), 0.0 = bottom (infrastructure)
- Evolution: 0.0 = genesis (left), 1.0 = commodity (right)
