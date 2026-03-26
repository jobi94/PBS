# SEO Copywriter — Fire Safety Solutions for Buildings
# File: CLAUDE.md
# Project: B2B website for a company specialising in fire safety of buildings
# Workflow: Claude Code + Antigravity — generate sections individually, plain text with inline comments

---

## PROJECT CONTEXT

**Company name:** Požární bezpečnostní řešení staveb
*(English equivalent for UX use: Fire Safety Solutions)*

The company provides comprehensive fire safety services for buildings, targeting B2B clients in the Czech Republic.

**Regions of operation:**
- Královéhradecký Region (Hradec Králové)
- Pardubický Region (Pardubice)
- Středočeský Region (Central Bohemia)
- Prague
- Olomoucký Region (Olomouc)

**Core services:**
- Fire Safety Design Documentation (PBŘ) — for all stages of building permits
- Fire-stopping penetration seals (HILTI, PROMAT, INTUMEX systems and others)
- Fire doors, shutters, roller doors, inspection hatches
- Fire inspections, revisions and regular checks
- Fire protection protocols and documentation (PO)
- Employee fire safety training
- Fire protection and occupational health & safety (BOZP) consulting and audits

**Target audience:**
- Construction companies and general contractors
- Architecture and design studios
- Building managers and facility management companies
- Property developers and investors
- Legal entities obligated under Czech Act No. 133/1985 Coll. (Fire Protection Act)

**Tone of Voice:** Expert, direct, trustworthy. No marketing fluff.
The client knows what they need — they don't need educating, they need to make a decision.

**CTA goal:** Non-binding enquiry / contact

> ⚠️ IMPORTANT: All generated page copy must be written in Czech. The instructions in this file are in English for developer clarity, but every output — headings, body text, CTAs, meta tags — must be in native Czech. Never translate directly. Write as a native Czech copywriter would.

---

## HOW TO GENERATE SECTIONS

Always generate **one section per command**.
Each call must include:

```
SECTION:   [name — see list below]
PAGE:      [homepage / services / about / contact / specific service name]
VARIANT:   [A = default | B = A/B test alternative]
```

If any parameter is missing, ask before generating.

---

## SECTION LIST AND PURPOSE

| Section | Page | Description |
|---|---|---|
| `hero` | homepage, landing page | Main heading + intro + CTA above the fold |
| `intro` | homepage, about | Short company introduction paragraph |
| `services-overview` | homepage | Brief services overview with links to subpages |
| `service-detail` | service subpage | Detailed description of one specific service |
| `why-us` | homepage, about | Reasons to work together — benefit-driven |
| `process` | homepage, services | How the collaboration works — step by step |
| `cta-block` | any | Standalone call-to-action block |
| `faq` | services, landing page | Frequently asked questions — 4–6 items |
| `about` | about | Company presentation, team, background |
| `references` | homepage, about | Social proof — project types, industries, volume |
| `footer-tagline` | footer | Short claim or company descriptor |
| `meta` | any | Meta title + meta description for the given page |

---

## OUTPUT FORMAT RULES

### Format for every section:

```
// ─── SECTION: [NAME] | Page: [name] | Variant: [A/B] ───

// [META] Primary KW: "[kw]" | LSI terms used: "[term1]", "[term2]"
// [TONE] Expert + direct. B2B. No marketing fluff.

[H1 or H2 — depending on section]
// [SEO] KW in heading: yes/no. Length: X characters.

[Lead paragraph or intro sentence]
// [COPY] Lead with benefit. KW in first paragraph: yes/no.

[Section body]
// [UX] Paragraphs max 3–4 lines. Mobile-first.

[CTA text]
// [CTA] Benefit-driven. Avoid "Submit" / "More info".
// [CTA-B] Alternative wording: "[alternative]"

// [INTERNAL LINK] Anchor: "[text]" → recommended target page: [type]
// [COMPONENT] Suggested Antigravity component: [name or description]
// [NOTE] Optional note for the developer or copywriter
```

---

## SEO RULES (always apply)

**Primary keywords by page:**

| Page | Primary KW (Czech) | Secondary KW (Czech) |
|---|---|---|
| Homepage | požární bezpečnost staveb | protipožární ochrana, PBŘ, požární ochrana budov |
| PBŘ / Fire Design | požárně bezpečnostní řešení stavby | PBŘ projektová dokumentace, požární projekt |
| Penetration Seals | protipožární ucpávky prostupů | požární těsnění, ucpávky HILTI, ucpávky PROMAT |
| Fire Doors | požární dveře | protipožární uzávěry, požární rolety, EI dveře |
| Inspections | požární kontrola | revize požární ochrany, požární prohlídka, protokol PO |
| About | požární bezpečnost staveb | autorizovaný technik PO, odborně způsobilá osoba |
| Contact | poptávka požární bezpečnost | nezávazná konzultace, požární specialista |

**Local SEO — apply where relevant:**

The company does not operate nationwide. Use local keyword modifiers naturally — in meta descriptions, H2s, and body text. Never force them into H1.

| Region | Local KW modifiers (Czech) |
|---|---|
| Prague | požární bezpečnost Praha, PBŘ Praha, protipožární ochrana Praha |
| Středočeský | požární bezpečnost Středočeský kraj, PBŘ Středočeský kraj |
| Královéhradecký | požární bezpečnost Hradec Králové, PBŘ Hradec Králové |
| Pardubický | požární bezpečnost Pardubice, protipožární ochrana Pardubice |
| Olomoucký | požární bezpečnost Olomouc, PBŘ Olomouc |

For pages without a specific region (e.g. homepage), use a natural enumeration once in the body text: "Praha, Hradec Králové, Pardubice, Olomouc a Středočeský kraj." Never repeat it.

**Technical SEO rules:**
- Meta title: 50–60 characters, primary KW at the start
- Meta description: 150–160 characters, primary KW + value proposition or CTA
- H1: once per page, contains primary KW naturally
- H2: main sections, at least one contains primary or secondary KW
- KW density: max 1–2%, never forced repetition
- LSI terms to weave in naturally: požární odolnost, pasivní požární ochrana, únikové cesty, požární úsek, zákon o požární ochraně, HZS, BOZP

---

## COPYWRITING RULES (always apply)

- Write "vy / vám / váš" (you / your) — never "my / naše firma / náš tým" (we / our company)
- Lead with benefits: what the client gains, not what the company does
- Use active verbs: "zajistíte soulad" (you ensure compliance), "získáte dokumentaci" (you get documentation) — not passive constructions
- Urgency only where real: legal obligations, building permit deadlines
- Social proof: reference project types — bytové domy, průmyslové haly, kanceláře, zdravotnictví (residential, industrial, office, healthcare)
- Banned phrases: "komplexní řešení", "světová třída", "špičkové služby", "profesionální přístup"
- Technical terminology is fine — the audience knows it: PBŘ, PO, BOZP, EI, HZS

---

## SELF-REVIEW CHECKLIST (run before every output)

- [ ] Primary KW in H1/H2, first paragraph, meta title, meta description
- [ ] KW density between 1–2%
- [ ] No forced or unnatural keyword repetition
- [ ] Paragraphs max 3–4 lines
- [ ] At least one CTA with a Variant B alternative
- [ ] Tone: expert, direct, no fluff
- [ ] Output is in Czech — written natively, not translated
- [ ] Above-the-fold content communicates value proposition without scrolling
- [ ] No corporate jargon or filler phrases
- [ ] Customer perspective — "vy", not "my"

---

## EXAMPLE COMMANDS

```
SECTION: hero
PAGE: homepage
VARIANT: A
```

```
SECTION: service-detail
PAGE: protipožární ucpávky prostupů
VARIANT: A
```

```
SECTION: faq
PAGE: požárně bezpečnostní řešení stavby
VARIANT: A
```

```
SECTION: meta
PAGE: homepage
VARIANT: A
```

---

## ANTIGRAVITY WORKFLOW NOTE

Output is always **plain text with inline comments** — not MDX, not JSON, not JSX.

Recommended workflow:
1. Claude Code generates the section with `//` comments
2. Developer / copywriter reviews comments and edits the text
3. Edited text is inserted into the relevant Antigravity component
4. All comments are removed before publication

Comments always follow the format `// [TAG]` where TAG is one of:
`[SEO]` `[COPY]` `[UX]` `[CTA]` `[CTA-B]` `[INTERNAL LINK]` `[COMPONENT]` `[NOTE]`
