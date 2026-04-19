# agriculture-regen (ours-v2) — draft promoted

Subagent hung after validator pass. Draft was already validator-clean (see parent session).

```owm
title Regenerative Farming Landscape (Aug 2022, IRA week)
style wardley

// Anchors — three principal user-needs in the regen-ag value chain
anchor Farmer [0.99, 0.35]
anchor Consumer [0.97, 0.65]
anchor Funder / Policy-Maker [0.95, 0.50]

// --- Farm-level outcomes / products (user-facing) ---
component Farm Livelihood / Profit [0.90, 0.55]
component Regen-branded CPG Product [0.88, 0.50]
component Eco-label on Shelf [0.84, 0.58]
component Ecosystem Services [0.82, 0.18]
component Consumer Trust in Claim [0.80, 0.25]
component Retailer / Grocery Channel [0.78, 0.78]
component On-farm Biodiversity [0.74, 0.22]
component Soil Health Outcomes [0.72, 0.28]
component Carbon Sequestration Outcomes [0.70, 0.20]
component Regenerative Produce [0.60, 0.45]

// --- Certifications ---
component Regenerative Certification [0.68, 0.32]
component Organic Certification (USDA NOP) [0.66, 0.80]

// --- Supply chain to consumer ---
component Food Processor / Aggregator [0.64, 0.70]
component CPG Brand Sourcing Program [0.64, 0.40]
component Cold Chain & Logistics [0.40, 0.88]
component Traceability Platform [0.50, 0.42]

// --- On-farm practices (Practices layer) ---
component Cover Cropping [0.58, 0.60]
component No-till / Reduced Till [0.56, 0.68]
component Rotational / Adaptive Grazing [0.54, 0.40]
component Diverse Crop Rotation [0.52, 0.62]
component Integrated Livestock [0.50, 0.35]
component Agroforestry / Silvopasture [0.46, 0.22]
component Reduced Synthetic Inputs [0.48, 0.55]

// --- Farmer capability & advisory ---
component Farmer Knowledge & Mindset Shift [0.42, 0.25]
component Technical Assistance (NRCS / TSPs) [0.38, 0.55]
component Peer Farmer Networks [0.36, 0.30]
component Extension & Land-Grant Research [0.34, 0.50]

// --- Funding sources (push funders into mid-chain — they are upstream) ---
component Crop Insurance (RMA) [0.60, 0.85]
component USDA EQIP / CSP Payments [0.36, 0.62]
component USDA Climate-Smart Commodities Grants [0.32, 0.25]
component Private Sustainability-Linked Finance [0.44, 0.35]
component Philanthropic / Foundation Grants [0.58, 0.45]
component IRA Climate-Smart Ag Funding [0.20, 0.15]

// --- Measurement, reporting, verification (MRV) ---
component Soil Carbon MRV Protocol [0.50, 0.18]
component Soil Sampling & Lab Analysis [0.44, 0.72]
component Life-Cycle / Scope 3 Accounting [0.40, 0.30]
component Remote Sensing / Satellite Modelling [0.34, 0.45]
component Farm Data Platform [0.30, 0.40]

// --- Carbon & ecosystem markets ---
component Voluntary Carbon Credits (soil) [0.52, 0.22]
component Biodiversity / Water Credits [0.34, 0.12]
component Carbon Registry & Standard [0.26, 0.30]

// --- Inputs & deep infrastructure ---
component Seed & Cover-Crop Seed Supply [0.30, 0.72]
component Biological Inputs (biofertiliser etc.) [0.28, 0.30]
component Farm Machinery (no-till drills) [0.26, 0.68]
component Land Tenure & Leases [0.22, 0.55]
component Rural Broadband [0.14, 0.78]
component Cloud Compute [0.08, 0.92]

// --- Notes & zones ---
note Differentiation / BUILD [0.55, 0.20]
note Industrialising frontier [0.40, 0.40]
note Utility — rent/leverage [0.15, 0.88]
note IRA shockwave (16 Aug 2022) [0.88, 0.12]

// === Dependencies (a depends on b) ===

// Anchors -> top outcomes
Farmer->Farm Livelihood / Profit
Farmer->Regenerative Produce
Farmer->Ecosystem Services
Consumer->Regen-branded CPG Product
Consumer->Eco-label on Shelf
Consumer->Consumer Trust in Claim
Funder / Policy-Maker->Ecosystem Services
Funder / Policy-Maker->Carbon Sequestration Outcomes
Funder / Policy-Maker->On-farm Biodiversity

// Produce / brand chain
Regen-branded CPG Product->Regenerative Produce
Regen-branded CPG Product->Eco-label on Shelf
Regen-branded CPG Product->CPG Brand Sourcing Program
Eco-label on Shelf->Regenerative Certification
Eco-label on Shelf->Organic Certification (USDA NOP)
Consumer Trust in Claim->Regenerative Certification
Consumer Trust in Claim->Traceability Platform

// Retail & supply chain
Regen-branded CPG Product->Retailer / Grocery Channel
Retailer / Grocery Channel->Cold Chain & Logistics
CPG Brand Sourcing Program->Food Processor / Aggregator
CPG Brand Sourcing Program->Traceability Platform
Food Processor / Aggregator->Cold Chain & Logistics
Food Processor / Aggregator->Regenerative Produce

// Produce comes from practices & land
Regenerative Produce->Cover Cropping
Regenerative Produce->Diverse Crop Rotation
Regenerative Produce->Reduced Synthetic Inputs
Regenerative Produce->Seed & Cover-Crop Seed Supply

// Farm livelihood
Farm Livelihood / Profit->Regen-branded CPG Product
Farm Livelihood / Profit->USDA EQIP / CSP Payments
Farm Livelihood / Profit->Voluntary Carbon Credits (soil)
Farm Livelihood / Profit->Crop Insurance (RMA)

// Ecosystem-service outcomes -> practices
Ecosystem Services->On-farm Biodiversity
Ecosystem Services->Soil Health Outcomes
Ecosystem Services->Carbon Sequestration Outcomes
On-farm Biodiversity->Diverse Crop Rotation
On-farm Biodiversity->Agroforestry / Silvopasture
On-farm Biodiversity->Integrated Livestock
Soil Health Outcomes->Cover Cropping
Soil Health Outcomes->No-till / Reduced Till
Soil Health Outcomes->Rotational / Adaptive Grazing
Soil Health Outcomes->Biological Inputs (biofertiliser etc.)
Carbon Sequestration Outcomes->No-till / Reduced Till
Carbon Sequestration Outcomes->Cover Cropping
Carbon Sequestration Outcomes->Agroforestry / Silvopasture
Carbon Sequestration Outcomes->Rotational / Adaptive Grazing

// Practices depend on capability and inputs
Cover Cropping->Seed & Cover-Crop Seed Supply
Cover Cropping->Farmer Knowledge & Mindset Shift
No-till / Reduced Till->Farm Machinery (no-till drills)
No-till / Reduced Till->Farmer Knowledge & Mindset Shift
Rotational / Adaptive Grazing->Farmer Knowledge & Mindset Shift
Rotational / Adaptive Grazing->Land Tenure & Leases
Diverse Crop Rotation->Farmer Knowledge & Mindset Shift
Integrated Livestock->Farmer Knowledge & Mindset Shift
Agroforestry / Silvopasture->Land Tenure & Leases
Agroforestry / Silvopasture->Farmer Knowledge & Mindset Shift
Reduced Synthetic Inputs->Biological Inputs (biofertiliser etc.)

// Farmer capability
Farmer Knowledge & Mindset Shift->Technical Assistance (NRCS / TSPs)
Farmer Knowledge & Mindset Shift->Peer Farmer Networks
Farmer Knowledge & Mindset Shift->Extension & Land-Grant Research
Technical Assistance (NRCS / TSPs)->USDA EQIP / CSP Payments

// Certifications depend on MRV
Regenerative Certification->Soil Carbon MRV Protocol
Regenerative Certification->Traceability Platform
Organic Certification (USDA NOP)->Soil Sampling & Lab Analysis
Traceability Platform->Farm Data Platform

// MRV stack
Soil Carbon MRV Protocol->Soil Sampling & Lab Analysis
Soil Carbon MRV Protocol->Remote Sensing / Satellite Modelling
Soil Carbon MRV Protocol->Farm Data Platform
Farm Data Platform->Cloud Compute
Farm Data Platform->Rural Broadband
Remote Sensing / Satellite Modelling->Cloud Compute
Life-Cycle / Scope 3 Accounting->Farm Data Platform
Life-Cycle / Scope 3 Accounting->Remote Sensing / Satellite Modelling

// Carbon markets
Voluntary Carbon Credits (soil)->Soil Carbon MRV Protocol
Voluntary Carbon Credits (soil)->Carbon Registry & Standard
Biodiversity / Water Credits->Carbon Registry & Standard
Biodiversity / Water Credits->Remote Sensing / Satellite Modelling

// Funding
USDA EQIP / CSP Payments->IRA Climate-Smart Ag Funding
USDA Climate-Smart Commodities Grants->IRA Climate-Smart Ag Funding
Private Sustainability-Linked Finance->Life-Cycle / Scope 3 Accounting
Philanthropic / Foundation Grants->Peer Farmer Networks
CPG Brand Sourcing Program->Private Sustainability-Linked Finance
CPG Brand Sourcing Program->Philanthropic / Foundation Grants

// Evolve arrows — plausible trajectories over next 3–5 years
evolve Soil Carbon MRV Protocol 0.55
evolve Regenerative Certification 0.60
evolve Voluntary Carbon Credits (soil) 0.45
evolve Remote Sensing / Satellite Modelling 0.70
evolve Farm Data Platform 0.65
evolve Biological Inputs (biofertiliser etc.) 0.55
evolve Traceability Platform 0.65
```
