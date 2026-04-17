# Wardley Map: Small Tea Shop

## Scenario

A small tea shop business that serves cups of tea to customers, handles payment, and sources tea leaves from suppliers.

## User Need

- **Customer**: Wants to buy and drink a cup of tea in a pleasant setting.

## Value Chain (Components)

From most visible (user-facing) to least visible (infrastructure):

| # | Component | Visibility (Y) | Evolution (X) | Stage |
|---|-----------|---------------|---------------|-------|
| 1 | Customer (User) | 1.00 | 0.95 | Commodity |
| 2 | Cup of Tea (served) | 0.90 | 0.75 | Product |
| 3 | Shop Experience / Ambience | 0.88 | 0.55 | Product |
| 4 | Payment (transaction) | 0.85 | 0.90 | Commodity |
| 5 | Tea Brewing (process) | 0.70 | 0.70 | Product |
| 6 | Staff / Barista Skill | 0.68 | 0.55 | Product |
| 7 | Cups & Crockery | 0.60 | 0.92 | Commodity |
| 8 | Payment Terminal (card reader / POS) | 0.55 | 0.85 | Commodity |
| 9 | Hot Water | 0.55 | 0.98 | Commodity |
| 10 | Tea Leaves (inventory) | 0.50 | 0.78 | Commodity |
| 11 | Supplier Relationship | 0.35 | 0.65 | Product |
| 12 | Shop Premises (rent) | 0.30 | 0.95 | Commodity |
| 13 | Electricity / Utilities | 0.15 | 0.99 | Commodity |
| 14 | Water Supply | 0.12 | 0.99 | Commodity |

## Dependency Graph (Edges)

Using the convention $(a, b) \in E$ means "a depends on b":

```
Customer --> Cup of Tea
Customer --> Shop Experience
Customer --> Payment

Cup of Tea --> Tea Brewing
Cup of Tea --> Cups & Crockery
Cup of Tea --> Hot Water

Tea Brewing --> Tea Leaves
Tea Brewing --> Hot Water
Tea Brewing --> Staff / Barista Skill

Payment --> Payment Terminal

Shop Experience --> Shop Premises
Shop Experience --> Staff / Barista Skill

Tea Leaves --> Supplier Relationship

Hot Water --> Water Supply
Hot Water --> Electricity

Payment Terminal --> Electricity
Shop Premises --> Electricity
```

## ASCII Wardley Map

```
Visibility
  ^
  |   Genesis       Custom-Built     Product           Commodity
  |   [0-0.25)      [0.25-0.5)       [0.5-0.75)        [0.75-1.0]
1.0 +----------------------------------------------------------------+
  |                                                    * Customer   |
  |                                                                  |
0.9 +                                    * Cup of Tea                |
  |                                * Shop Experience                 |
  |                                                    * Payment     |
0.8 +                                                                |
  |                                * Tea Brewing                     |
0.7 +                              * Staff/Barista                   |
  |                                                                  |
0.6 +                                                  * Cups/Crockery|
  |                                                                  |
0.5 +                                   * POS Terminal               |
  |                                                    * Hot Water   |
  |                                                    * Tea Leaves  |
0.4 +                                                                |
  |                          * Supplier Relationship                 |
0.3 +                                                   * Premises   |
  |                                                                  |
0.2 +                                                                |
  |                                                    * Electricity |
0.1 +                                                    * Water     |
  |                                                                  |
0.0 +----------------------------------------------------------------+
       0.0       0.25         0.5          0.75           1.0
                         Evolution (X) ->
```

## Formal Model

Following the tuple definition $\mathcal{M} = (V, E, \nu, \varepsilon, t)$:

- **V** = {Customer, CupOfTea, ShopExperience, Payment, TeaBrewing, Staff, Cups, POSTerminal, HotWater, TeaLeaves, SupplierRelationship, Premises, Electricity, Water}
- **E** = directed edges listed above (a depends on b)
- **$\nu(v)$** = visibility values in the table (1 = user, decreasing with graph distance)
- **$\varepsilon(v)$** = evolution score in the table, mapped to stages:
  - Genesis $[0, 0.25)$
  - Custom-Built $[0.25, 0.5)$
  - Product $[0.5, 0.75)$
  - Commodity $[0.75, 1.0]$
- **t** = snapshot, today (2026-04-17)

## Strategic Observations

1. **Commodity components** (Hot Water, Electricity, Water, Cups, Premises, Payment Terminal) should be outsourced or purchased off-the-shelf at lowest cost. No strategic advantage in building these in-house.

2. **Product-stage components** (Tea Brewing, Cup of Tea, Shop Experience, Staff Skill, Supplier Relationship) are where differentiation happens. These are worth investing in to distinguish the shop from competitors.

3. **Supplier Relationship** is the lowest-visibility component that still offers differentiation. Direct/ethical sourcing, rare teas, or exclusive supplier partnerships can move this leftward toward Custom-Built and create defensible value.

4. **Payment** has evolved to a commodity - using standard card readers (e.g., SumUp, Square, Stripe Terminal) is correct. No reason to build bespoke payment infrastructure.

5. **Evolution pressure**: Tea Leaves drift toward commodity; premium sourcing (single-estate, organic, fair-trade) pulls them back toward Product to preserve margin.

## Gameplay Suggestions

- **Standardise** commodity inputs (use wholesale suppliers for cups, standard POS).
- **Differentiate** on Shop Experience and Barista Skill (training, ambience, loyalty).
- **Build alliances** with specialty tea suppliers to secure unique leaves.
- **Measure** cup-of-tea unit economics: $\text{margin} = \text{price} - (c_{\text{leaves}} + c_{\text{water}} + c_{\text{energy}} + c_{\text{labour}} + c_{\text{overhead}})$.
