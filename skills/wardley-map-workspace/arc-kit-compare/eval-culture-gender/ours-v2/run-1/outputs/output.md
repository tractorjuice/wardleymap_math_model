# culture-gender (ours-v2) — draft promoted

Subagent hung after validator pass. Draft was already validator-clean (see parent session).

```owm
title Cultural Landscape of Gender in Society (March 2022)
style wardley

// Anchors — three stakeholder types navigating contested cultural terrain
anchor Individual Person [0.98, 0.40]
anchor Institution (school / sport / workplace / clinic) [0.95, 0.55]
anchor Policymaker / Regulator [0.92, 0.50]

// Identity / lived practice (user-facing, mostly contested)
component Pronoun Disclosure Norms [0.86, 0.40]
component Trans Identity Claim [0.84, 0.35]
component Coming-Out Practices [0.82, 0.60]
component Non-Binary Recognition [0.80, 0.20]
component Self-ID Claim [0.78, 0.22]
component Gender-Neutral Facilities Norm [0.75, 0.30]

// Advocacy / counter-advocacy (mid-chain enabling structures)
component Trans Rights Advocacy [0.55, 0.55]
component Gender-Critical Advocacy [0.54, 0.35]
component Parental-Rights Movement [0.56, 0.40]
component Religious-Conservative Advocacy [0.50, 0.70]
component Detransitioner Voices [0.40, 0.18]

// Institutional policy
component School Curriculum Policy on Gender [0.72, 0.38]
component Sports Eligibility Policy (NCAA / IOC) [0.70, 0.32]
component Workplace DEI Policy [0.68, 0.55]
component Bathroom / Facilities Policy [0.65, 0.42]
component Healthcare Provider Protocols [0.58, 0.48]
component Prison Housing Policy [0.50, 0.35]

// Media / platform norms
component Social-Media Discourse Norms [0.70, 0.30]
component Journalistic Style Guides (AP / BBC) [0.58, 0.60]
component Newsroom Balance Conventions [0.60, 0.55]
component Platform Content Moderation Policy [0.56, 0.45]

// Legal frameworks
component HB 1557 "Parental Rights in Education" (FL) [0.58, 0.28]
component Scotland GRR Bill (self-ID) [0.57, 0.25]
component US Equality Act (stalled) [0.55, 0.15]
component Belief Protection (Forstater precedent) [0.54, 0.40]
component Title IX Interpretation (US) [0.53, 0.50]
component Gender Recognition Certificate (UK GRA 2004) [0.52, 0.60]
component Marriage Equality Law [0.51, 0.80]
component Equality Act 2010 / Anti-Discrimination Statutes [0.50, 0.70]
component Legal Sex Marker on Documents [0.45, 0.72]

// Clinical & evidential
component Gender-Affirming Care Pathway (Adult) [0.58, 0.55]
component Gender-Affirming Care Pathway (Youth) [0.60, 0.30]
component Gender Clinic Capacity (Tavistock GIDS etc.) [0.52, 0.48]
component Puberty Blocker Protocol [0.48, 0.28]
component Cross-Sex Hormones (Adult) [0.46, 0.55]
component Surgical Interventions (Adult) [0.46, 0.55]
component WPATH Standards of Care [0.44, 0.55]
component DSM-5 Gender Dysphoria Criteria [0.40, 0.65]
component ICD-11 Gender Incongruence [0.38, 0.60]
component Cass Review Interim Report [0.36, 0.22]
component Longitudinal Outcome Evidence (Youth) [0.30, 0.18]

// Baseline defaults (deep, taken-for-granted substrate)
component Traditional Gender Roles [0.30, 0.86]
component Biological Sex Recording (Birth Certificate) [0.28, 0.92]
component Cisnormative Default [0.26, 0.90]
component Heteronormative Default [0.24, 0.88]
component Binary Sex Category (M / F) [0.15, 0.95]

// Dependencies (a depends on b)
Individual Person->Pronoun Disclosure Norms
Individual Person->Trans Identity Claim
Individual Person->Coming-Out Practices
Individual Person->Non-Binary Recognition
Individual Person->Self-ID Claim
Individual Person->Gender-Neutral Facilities Norm
Individual Person->Legal Sex Marker on Documents
Individual Person->Gender-Affirming Care Pathway (Adult)
Individual Person->Gender-Affirming Care Pathway (Youth)

Institution (school / sport / workplace / clinic)->School Curriculum Policy on Gender
Institution (school / sport / workplace / clinic)->Sports Eligibility Policy (NCAA / IOC)
Institution (school / sport / workplace / clinic)->Workplace DEI Policy
Institution (school / sport / workplace / clinic)->Bathroom / Facilities Policy
Institution (school / sport / workplace / clinic)->Healthcare Provider Protocols
Institution (school / sport / workplace / clinic)->Prison Housing Policy
Institution (school / sport / workplace / clinic)->Platform Content Moderation Policy
Institution (school / sport / workplace / clinic)->Journalistic Style Guides (AP / BBC)

Policymaker / Regulator->HB 1557 "Parental Rights in Education" (FL)
Policymaker / Regulator->Scotland GRR Bill (self-ID)
Policymaker / Regulator->US Equality Act (stalled)
Policymaker / Regulator->Equality Act 2010 / Anti-Discrimination Statutes
Policymaker / Regulator->Title IX Interpretation (US)
Policymaker / Regulator->Gender Recognition Certificate (UK GRA 2004)
Policymaker / Regulator->Marriage Equality Law
Policymaker / Regulator->Belief Protection (Forstater precedent)

// Identity claims rest on recognition norms and default substrate
Trans Identity Claim->Self-ID Claim
Trans Identity Claim->Gender-Affirming Care Pathway (Adult)
Non-Binary Recognition->Self-ID Claim
Self-ID Claim->Scotland GRR Bill (self-ID)
Pronoun Disclosure Norms->Social-Media Discourse Norms
Coming-Out Practices->Trans Rights Advocacy
Gender-Neutral Facilities Norm->Bathroom / Facilities Policy

// Advocacy rests on substrates; discourse and journalism reflect advocacy
Trans Rights Advocacy->Equality Act 2010 / Anti-Discrimination Statutes
Gender-Critical Advocacy->Belief Protection (Forstater precedent)
Parental-Rights Movement->Traditional Gender Roles
Religious-Conservative Advocacy->Traditional Gender Roles
Religious-Conservative Advocacy->Heteronormative Default
Detransitioner Voices->Cass Review Interim Report
Detransitioner Voices->Longitudinal Outcome Evidence (Youth)

// Institutional policy rests on legal + clinical foundations
School Curriculum Policy on Gender->Equality Act 2010 / Anti-Discrimination Statutes
School Curriculum Policy on Gender->Title IX Interpretation (US)
School Curriculum Policy on Gender->HB 1557 "Parental Rights in Education" (FL)
Sports Eligibility Policy (NCAA / IOC)->Title IX Interpretation (US)
Sports Eligibility Policy (NCAA / IOC)->Binary Sex Category (M / F)
Workplace DEI Policy->Equality Act 2010 / Anti-Discrimination Statutes
Workplace DEI Policy->Belief Protection (Forstater precedent)
Bathroom / Facilities Policy->Binary Sex Category (M / F)
Bathroom / Facilities Policy->Title IX Interpretation (US)
Healthcare Provider Protocols->WPATH Standards of Care
Healthcare Provider Protocols->Gender Clinic Capacity (Tavistock GIDS etc.)
Prison Housing Policy->Binary Sex Category (M / F)
Prison Housing Policy->Legal Sex Marker on Documents

// Media / platform — moderation and newsroom practices anchor into advocacy & norms below
Social-Media Discourse Norms->Platform Content Moderation Policy
Social-Media Discourse Norms->Trans Rights Advocacy
Social-Media Discourse Norms->Gender-Critical Advocacy
Newsroom Balance Conventions->Journalistic Style Guides (AP / BBC)
Newsroom Balance Conventions->Trans Rights Advocacy
Newsroom Balance Conventions->Gender-Critical Advocacy

// Legal depends on deeper legal + defaults
Legal Sex Marker on Documents->Biological Sex Recording (Birth Certificate)
Gender Recognition Certificate (UK GRA 2004)->DSM-5 Gender Dysphoria Criteria
Gender Recognition Certificate (UK GRA 2004)->Legal Sex Marker on Documents
Scotland GRR Bill (self-ID)->Gender Recognition Certificate (UK GRA 2004)
Title IX Interpretation (US)->Binary Sex Category (M / F)
Equality Act 2010 / Anti-Discrimination Statutes->Binary Sex Category (M / F)
Marriage Equality Law->Heteronormative Default
Belief Protection (Forstater precedent)->Equality Act 2010 / Anti-Discrimination Statutes
HB 1557 "Parental Rights in Education" (FL)->Parental-Rights Movement

// Clinical chain
Gender-Affirming Care Pathway (Adult)->Cross-Sex Hormones (Adult)
Gender-Affirming Care Pathway (Adult)->Surgical Interventions (Adult)
Gender-Affirming Care Pathway (Adult)->WPATH Standards of Care
Gender-Affirming Care Pathway (Adult)->Gender Clinic Capacity (Tavistock GIDS etc.)
Gender-Affirming Care Pathway (Youth)->Puberty Blocker Protocol
Gender-Affirming Care Pathway (Youth)->WPATH Standards of Care
Gender-Affirming Care Pathway (Youth)->Gender Clinic Capacity (Tavistock GIDS etc.)
Gender-Affirming Care Pathway (Youth)->Cass Review Interim Report
Puberty Blocker Protocol->Longitudinal Outcome Evidence (Youth)
Puberty Blocker Protocol->WPATH Standards of Care
Cross-Sex Hormones (Adult)->WPATH Standards of Care
Surgical Interventions (Adult)->WPATH Standards of Care
WPATH Standards of Care->DSM-5 Gender Dysphoria Criteria
WPATH Standards of Care->ICD-11 Gender Incongruence
DSM-5 Gender Dysphoria Criteria->Binary Sex Category (M / F)
ICD-11 Gender Incongruence->Binary Sex Category (M / F)
Cass Review Interim Report->Longitudinal Outcome Evidence (Youth)

// Defaults sit on defaults
Cisnormative Default->Binary Sex Category (M / F)
Heteronormative Default->Binary Sex Category (M / F)
Traditional Gender Roles->Heteronormative Default
Traditional Gender Roles->Cisnormative Default
Biological Sex Recording (Birth Certificate)->Binary Sex Category (M / F)

evolve Scotland GRR Bill (self-ID) 0.45
evolve Sports Eligibility Policy (NCAA / IOC) 0.55
evolve Gender-Affirming Care Pathway (Youth) 0.45
evolve Non-Binary Recognition 0.40

note Genesis: contested / novel [0.80, 0.12]
note Commodity: taken-for-granted defaults [0.18, 0.97]
```
