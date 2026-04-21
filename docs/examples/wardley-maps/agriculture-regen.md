# agriculture-regen (Wardley reference, Mermaid rendering)

Source: [`/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare/eval-agriculture-regen/wardley-reference.owm`](../../../skills/wardley-map-workspace/arc-kit-compare/eval-agriculture-regen/wardley-reference.owm)

Converted from OWM via `scripts/owm_to_mermaid.py`.

```mermaid
wardley-beta
title AGRICULTURE - regenerative farming - AUG 2022
component nutrient density [0.87, 0.39]
component preservation [0.67, 0.63]
component water [0.34, 0.71]
component forestation [0.67, 0.49]
component breeding [0.67, 0.56]
component heritage [0.87, 0.46]
component food security [0.87, 0.49]
component vertical [0.49, 0.38]
component CONSERVATION [0.69, 0.58]
component CERTIFICATION BODIES [0.62, 0.36]
component SUBSTRATE [0.36, 0.72]
component territory [0.62, 0.74]
component landscape [0.30, 0.30]
component supply chain awareness [0.32, 0.19]
component behaviour [0.72, 0.21]
component marking visual feedback [0.65, 0.17]
component gov [0.92, 0.57]
component policy [0.80, 0.51]
component SUPRANATIONAL UN [0.98, 0.50]
component TREATY [0.89, 0.42]
component social knowledge [0.40, 0.31]
component knowledge based systems [0.40, 0.66]
component MEASURE [0.76, 0.73]
component grade [0.74, 0.79]
component RETAIL LOCATION [0.96, 0.65]
component farmer [0.70, 0.66]
component consumer [0.95, 0.71]
component profit [0.86, 0.74]
component quality [0.74, 0.51]
component standardised [0.82, 0.65]
component logistics [0.88, 0.68]
component Food [0.81, 0.73]
component soil [0.34, 0.74]
component FARMING PRACTICE [0.51, 0.66]
component regenerative at scale [0.49, 0.31]
component extractive at scale [0.49, 0.77]
component CROP [0.27, 0.71]
component monoculture [0.25, 0.74]
component diversity [0.25, 0.41]
component rotation [0.25, 0.64]
component ENERGY MATRIX [0.17, 0.72]
component microbes [0.08, 0.69]
component photosynthesis [0.15, 0.74]
component microbial quorum [0.06, 0.39]
component signalling [0.02, 0.33]
component synthetics [0.15, 0.69]
component petrochemical [0.08, 0.73]
component supply chain [0.02, 0.61]
component environment [0.04, 0.70]
microbes -> microbial quorum
microbial quorum -> signalling
petrochemical -> synthetics
regenerative at scale -> photosynthesis
extractive at scale -> monoculture
diversity -> regenerative at scale
monoculture -> ENERGY MATRIX
regenerative at scale -> microbial quorum
Food -> farmer
consumer -> Food
RETAIL LOCATION -> profit
Food -> MEASURE
profit -> standardised
standardised -> MEASURE
logistics -> RETAIL LOCATION
logistics -> standardised
farmer -> FARMING PRACTICE
CERTIFICATION BODIES -> standardised
SUBSTRATE -> FARMING PRACTICE
CONSERVATION -> FARMING PRACTICE
gov -> policy
policy -> CONSERVATION
SUPRANATIONAL UN -> gov
SUPRANATIONAL UN -> TREATY
TREATY -> policy
TREATY -> diversity
gov -> territory
territory -> SUBSTRATE
regenerative at scale -> social knowledge
territory -> landscape
social knowledge -> landscape
SUBSTRATE -> landscape
extractive at scale -> knowledge based systems
consumer -> behaviour
behaviour -> marking visual feedback
marking visual feedback -> supply chain awareness
FARMING PRACTICE -> supply chain awareness
policy -> behaviour
supply chain -> CROP
supply chain awareness -> supply chain
soil -> microbes
environment -> microbes
CERTIFICATION BODIES -> social knowledge
CERTIFICATION BODIES -> marking visual feedback
grade -> extractive at scale
note "+Knowledge based system" [0.38, 0.35]
note "+dependency" [0.11, 0.72]
note "+climate change" [0.02, 0.71]
note "+ incl community driven schemes" [0.68, 0.27]
```
