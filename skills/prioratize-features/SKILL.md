---
name: prioratize-features
description: Analyze an explicitly supplied requirements backlog or individual features for fixed-price delivery. Clarify ambiguities, preserve contractual coverage, find simpler scope, and prioritize features using qualitative evidence-based judgments. Use for backlog prioritization, feature scope reviews, overengineering detection, and minimum contract-compliant solution assessments.
---

# Prioratize Features

## Objective

Recommend the simplest defensible implementation of each feature while preserving all documented contractual obligations, then recommend a feasible delivery order. Optimize scope and complexity, **not estimated costs**.

## Non-negotiable boundaries

1. **Strict input isolation.** Use only materials explicitly supplied or designated by the user for the current analysis and clarifications the user gives during this run. Do not use prior conversation history, memory, unrelated workspace files, connected repositories, browsing, or general project knowledge as evidence. Do not autonomously retrieve additional sources. If a tool automatically supplies unrelated context, disregard it.
2. Distinguish **source facts**, **user clarifications**, **reasoned inferences**, and **unknowns**. A plausible interpretation is not a contractual fact. Never invent requirements, acceptance criteria, business values, technical constraints, dependencies, or estimates.
3. **Preserve contractual coverage.** Never recommend dropping an obligation as though it were optional. Do not treat a lower-ranked mandatory requirement as removable. Do not interpret silence in a contract as approval of an implementation choice.
4. Source every material finding with a document name plus stable requirement ID, section, row, or exact supplied excerpt. If source identifiers are absent, assign analysis-only references and clearly label them as such.
5. Do not calculate person-days, monetary savings, development cost, or numerical scoring. Do not assert that a simplification saves effort without technical confirmation. Flag complexity and implementation uncertainty for expert review.
6. Do not modify source documents, backlog items, or contracts. Do not declare contractual acceptance, scope changes, or feature removal approved. Present recommendations for human decision.

## Inputs

Accept any explicitly provided subset of: contract or statement of work, requirements/Lastenheft, backlog, user stories, acceptance criteria, business objectives, process descriptions, architecture/integration constraints, approved decisions, and change requests. Ask the user to identify the authoritative source when sources conflict. Do not assume document authority from its filename.

If no usable materials are supplied, ask for them. Explain that business priority cannot be reliably assessed without explicit goals or stakeholder priorities, and implementation feasibility cannot be confirmed without technical evidence.

## Workflow

### 1. Establish analysis boundary

- List the supplied sources, their identifiers, and any user-declared authority or version.
- Confirm whether the user requests **backlog-wide**, **single-feature**, or **both** analysis. For both, analyze backlog relationships first, then high-impact individual features.
- Identify explicitly documented contractual obligations separately from proposed solutions and optional requests.
- Build traceability from each requirement to proposed feature(s). Avoid silently consolidating requirements that have distinct acceptance obligations.

### 2. Interactive clarification gate

- Identify contradictions, missing acceptance boundaries, undefined terms, unclear obligations, unknown business goals, and dependencies that could change scope or ordering.
- Ask **up to five related questions per batch**, ordered by impact on contractual coverage and scope decisions. Make questions specific and cite the relevant source. Where helpful, offer concrete alternatives without implying any is confirmed.
- Wait for answers and reassess. Record the user's answers as **clarifications**, not amendments to the contract. Repeat batches if material uncertainties remain.
- If the user cannot answer or elects to proceed, continue only where safe; mark affected conclusions **Unclear / Decision pending**, explain limitations, and avoid definitive scope-reduction recommendations.
- Do not block unrelated, evidence-supported analysis because another feature remains unclear.

### 3. Backlog-wide analysis

- Map obligations to features and inspect duplicate coverage, overlap, conflicting wording, dependencies, integration touchpoints, sequencing constraints, and possible consolidation.
- Separate **contractually required outcomes** from a particular design or technical approach, unless the latter is contractually specified.
- Flag possible scope expansion, redundant functionality, unnecessary configurability, and unsupported assumptions.
- Recommend ordering based on **documented business value**, **documented dependencies**, and **documented risk**. If one factor lacks evidence, label it **Unknown** instead of assigning a fictional ranking. Distinguish delivery sequence from contractual inclusion.
- Suggest manageable vertical slices where supported; do not imply that partial slices fulfill the complete contract.

### 4. Individual-feature optimization

For each selected feature:

1. State its required outcome and cite the source.
2. Identify required behaviors, constraints, acceptance conditions, and any gaps.
3. Label proposed elements as:
   - **Contractually required** — supported by authoritative input.
   - **Implementation necessity** — plausibly essential but requires technical confirmation unless documented.
   - **Optional enhancement** — not evidenced as required; do not presume it can be omitted if contract wording is unclear.
   - **Ambiguous** — cannot classify without clarification.
4. Challenge additional workflows, screens, settings, roles, edge-case handling, generalization, and infrastructure **only if they appear in the supplied material**. Never assume their presence.
5. Recommend the **minimum evidenced scope**, preserving required behavior and non-functional obligations. Present alternative designs as **proposals**, never established feasibility.
6. Explicitly state what cannot be simplified, what needs stakeholder approval, and what needs technical verification.

### 5. Qualitative assessment

Use these scales, with short evidence-based justification:

| Criterion | Allowed ratings | Meaning |
| --- | --- | --- |
| Contractual coverage | Covered / Partially covered / Not covered / Unclear | Traceable satisfaction of supplied obligations; this is not a legal determination |
| Complexity | Low / Medium / High / Unknown | Complexity evidenced by proposed behavior, integrations, variants, and constraints |
| Overengineering risk | Low / Medium / High / Unknown | Evidence of unnecessary solution breadth relative to stated outcomes |
| Simplification potential | Low / Medium / High / Unknown | Extent of defensible simplification opportunities, pending validation |
| Business priority | High / Medium / Low / Unknown | Relative importance based only on supplied business evidence |
| Dependency criticality | High / Medium / Low / Unknown | Extent to which this feature enables or blocks other work |

Do not average ratings or convert them to points. Explain significant disagreements between criteria (e.g., low business priority but high dependency criticality). If ranking evidence is incomplete, recommend a **provisional order** or group features as **not rankable from supplied evidence**.

## Output contract

Keep reports concise and decision-oriented. Use the following sections, adapting the number of rows to the supplied material:

1. **Evidence and limitations:** supplied sources, authority conflicts, unresolved gaps.
2. **Clarification questions:** at most five per round, before conclusions that depend on answers.
3. **Backlog assessment:** feature/requirement IDs, contractual status, business priority, dependency criticality, recommended sequence, reasons and citations.
4. **Scope opportunities:** feature ID, evidenced complexity, simplification proposal, contractual coverage impact, validation required, citation.
5. **Feature deep dives:** contractual outcome, current proposed scope, minimum evidenced scope, qualitative ratings, assumptions/unknowns, risks, and approval points.
6. **Decision log:** recommendations for **Keep / Simplify (pending validation) / Clarify / Consider change control**, with owner or approver listed only if supplied; otherwise **Owner unknown**.

Always distinguish **finding** from **recommendation**. Use conditional language when evidence is incomplete. Cite each finding beside the relevant row or statement, not only in an appendix.

## Safety checks before finalizing

- Can every contractual requirement still be traced to a proposed deliverable?
- Does any recommendation rely on outside context, remembered details, or an invented assumption? If yes, remove or relabel it.
- Is a mandatory requirement being deprioritized in sequence rather than implicitly excluded?
- Is an alternative described as feasible or cheaper without supplied technical evidence? If yes, mark it for validation.
- Are important missing facts explicitly marked Unknown, with targeted next decisions?

## Example invocation

"Use prioratize-features on only the attached requirements.xlsx and signed-scope.pdf. Start with backlog analysis, ask up to five clarification questions at a time, then recommend contract-compliant simplifications and a provisional feature order. Do not use previous conversations or external information."
