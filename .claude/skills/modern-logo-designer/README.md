# Modern Logo Designer Skill for Claude Code

**Complete knowledge base and workflow for generating professional, modern logo designs in SVG according to 2024-2026 standards.**

---

## What's Inside

This skill directory contains comprehensive reference materials derived from research into 80+ authoritative sources on logo design, color psychology, typography, and SVG/favicon technical specifications.

### Files

1. **SKILL.md** — Trigger instructions, workflow, core principles, outputs format
   - How to invoke the skill (`/modern-logo`)
   - 15-criteria evaluation checklist
   - Quality gates before delivery
   - Design and technical workflow

2. **DESIGN_PRINCIPLES.md** — The 5 core principles + current trends
   - Simplicity, Versatility, Memorability, Timelessness, Scalability
   - Logo types (wordmark, mark, combination, emblem, etc.)
   - 2024-2026 trends (minimalism+warmth, custom typography, negative space, monochrome)
   - Design process workflow

3. **COLOR_REFERENCE.md** — Color psychology and accessibility
   - Psychology of 8 primary colors (blue, red, green, yellow, purple, orange, black/white, neutral)
   - 2026 color trends (Cloud Dancer, earthy sustainability, cosmic gradients, monochrome dominance)
   - Contrast ratios and WCAG accessibility (3:1, 4.5:1 standards)
   - Color blind testing (Protanopia, Deuteranopia, Tritanopia)
   - Color pairing strategies (monochromatic, analogous, complementary, triadic)
   - Practical color selection workflow

4. **TYPOGRAPHY_GUIDE.md** — Font pairing and typographic design
   - Font pairing principles (harmonic, contrasting, display+body, geometric+organic)
   - 2024-2026 typography trends (custom lettering, bold serifs, geometric sans dominance)
   - Font family tiers (Google Fonts, foundry licenses, custom)
   - Industry-specific font recommendations
   - Accessibility in typography
   - Font pairing workflow for skill integration

5. **SVG_TECHNICAL.md** — Technical specifications for SVG and favicon
   - Why SVG (scalability, size, dark mode compatibility)
   - SVG structure and anatomy (viewBox, stroke width, optimization)
   - Favicon strategy (16px to 512px, manifest.json, implementation)
   - SVG optimization with SVGO
   - Accessibility in SVG (title, desc, role, aria-label)
   - Color variants and theming
   - Testing and quality gates

6. **QUALITY_CHECKLIST.md** — 15-point evaluation framework
   - Simplicity (≤3 elements)
   - Monochrome test
   - Scalability (16px to 4000px)
   - Background agnostic
   - Contrast ratio (WCAG AA 3:1+)
   - Color blind safe (all three types)
   - SVG optimized (<5 KB)
   - Typography (if wordmark)
   - Negative space (intentional)
   - Grid foundation
   - Motion-ready
   - File formats (SVG, PNG, favicon set)
   - Favicon viability (16×16px)
   - Consistency (across scales/formats)
   - Future-proof (not trend-dependent)

7. **README.md** (this file) — Overview and quick-start guide

---

## How to Use This Skill

### Invoke the Skill
```
/modern-logo
Brand: [Brand Name or Description]
Industry: [Industry/Category]
Tone: [Professional/Playful/Luxurious/etc.]
Audience: [B2B/B2C/Enterprise/Consumer/etc.]
```

### What the Skill Generates
1. **5 Parallel Concepts** — Each explores different strategic direction
   - Concept 1: Wordmark (typography-focused)
   - Concept 2: Abstract Mark (geometric symbol)
   - Concept 3: Combination (mark + wordmark)
   - Concept 4: Lettermark (monogram/initials)
   - Concept 5: Alternative style (minimalist vs. detailed contrast)

2. **Per Concept**:
   - SVG code (production-ready)
   - Design rationale (which principles applied)
   - Color psychology explanation
   - Font pairing (if wordmark)
   - Favicon viability assessment
   - 15-point checklist evaluation

3. **Refinement**:
   - Pick preferred concept(s)
   - Request specific iterations ("Warmer," "More minimal," "Add negative space")
   - Generate favicon set (16–512px variants)
   - Export to multiple formats

### Quality Assurance
All concepts are evaluated against the **15-Point Quality Checklist** before delivery:
1. Simplicity (≤3 elements)
2. Monochrome legible
3. Scalable (16–4000px)
4. Background agnostic
5. Contrast ≥3:1 (WCAG AA)
6. Color blind safe
7. SVG optimized (<5 KB)
8. Typography intentional
9. Negative space meaningful
10. Grid-based foundation
11. Motion-ready
12. File formats ready
13. Favicon viable
14. Consistent across contexts
15. Future-proof (timeless)

---

## Key Principles Applied

### The 5 Core Principles (Timeless)
1. **Simplicity**: Minimum visual information; instant recognition
2. **Versatility**: Works on favicon to billboard, color to monochrome
3. **Memorability**: Clever negative space, hidden symbols, unique forms
4. **Timelessness**: No trendy elements; flexible for 10+ years
5. **Scalability**: Vector-first (SVG); perfect at any size

### 2024-2026 Trends Acknowledged
- **Minimalism + Warmth**: Away from sterile minimalism; soft curves, breathing room
- **Custom Typography**: Proprietary lettering, bold serifs, geometric sans dominance
- **Negative Space as Storyteller**: Hidden symbols, layered narratives
- **Monochrome Dominance** (51% of new logos): Single-color for dark mode + simplicity
- **Adaptive & Motion Logos**: Dynamic, responsive design
- **Color Psychology**: Cloud Dancer (Pantone 2026 CoY), earthy sustainability, cosmic gradients

### Technical Standards Applied
- **SVG Master File**: Optimized (<5 KB), semantic HTML, accessible
- **Favicon Strategy**: 16, 32, 48, 180, 192, 512px variants
- **Accessibility**: WCAG AA contrast (3:1+), color blind safe, semantic markup
- **Dark Mode**: Monochrome variants, CSS-driven theming

---

## Quick Reference: Design Decisions

### When to Choose Each Logo Type
- **Wordmark**: New brands, short names, tech companies (invest in custom typography)
- **Pictorial Mark**: Established brands only; takes years to become recognizable
- **Abstract Mark**: Tech, finance, contemporary brands (geometric, flexible, unique)
- **Combination Mark**: Safest bet; provides context + icon (most Fortune 500)
- **Lettermark**: Long names, corporate identities, luxury brands
- **Emblem**: Heritage, premium brands willing to look traditional

### Color Selection Quick Reference
| Psychology | Use Cases | Trending Colors |
|-----------|-----------|-----------------|
| Trust | Financial, tech, enterprise | Navy, teal, deep blue |
| Energy | Retail, food, entertainment | Red, coral, warm orange |
| Growth | Sustainability, wellness, health | Sage green, terracotta |
| Premium | Luxury, fashion, heritage | Bold serifs, gold accents |
| Contemporary | Startups, creative, tech | Monochrome + bold accent |

### Font Pairing Quick Tips
- **Harmonic** (same family, different weights): Modern, cohesive (Montserrat Bold + Montserrat Light)
- **Contrasting** (serif + sans): Tradition + innovation (Playfair Display + Inter)
- **Geometric + Organic**: Precise + human (Montserrat + Poppins)
- **Default for 2026**: Google Fonts (Poppins, Inter, Montserrat) — free, professional, licensed

---

## Example Usage

### Invoke
```
/modern-logo
Brand: TechStart AI
Industry: Artificial Intelligence / SaaS
Tone: Innovative, trustworthy, modern
Audience: Enterprise (B2B)
```

### Expected Output
1. **5 Concepts** in SVG
   - Wordmark in clean sans-serif
   - Abstract geometric mark (circuit pattern)
   - Combination (mark + company name)
   - Lettermark (T, S, or TS)
   - Alternative (minimalist variant)

2. **Per Concept**:
   - SVG code
   - Design rationale ("Geometric mark conveys precision; sans-serif = modern trust")
   - Color choice ("Navy #0B2D4D for enterprise trust + tech credibility; 8.2:1 contrast")
   - Font pairing ("Montserrat Bold + Inter = contemporary geometric harmony")
   - Checklist result ("14/15 ✅ — excellent, one minor note on negative space")

3. **Refinement**:
   - User picks Concept 2 (abstract mark) and Concept 3 (combination)
   - Requests: "Make it warmer; less perfect geometry"
   - Skill regenerates with rounded edges, softer curves, warm blue tint
   - Generates favicon set (6 sizes, PNG + ICO format)
   - Exports: SVG master, SVG optimized, PNGs, monochrome variant

---

## Technical Specifications

### Deliverables Format

#### SVG (Master & Optimized)
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="Brand Name Logo">
  <title>Brand Name Logo</title>
  <desc>Logo description</desc>
  <!-- Logo shapes -->
</svg>
```

#### File Sizes
- SVG Master: 2–5 KB (typical)
- SVG Optimized (SVGO): 1–3 KB
- PNG (each size): 1–50 KB depending on complexity

#### Favicon Sizes
- 16×16px (browser tab)
- 32×32px (taskbar)
- 48×48px (Windows desktop)
- 180×180px (Apple Touch Icon)
- 192×192px (Android Chrome)
- 512×512px (PWA manifest)

---

## Integration with Claude Code

### How to Activate
1. Save this folder to `~/.claude/skills/modern-logo-designer/`
2. Restart Claude Code CLI
3. Type `/modern-logo` in prompt to invoke

### Model Recommendation
- **Initial Ideation**: Claude Opus 4.6 (for quality concept generation)
- **Refinements**: Can use Haiku 4.5 for faster iterations
- **Evaluations**: Opus 4.6 for final checklist assessments

---

## Knowledge Sources

This skill is based on research from 80+ authoritative sources:

**Design Institutions & Publications**:
- Smashing Magazine, Logo Design Love, Brand New, AIGA Eye on Design, Print Magazine, Design Observer

**Design Platforms**:
- Dribbble, Behance, LogoLounge, Designmodo, Looka, 99designs

**Technical Standards**:
- web.dev, MDN Web Docs, W3C SVG Specification, WebAIM, The A11Y Collective

**Color & Typography**:
- Pantone Insights, Adobe Design, Monotype, Creative Bloq, Typewolf, Contrast Foundry

**Case Studies & Trends**:
- Logo Design Love (archives), Brand New (redesigns), Kittl, Wix Design, Status Labs, WGSN

---

## Skill Limitations & Next Steps

### What This Skill Does
- ✅ Generate 5 distinct logo concepts
- ✅ Evaluate against 15 quality criteria
- ✅ Explain design rationale (principles, color psychology, trends)
- ✅ Suggest refinements
- ✅ Provide SVG code + optimization guidance
- ✅ Assess favicon viability

### What This Skill Doesn't Do (Yet)
- ❌ Automated favicon generation (guidance provided; manual export required for now)
- ❌ Branded asset system (brand guidelines extraction — can be added)
- ❌ Competitor analysis (brief research — can be added)
- ❌ Multi-language logo adaptation (scope for future)

### Future Enhancements
- Favicon set auto-generation (PNG batch export)
- Brand style guide extraction (fonts, colors, usage rules)
- Competitive landscape analysis (identify white space)
- Animation suggestions (if logo structure supports motion)
- A/B testing framework (multiple options for user testing)

---

## Version

**Modern Logo Designer Skill v1.0**
- Released: April 2026
- Knowledge Base: 80+ sources, 2024-2026 trends
- Quality Framework: 15-point checklist
- SVG/Favicon Spec: 2026 standards (web.dev, W3C)

---

## Quick Troubleshooting

**Q: Logo is too complex; failing simplicity check**
A: Reduce to ≤3 primary elements. Remove decorative details. Test monochrome version.

**Q: Monochrome version loses meaning**
A: Revisit color psychology choice. Ensure distinction via shape, not color alone. Test with color-blind simulator.

**Q: SVG file too large (>5 KB)**
A: Run SVGO optimization. Check for embedded metadata. Simplify paths. Remove unnecessary groups.

**Q: Logo doesn't render at 16px favicon size**
A: Simplify further. Use solid shapes, no thin strokes. Test at actual 16px in browser.

**Q: Font pairing feels generic**
A: Consider custom lettering or bolder serif/sans contrast. Check 2026 trends alignment.

**Q: Colors don't work for color-blind users**
A: Use contrast (light/dark) in addition to hue. Test in Coblis or Color Oracle simulator.

---

## Feedback & Iteration

This skill is designed to evolve. Feedback on logo concepts should reference:
- Which checkpoint is failing (use QUALITY_CHECKLIST.md)
- Specific direction ("Warmer," "More geometric," "Less trendy")
- Brand context changes

Example refinement request:
```
/modern-logo [refine]
Concept: 2 (Abstract Mark)
Request: Make it warmer; add subtle curve to geometric shape; test for dark mode
Feedback: Too corporate; needs personality
```

---

## Contact & Attribution

**Knowledge Base Compiled**: Research into 80+ design authorities, technical standards (web.dev, W3C), and contemporary trends (Pantone, WGSN, Dribbble).

**Skill Framework**: Claude Code integration; designed for rapid logo ideation and quality assurance.

**License**: MIT (examples in this skill are reference implementations; actual output is user-owned)

---

## Next Steps

1. **Invoke the skill**: `/modern-logo` + brand brief
2. **Review 5 concepts**: Against 15-point checklist
3. **Select & refine**: Pick preferred direction(s); request iterations
4. **Finalize**: Export SVG master, PNG variants, favicon set
5. **Document**: Create brand guideline extract (fonts, colors, usage rules)

Happy designing! 🎨
