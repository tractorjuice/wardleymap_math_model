
# Wardley Map Generator Prompt

Use this prompt to create a mathematically-grounded Wardley Map for any domain, system, or business scenario.

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
- Second level: ν = 0.33 (d=2)
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

### 6. Output Format

Provide the map in this structured format:

```yaml
wardley_map:
  name: "[Map Name]"
  anchor: "[User Need]"

  components:
    - name: "[Component Name]"
      visibility: [0-1]
      evolution: [0-1]
      stage: "[Genesis|Custom|Product|Commodity]"
      depends_on: ["Component1", "Component2"]

  metrics:
    differentiation_pressure:
      - component: "[Name]"
        score: [0-1]
    commodity_leverage:
      - component: "[Name]"
        score: [0-1]
    dependency_risks:
      - edge: "[A] → [B]"
        score: [0-1]

  strategic_insights:
    - "[Insight based on metrics]"
```

### 7. Visual Representation

Also provide an ASCII representation:

```
Visibility (ν)
    1.0 |  [User Need]
        |
    0.5 |     [Component A]
        |
    0.33|        [B]    [C]
        |
    0.25|           [D]
        |
    0.0 +---------------------------
        0    0.25   0.5   0.75   1.0
             Genesis Custom Product Commodity
                    Evolution (ε) →
```

---

Now analyze the following scenario and create a Wardley Map:

[INSERT YOUR SCENARIO HERE]
```

---

## Example Usage

**Input Scenario:**
> "An e-commerce company selling handmade crafts online. They need to handle product listings, payments, shipping, and customer service."

**The prompt will generate:**
1. Components like: Customer Need, Online Storefront, Product Catalog, Payment Processing, Shipping Integration, Customer Support, Cloud Hosting, etc.
2. Dependencies showing how each component relates
3. Calculated visibility based on distance from customer
4. Evolution estimates based on market maturity signals
5. Strategic metrics highlighting opportunities and risks
6. Structured YAML output and ASCII visualization

---

## Customization Options

Add these to the prompt for specific needs:

**For dynamics/time evolution:**
```
Also model how components might evolve over 2 years using:
dε/dt = r × (1 - ε)
Where r = baseline_pressure + your_actions - friction
```

**For uncertainty:**
```
Express confidence in positions using Beta distributions:
ε(v) ~ Beta(α, β) where mean = α/(α+β)
Include uncertainty ranges in output.
```

**For competitive analysis:**
```
Include competitor positions on the same map.
Identify where competitors are investing.
```
