# Mathematical Models for Wardley Mapping

This repository contains research and theoretical frameworks for formalizing [Wardley Mapping](https://learnwardleymapping.com/) as a mathematical model. The goal is to transform Wardley Maps from a purely visual and qualitative strategic tool into a quantitative framework that enables computation, simulation, and data-driven strategic decision-making.

## What is Wardley Mapping?

Wardley Mapping, created by Simon Wardley, is a visual technique for mapping business strategy. A Wardley Map plots components on two axes:

- **Y-axis (Visibility)**: How close a component is to the end user
- **X-axis (Evolution)**: How mature/commoditized a component is, from Genesis → Custom → Product → Commodity

Components are connected by dependency relationships forming a value chain.

## The Mathematical Approach

This repository explores how to formalize these concepts mathematically. A Wardley Map becomes:

$$\mathcal{M} = (V, E, u, \nu, \varepsilon, t)$$

Where:
- $V$ = set of components
- $E \subseteq V \times V$ = directed dependency edges
- $u \in V$ = anchor node (user need)
- $\nu: V \to [0,1]$ = visibility function (Y-axis)
- $\varepsilon: V \to [0,1]$ = evolution function (X-axis)
- $t$ = time parameter for dynamics

This formalization enables:
- Generating maps from data
- Validating maps with constraints
- Quantifying strategic positions
- Simulating evolution over time
- Computing decision metrics (differentiation pressure, commodity leverage, dependency risk)

## Documents

### Core Model
| Document | Description |
|----------|-------------|
| [A Prototype Math Model for Wardley Mapping](A%20Prototype%20Math%20Model%20for%20Wardley%20Mapping.md) | Exploratory prototype introducing S-curve evolution dynamics and game-theoretic extensions |

### Comprehensive Framework
| Document | Description |
|----------|-------------|
| [The Mathematical Framework of Wardley Mapping](The%20Mathematical%20Framework%20of%20Wardley%20Mapping.md) | Extended treatment covering graph theory, game theory, probability, and machine learning applications |

### Strategy & Gameplay
| Document | Description |
|----------|-------------|
| [Strategic Mastery: Creating Math Models for Wardley Mapping Gameplays](Strategic%20Mastery%3A%20Creating%20Math%20Models%20for%20Wardley%20Mapping%20Gameplays.md) | Quantitative approaches to strategic plays and decision-making |
| [Mathematical Models for Wardley Mapping Gameplay](Mathematical%20Models%20for%20Wardley%20Mapping%20Gameplay%3A%20A%20Quantitative%20Approach%20to%20Strategic%20Decision%20Making.md) | Detailed gameplay modeling methodology |

### Progressive Series
| Document | Description |
|----------|-------------|
| [Part 1 - Core Mathematical Model](Part%201%20-%20Core%20Mathematical%20Model%20for%20Wardley%20Mapping.md) | The formal tuple model $\mathcal{M} = (V, E, u, \nu, \varepsilon, t)$ with computed visibility, evolution scoring, and derived metrics |
| [Part 2 - Revised Model: Map Evolution, Not Maturity](Part%202%20-%20Revised%20Wardley%20Map%20Model%3A%20Map%20Evolution%2C%20Not%20Maturity.md) | Refining the evolution axis interpretation |
| [Part 3 - Explaining the Tea Shop Map](Part%203%20-%20Explaining%20the%20Tea%20Shop%20Map%20Using%20Our%20Mathematical%20Model.md) | Applying the model to a classic Wardley Map example |
| [Part 4 - Working Out Evolution Values](Part%204%20-%20Working%20Out%20the%20Evolution%20Value%20for%20a%20Single%20Component.md) | Methods for computing evolution scores |
| [Part 5 - Layer-Based Visibility and Sigmoid Evolution](Part%205%20-%20Extending%20Wardley%20Maps%3A%20Layer-Based%20Visibility%20and%20Sigmoid%20Evolution.md) | Extended model with visibility layers |

### Specialized Topics
| Document | Description |
|----------|-------------|
| [Wardley Strategy Cycle - Core Model](Wardley%20Strategy%20Cycle%20-%20Core%20Model%20-%20Part%201.md) | Modeling strategic cycles |
| [Wardley Strategy Cycle - Example](Wardley%20Strategy%20Cycle%20-%20Example%20-%20Part%202.md) | Applied example of strategy cycles |
| [Weak Signals & Evolution - Core](Weak%20Signals%20%26%20Evolution%20-%20Core%20-%20Part%201.md) | Detecting and modeling weak signals |
| [Weak Signals & Evolution - Example](Weak%20Signals%20%26%20Evolution%20-%20Example%20-%20Part%202.md) | Applied example of weak signal detection |
| [Reimagining Wardley Maps: Layer-Based Visibility](Reimagining%20Wardley%20Maps%3A%20Layer-Based%20Visibility%20and%20Sigmoid%20Evolution.md) | Alternative visibility model using layers |

### Tools & Prompts
| Document | Description |
|----------|-------------|
| [Wardley Map Generator Prompt](prompts/wardley_map_generator.md) | AI prompt for generating Wardley Maps in OWM format compatible with [create.wardleymaps.ai](https://create.wardleymaps.ai) |

## Key Formulas

**Visibility from graph distance:**

$$\nu(v) = \frac{1}{1 + d(v)}$$

where $d(v)$ is the shortest path length from user to component.

**Evolution dynamics (S-curve):**

$$\frac{d\varepsilon}{dt} = r(t) \cdot (1 - \varepsilon(t))$$

where $r(t)$ incorporates market forces and strategic actions.

**Evolution stages:**
- Genesis: $[0, 0.25)$
- Custom Built: $[0.25, 0.50)$
- Product: $[0.50, 0.75)$
- Commodity: $[0.75, 1.0]$

**Decision metrics:**
- Differentiation pressure: $D(v) = \nu(v) \cdot (1 - \varepsilon(v))$
- Commodity leverage: $K(v) = (1 - \nu(v)) \cdot \varepsilon(v)$
- Dependency risk: $R(a,b) = \nu(a) \cdot (1 - \varepsilon(b))$

## License

This repository contains theoretical research and documentation.

## Acknowledgments

Based on the Wardley Mapping framework created by Simon Wardley.
