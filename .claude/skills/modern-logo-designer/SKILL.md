# Modern Logo Designer Skill

**Trigger**: `/modern-logo` or `/logo-design`

**Purpose**: Generate high-quality, modern logo concepts in SVG format according to contemporary design standards and best practices (2024-2026).

**Scope**: This skill specializes in creating professionally viable logo concepts for any brand/project. It combines design principles with technical requirements for web, favicon, and print-ready assets.

---

## How to Use

1. **Provide Brief**: Describe brand, industry, tone, target audience
   ```
   /modern-logo
   Brand: TechStart AI
   Industry: AI/Machine Learning
   Tone: Innovative, trustworthy, modern
   Audience: B2B, enterprise
   ```

2. **Skill Will Generate**:
   - 5 distinct SVG logo concepts (parallel ideation)
   - Each with design rationale explaining principles applied
   - Technical specs (SVG, monochrome test, favicon viability)
   - Font pairing recommendations if wordmark component exists

3. **Refinement Loop**:
   - Pick preferred concept
   - Request iterations: "Warmer, less geometric" or "More minimal"
   - Generate favicon set (16, 32, 48, 180, 192, 512px)
   - Export to multiple formats (SVG master, PNG, CSS)

---

## Core Principles Applied

The skill evaluates all designs against these 15 criteria:

### Design Principles (from Modern Logo Designer Reference)
1. **Simplicity**: ≤3 primary visual elements, instantly recognizable
2. **Versatility**: Functions on 16px favicon to 4000px billboard
3. **Memorability**: Uses negative space, hidden symbols, or unique forms
4. **Timelessness**: No trendy elements, flexible for 10+ year evolution
5. **Scalability**: Vector-perfect at all sizes, no stroke issues

### Technical Requirements
6. **Monochrome Viability**: Legible in black/white without color
7. **WCAG Contrast**: 3:1 minimum for graphical elements
8. **Color Blind Safe**: Pass Protanopia, Deuteranopia, Tritanopia tests
9. **SVG Optimized**: Clean code, minimal paths, proper stroke widths
10. **Favicon Ready**: Works at 16×16px with clarity

### Modern Trends 2024-2026
11. **Trend Awareness**: Minimal+warmth, custom typography, negative space, adaptive design
12. **Color Psychology**: Uses research-backed colors (Pantone 2026 awareness)
13. **Typography**: Font pairings follow harmonic/contrast rules if wordmark
14. **Negative Space**: Intentional use, not overcrowded

### Deliverables
15. **Production Ready**: SVG master with semantic HTML, bounding box optimized, ready for favicon generation

---

## Skill Workflow

```
User Brief
    ↓
Brief Analysis (industry, tone, competitive landscape context)
    ↓
5 Parallel Concepts (5 subagents, each generates 1-2 SVG concepts)
    ├─ Concept 1: Wordmark (typography-focused)
    ├─ Concept 2: Abstract Mark (geometric, symbol)
    ├─ Concept 3: Combination (mark + wordmark)
    ├─ Concept 4: Lettermark/Monogram (if applicable)
    └─ Concept 5: Alternative style (minimal vs. detailed contrast)
    ↓
Evaluation: Checklist against 15 criteria
    ↓
Deliverables: SVG code, design rationale, favicon viability assessment
    ↓
User Selects → Refinement Loop (iterations)
    ↓
Favicon Set Generation (16, 32, 48, 180, 192, 512px variants)
    ↓
Export Package: SVG master, PNG, favicon.ico, manifest.json
```

---

## Design Checklist (Used by Skill)

For each concept, verify:
- [ ] Simplicity: ≤3 main elements, recognizable at any size
- [ ] Monochrome test: Looks good in black on white
- [ ] Scalability: Tested mentally at 16px and 4000px
- [ ] Background agnostic: Works on white, black, color, texture
- [ ] Contrast: 3:1+ for all colors
- [ ] Color blind safe: No red/green reliance alone
- [ ] SVG quality: Clean paths, optimized, semantic
- [ ] Typography (if used): Font pairing is harmonic, readable
- [ ] Negative space: Intentional, not accidental gaps
- [ ] Grid foundation: Built on Golden Ratio or clear geometry
- [ ] Motion-ready: Can support subtle CSS animations
- [ ] File-agnostic: Can export to SVG, PNG, WEBP, ICO
- [ ] Favicon viable: Legible at 16×16px
- [ ] Consistency: Maintains integrity across scales
- [ ] Future-proof: Not reliant on 2025-2026 trends, timeless

---

## Color Theory Quick Reference

**Psychology Anchor** (for design rationale):
- Blue: Trust, professionalism (33% of top brands)
- Red: Energy, urgency, action
- Green: Growth, nature, health
- Yellow: Optimism, accessibility
- Black/White: Contrast, modern elegance
- Purple: Creativity, luxury
- Orange: Friendliness, enthusiasm

**2026 Trending**:
- Pantone 2026 Color of the Year: **Cloud Dancer** (white/cream, #F0EEE9)
- Terracotta, Sage Green, Earthy Browns (sustainability)
- Cosmic gradients (iridescent pastels)
- Monochrome dominance (51% of new logos)

**Contrast Rules**:
- WCAG AA minimum: 3:1 for graphical elements, 4.5:1 for text
- Logo exception: Not bound by contrast ratio, but test on multiple backgrounds
- Test workflow: Grayscale conversion = accessibility check

---

## Font Pairing Quick Reference

**Harmonic Pairing** (similar families):
- Montserrat + Montserrat Light (same family, different weights)
- Poppins + Poppins Medium

**Contrasting Pairing** (serif + sans):
- Playfair Display + Inter (elegant + modern)
- EB Garamond + Montserrat (tradition + contemporary)

**Modern Wordmark Fonts**:
- Custom lettering (proprietary — Google Product Sans, Spotify custom)
- Bold Serifs: High contrast, thick strokes
- Geometric Sans: Futura, Montserrat, Poppins
- Display Fonts: Playfair, Roc Grotesk (headline impact)

---

## SVG & Favicon Technical Specs

**SVG Optimization**:
- Stroke width: 2-4px small, 6-12px large
- Remove unnecessary attributes (SVGO tool reference)
- Use `currentColor` for dynamic theming
- Semantic: `<svg role="img" aria-label="Brand Name">`

**Favicon Sizes Required**:
- 16×16px (browser tab)
- 32×32px (taskbar)
- 48×48px (Windows desktop)
- 180×180px (Apple Touch Icon)
- 192×192px (Android Chrome)
- 512×512px (PWA manifest)

**Implementation Template**:
```html
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">
<link rel="apple-touch-icon" href="/apple-touch-icon-180x180.png">
<link rel="manifest" href="/manifest.json">
```

---

## Competitive Research Context

Before generating concepts, skill can:
- Identify competitor logos in same industry
- Note color/style patterns (avoid clichés)
- Define white space opportunity
- Establish tone differentiation (if brief includes competitors)

---

## Quality Gates

**Before Delivering**:
1. ✅ SVG renders cleanly in browser DevTools
2. ✅ Monochrome version is legible (grayscale filter test)
3. ✅ No warnings from SVGO optimization
4. ✅ Design rationale explains which of 5 principles each concept demonstrates
5. ✅ Favicon viability confirmed (mentally testable at 16px)
6. ✅ Color choices backed by psychology + 2026 trends
7. ✅ Typography (if used) justified via pairing principles

---

## Outputs Format

**Per Concept**:
```markdown
### Concept [N]: [Name]

**SVG Code**:
```svg
<svg ...>...</svg>
```

**Design Rationale**:
- Primary principle: [Simplicity/Memorability/etc.]
- Color choice: [Psychology + trend alignment]
- Scalability note: [How it performs at extremes]
- Font pairing (if wordmark): [Font names + why they work together]

**Favicon Viability**: [Assessment of 16×16px legibility]

**Style**: [Minimalist/Geometric/Organic/Retro-Futurism/etc.]
```

---

## Skill Metadata

- **Model Used**: Claude Opus 4.6 (for quality ideation)
- **Fallback for Iterations**: Can use Haiku for refinement loops
- **SVG Generation**: Native Claude SVG generation (no external tools)
- **Research Sources**: 80+ curated sources (Smashing Mag, Brand New, web.dev, Adobe, Dribbble, Behance, etc.)
- **Knowledge Base**: Modern Logo Designer Reference (embedded in skill)
