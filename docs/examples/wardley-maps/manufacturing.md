# manufacturing (Wardley reference, Mermaid rendering)

Source: [`/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare/eval-manufacturing/wardley-reference.owm`](../../../skills/wardley-map-workspace/arc-kit-compare/eval-manufacturing/wardley-reference.owm)

Converted from OWM via `scripts/owm_to_mermaid.py`. Some edges may be dropped if endpoints weren't declared in the source (Wardley sometimes names components in edges that don't appear in the declaration list).

```mermaid
wardley-beta
title manufacturing - SUPPLY CHAINs, Feb 2023
component PRODUCT [0.87, 0.64]
component sales forecasting [0.82, 0.62]
component R&D [0.51, 0.22]
component prototype [0.73, 0.19]
component trial [0.72, 0.34]
component EQUIPMENT [0.67, 0.61]
component government [0.93, 0.56]
component manufacturer [0.95, 0.65]
component REGULATION [0.65, 0.47]
component lobbying [0.63, 0.38]
component compliance [0.63, 0.53]
component safety [0.87, 0.55]
component distributor [0.92, 0.48]
component IP [0.74, 0.49]
component MATERIALS [0.58, 0.63]
component raw [0.57, 0.75]
component branded [0.56, 0.50]
component refined [0.56, 0.69]
component novel [0.56, 0.41]
component design [0.72, 0.42]
component relationships [0.72, 0.53]
component SUPPLY CHAIN [0.44, 0.62]
component agility [0.81, 0.33]
component METRICS [0.10, 0.43]
component visibility [0.31, 0.30]
component AWARENESS [0.67, 0.28]
component certification [0.51, 0.70]
component automation [0.19, 0.27]
component clipboard [0.19, 0.67]
component reliability [0.78, 0.70]
component INVENTORY MANAGEMENT [0.33, 0.64]
component just in time [0.31, 0.69]
component just in case [0.31, 0.52]
component warehousing [0.26, 0.66]
component cost [0.76, 0.78]
component forecasting [0.36, 0.44]
component LOGISTICS [0.21, 0.60]
component rate of change [0.20, 0.41]
component data [0.02, 0.66]
component ROCE [0.91, 0.72]
component ENERGY [0.39, 0.70]
component CNI [0.76, 0.57]
component capital [0.85, 0.78]
component authority [0.49, 0.51]
agility -> prototype
visibility -> AWARENESS
AWARENESS -> SUPPLY CHAIN
R&D -> SUPPLY CHAIN
visibility -> rate of change
rate of change -> METRICS
manufacturer -> agility
manufacturer -> reliability
distributor -> relationships
government -> safety
safety -> REGULATION
reliability -> SUPPLY CHAIN
SUPPLY CHAIN -> INVENTORY MANAGEMENT
SUPPLY CHAIN -> LOGISTICS
REGULATION -> certification
warehousing -> INVENTORY MANAGEMENT
forecasting -> AWARENESS
certification -> METRICS
MATERIALS -> SUPPLY CHAIN
agility -> AWARENESS
AWARENESS -> R&D
data -> METRICS
manufacturer -> ROCE
relationships -> SUPPLY CHAIN
manufacturer -> design
government -> CNI
CNI -> SUPPLY CHAIN
capital -> ROCE
cost -> MATERIALS
design -> R&D
SUPPLY CHAIN -> forecasting
PRODUCT -> manufacturer
PRODUCT -> cost
PRODUCT -> sales forecasting
PRODUCT -> MATERIALS
ROCE -> PRODUCT
certification -> MATERIALS
authority -> certification
SUPPLY CHAIN -> ENERGY
novel -> R&D
cost -> EQUIPMENT
EQUIPMENT -> MATERIALS
EQUIPMENT -> certification
```
