# telecoms-sovereignty (Wardley reference, Mermaid rendering)

Source: [`/workspaces/wardleymap_math_model/skills/wardley-map-workspace/arc-kit-compare/eval-telecoms-sovereignty/wardley-reference.owm`](../../../skills/wardley-map-workspace/arc-kit-compare/eval-telecoms-sovereignty/wardley-reference.owm)

Converted from OWM via `scripts/owm_to_mermaid.py`.

```mermaid
wardley-beta
title TELECOMS - Sovereignty - OCT 2022
component corporation [1.00, 0.57]
component people [0.94, 0.69]
component GOVERNMENT [1.00, 0.63]
component COLLECTIVE [0.98, 0.67]
component perception of success [0.92, 0.63]
component COMMUNICATION [0.78, 0.66]
component LEGITIMACY [0.95, 0.60]
component SOVEREIGNTY [0.86, 0.53]
component territorial [0.84, 0.72]
component political [0.84, 0.62]
component cultural [0.84, 0.67]
component economic [0.84, 0.44]
component digital [0.84, 0.33]
component CNI [0.84, 0.52]
component ACCESS DEVICE [0.74, 0.70]
component radio and TV [0.72, 0.76]
component smartphone [0.72, 0.66]
component sat phone [0.72, 0.60]
component computer [0.72, 0.73]
component IoT [0.72, 0.56]
component doves [0.24, 0.67]
component ACCESS NETWORK [0.64, 0.73]
component satellite [0.37, 0.72]
component Towers [0.37, 0.45]
component cable [0.37, 0.37]
component launch vehicles [0.31, 0.65]
component NETWORK EQPT [0.30, 0.51]
component quantum network [0.53, 0.19]
component NETWORK TOPOLOGY [0.39, 0.64]
component Fixed [0.62, 0.74]
component Mobile [0.62, 0.68]
component THEATRE [0.21, 0.50]
component awareness of land sea air space [0.19, 0.70]
component awareness of supply chains [0.19, 0.35]
component peering [0.53, 0.63]
component REALITY [0.09, 0.49]
component geography [0.07, 0.31]
component physical supply chain [0.07, 0.64]
component space [0.07, 0.72]
component Compute [0.19, 0.83]
component Power [0.05, 0.84]
component information supply chain [0.07, 0.59]
component CONTROL LAYER [0.55, 0.67]
component DNSoverHTTPS [0.53, 0.51]
component NationStateFirewalls [0.53, 0.44]
component SIMS [0.53, 0.73]
component geofencing [0.53, 0.56]
component Real estate [0.29, 0.31]
component EXPERTISE [0.27, 0.46]
GOVERNMENT -> COLLECTIVE
COLLECTIVE -> people
GOVERNMENT -> LEGITIMACY
LEGITIMACY -> SOVEREIGNTY
people -> perception of success
perception of success -> CNI
digital -> awareness of supply chains
awareness of supply chains -> economic
satellite -> launch vehicles
awareness of land sea air space -> territorial
geography -> awareness of land sea air space
space -> awareness of land sea air space
COMMUNICATION -> ACCESS DEVICE
COMMUNICATION -> ACCESS NETWORK
ACCESS NETWORK -> Compute
Compute -> Power
CNI -> COMMUNICATION
Real estate -> geography
NETWORK EQPT -> EXPERTISE
awareness of supply chains -> EXPERTISE
EXPERTISE -> awareness of land sea air space
information supply chain -> NETWORK EQPT
NETWORK EQPT -> physical supply chain
information supply chain -> awareness of supply chains
physical supply chain -> awareness of supply chains
Towers -> Real estate
cable -> Real estate
NETWORK TOPOLOGY -> NETWORK EQPT
Mobile -> satellite
CONTROL LAYER -> NETWORK TOPOLOGY
CONTROL LAYER -> ACCESS NETWORK
corporation -> SOVEREIGNTY
satellite -> doves
```
