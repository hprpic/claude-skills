# 15-Point Logo Quality Checklist

**Used by Modern Logo Designer Skill to evaluate all generated concepts before delivery.**

This checklist combines the 5 core principles (Simplicity, Versatility, Memorability, Timelessness, Scalability) with technical requirements and modern standards (2024-2026).

---

## Checklist

### 1. Simplicity: ≤3 Primary Visual Elements
**Criterion**: The logo can be recognized and described using 3 or fewer main shapes/elements.

**How to Test**:
- Mentally reduce the logo to its core: "What's the essential shape?"
- Can you describe it in one sentence? (e.g., "Apple logo is a single apple silhouette")
- Are there redundant details that could be removed?

**Pass/Fail**:
- ✅ PASS: 1-3 clear primary elements; instantly recognizable
- ❌ FAIL: 4+ elements; feels busy or overcomplicated

**Why It Matters**: Logos processed in <400ms; simplicity enables instant comprehension

**Example**:
- Nike Swoosh: ✅ (1 element — curved line)
- Mastercard: ✅ (3 elements — two overlapping circles + one circle)
- Complex emblem with 8 details: ❌ (fails simplicity)

---

### 2. Monochrome Test: Legible in Black/White Without Color
**Criterion**: Remove all color (convert to grayscale); logo remains clearly identifiable and doesn't lose critical meaning.

**How to Test**:
- Apply `filter: grayscale(100%)` in CSS or mental conversion
- Does the logo still communicate the brand essence?
- Are shapes distinct, not merged together?

**Pass/Fail**:
- ✅ PASS: Monochrome version maintains full identity; all shapes separate
- ⚠️ WARNING: Monochrome slightly weaker but acceptable; shapes distinct
- ❌ FAIL: Loses meaning in monochrome; shapes merge; illegible

**Why It Matters**: 
- Accessibility (color-blind users)
- Universality (works in situations where color isn't available: fax, print BW, engraving)
- Dark mode compatibility

**Example**:
- Apple: ✅ (silhouette alone is iconic)
- Target: ✅ (concentric circles remain distinct)
- Logo relying entirely on color (red/green distinction): ❌ (fails for color-blind)

---

### 3. Scalability: Legible at 16px (Favicon) and 4000px (Billboard)
**Criterion**: Logo maintains visual integrity at extreme sizes — no detail lost at 16px, no inflation artifacts at 4000px.

**How to Test (Mental)**:
- Imagine the logo at 16×16 pixels (browser tab favicon) — are fine details lost?
- Imagine at 4000×4000 pixels (building-side billboard) — are edges clean, no pixelation?
- Test in browser DevTools at various sizes

**How to Test (Actual)**:
- Export and view at actual sizes on screen
- 16×16: Open in browser at native size, squint test (still identifiable?)
- 512×512: Zoom in; check for anti-aliasing artifacts, stroke crispness

**Pass/Fail**:
- ✅ PASS: Crisp at 16px, clean edges at 512px+, no SVG artifacts
- ⚠️ WARNING: Slight fuzziness at very small size, but acceptable
- ❌ FAIL: Illegible at 16px; pixelated or blurry at large sizes

**Why It Matters**: Modern brands exist on screens (favicon) and print (large format); logo must work everywhere

**Example**:
- FedEx logo: ✅ (arrow visible even at tiny size; scales perfectly)
- Logo with 1px strokes: ❌ (disappears at 16px)

---

### 4. Background Agnostic: Works on White, Black, Color, Texture
**Criterion**: Logo maintains visibility and impact on any background (white, black, colored, textured).

**How to Test**:
- Place on white background; legible?
- Place on black background; legible?
- Place on brand color; contrast sufficient?
- Place on competitor brand color (stress test); still distinguishable?
- Textured background (wood, fabric, concrete); logo readable?

**Pass/Fail**:
- ✅ PASS: Legible on all backgrounds tested; contrast maintained
- ⚠️ WARNING: Slight contrast issue on one background; fixable with adjustment
- ❌ FAIL: Illegible on black or white; requires background to work

**Why It Matters**: Logos appear on marketing materials, dark mode websites, print on colored paper; must adapt

**Technical Aid**: Check contrast ratio:
- White bg: Foreground color vs #FFFFFF
- Black bg: Foreground color vs #000000
- Color bg: Foreground color vs chosen brand color
- Target: 3:1+ (WCAG AA minimum for graphics)

**Example**:
- Nike Swoosh: ✅ (works black on white, white on black, gold on black, etc.)
- Logo that's pure red: ⚠️ (poor on red background; needs context)

---

### 5. Contrast Ratio: WCAG AA 3:1+ for All Color Combinations
**Criterion**: All color pairings in logo meet WCAG AA accessibility standard (3:1 minimum for graphical elements).

**How to Test**:
- Use WebAIM contrast checker (webaim.org/resources/contrastchecker)
- Test each color pair:
  - Logo color vs white background
  - Logo color vs black background
  - Secondary color vs primary (if multi-color)
- Document ratios

**Pass/Fail**:
- ✅ PASS: All combinations ≥3:1 (WCAG AA)
- ✅ EXCELLENT: All combinations ≥4.5:1 (WCAG AAA)
- ⚠️ WARNING: 2.5:1 to 3:1; functional but below standard
- ❌ FAIL: <2.5:1; poor accessibility

**Why It Matters**: Low contrast affects users with low vision; ensures inclusive design

**Example**:
- Black on white: ✅ 21:1 (excellent)
- Navy on white: ✅ 7.6:1 (excellent)
- Light gray on white: ❌ 1.2:1 (fails)

---

### 6. Color Blind Safe: Pass Protanopia, Deuteranopia, Tritanopia Tests
**Criterion**: Logo remains distinct and identifiable for users with all types of color blindness (red-blind, green-blind, blue-yellow blind).

**How to Test**:
- Use Coblis simulator (coblis.com) to view logo in three color-blind modes
- Or Color Oracle desktop app (color-oracle.org)
- Ask: Is the logo still recognizable? Do shapes remain distinct?

**Pass/Fail**:
- ✅ PASS: Distinct in all three color-blind simulations
- ⚠️ WARNING: Slightly less distinct but still recognizable
- ❌ FAIL: Indistinguishable in one or more color-blind simulation

**Why It Matters**: 
- ~8% of males, 0.5% of females have color blindness
- Ethical design includes all users
- Monochrome test (Checkpoint #2) often covers this, but color-blind simulation is more thorough

**Example**:
- Logo using red/green distinction alone: ❌ (fails Protanopia)
- Logo using contrast (dark/light) + color: ✅ (works for color-blind)

---

### 7. SVG Optimized: Clean Code, No Artifacts, ≤5KB After SVGO
**Criterion**: SVG master file is well-structured, optimized, and free of visual artifacts.

**How to Test**:
- Run SVGO (svgo.js.org) on SVG file
- Check file size reduction (target: <5 KB for typical logo)
- Open in text editor; verify clean structure (no Figma/Illustrator metadata)
- Render in browser; look for any visual glitches (offset shapes, clipping artifacts)

**Pass/Fail**:
- ✅ PASS: SVGO optimized, <5 KB, renders cleanly, no artifacts
- ⚠️ WARNING: 5-10 KB, minimal artifacts, mostly clean
- ❌ FAIL: >10 KB; visual glitches; excessive metadata

**Why It Matters**: 
- Smaller files = faster loading
- Clean code = maintainable; easier to edit later
- No artifacts = professional quality

**Example**:
```
Before SVGO: 2.3 KB
After SVGO: 1.8 KB ✅ (78% efficiency)

After SVGO: 8.5 KB ⚠️ (acceptable but could optimize more)
After SVGO: 15 KB ❌ (needs optimization)
```

---

### 8. Typography: Font Pairing Follows Harmonic or Contrast Rules
**Criterion** (if wordmark or mark+word): Fonts are intentionally paired and readable, following established pairing principles.

**How to Test** (if typography present):
- Identify primary and secondary fonts
- Is pairing harmonic (same family) or contrasting (serif + sans)?
- Are weights distinct (e.g., Bold + Regular, not Bold + Medium)?
- Legible at 16px (if part of logo)?
- Do fonts complement brand tone?

**Pass/Fail** (Typography Present):
- ✅ PASS: Clear pairing strategy; intentional, readable, fits brand
- ⚠️ WARNING: Acceptable pairing; slightly generic but functional
- ❌ FAIL: Random fonts; poor contrast; unreadable at small sizes
- N/A: Logo has no typography (icon-only)

**Why It Matters**: Typography is 95% of identity design; poor pairing undermines entire logo

**Example**:
- Montserrat Bold + Inter Regular: ✅ (harmonic, contemporary, readable)
- Comic Sans + Helvetica: ❌ (no intentional pairing, clashes)

---

### 9. Negative Space: Intentional, Not Accidental Gaps
**Criterion**: Empty space is used meaningfully (hidden symbols, breathing room, visual interest) rather than incidental.

**How to Test**:
- Look at "holes" or empty areas in logo
- Are they necessary for the design, or do they feel like mistakes?
- Are there clever uses of negative space (e.g., FedEx arrow)?
- Does breathing room enhance or clutter the logo?

**Pass/Fail**:
- ✅ PASS: Negative space is intentional; may contain hidden symbols or enhance form
- ✅ EXCELLENT: Clever use of negative space (hidden meaning, aha moment)
- ⚠️ WARNING: Negative space present but not particularly meaningful
- ❌ FAIL: Negative space feels accidental or distracts

**Why It Matters**: Intentional negative space = sophisticated design; memorable (FedEx arrow, Toblerone bear)

**Example**:
- Nike Swoosh: ✅ (negative space between swoosh and type enhances form)
- FedEx logo: ✅✅ (arrow hidden in space between letters — clever!)
- Random gap in logo: ❌ (feels like design error)

---

### 10. Grid Foundation: Built on Golden Ratio or Clear Geometric System
**Criterion**: Logo proportions are based on mathematical systems (Golden Ratio, grid, geometric shapes) — not random placement.

**How to Test**:
- Can you identify a grid system in the logo? (e.g., all circles 1:1 ratio)
- Do proportions follow Golden Ratio (1:1.618)?
- Are elements aligned to consistent snap points?
- Does removal of guidelines maintain visual harmony?

**Pass/Fail**:
- ✅ PASS: Clear geometric foundation; proportions deliberate
- ✅ EXCELLENT: Golden Ratio or professional grid system evident
- ⚠️ WARNING: Some geometric logic but not systematic
- ❌ FAIL: Appears randomly placed; no proportional logic

**Why It Matters**: 
- Geometric foundation = timelessness (classical harmony)
- Easier to scale and adapt
- Discipline in design = professional quality

**Example**:
- Apple logo: ✅ (proportional, symmetrical, geometric)
- Mastercard circles: ✅✅ (mathematical overlap; Golden Ratio-inspired)
- Logo drawn freehand with no structure: ❌ (lacks foundation)

---

### 11. Motion-Ready: Can Support Subtle CSS Animations Without Disruption
**Criterion**: Logo structure allows for subtle animation (stroke animation, opacity fade, color transitions) if needed in future.

**How to Test**:
- Mentally animate stroke drawing (if stroke-based)
- Color transition (primary → accent color)
- Opacity fade-in
- Subtle rotate or scale
- Ask: Does animation enhance or disrupt brand perception?

**Pass/Fail**:
- ✅ PASS: Animation possible; enhances without excess
- ⚠️ WARNING: Animation possible but not critical
- ❌ FAIL: Logo structure doesn't support animation; would feel gimmicky

**Why It Matters**: 
- Modern web expects micro-interactions
- Animation isn't required but feasible with good SVG structure
- Future-proofs logo design

**Example**:
- SVG with well-defined paths: ✅ (stroke drawing animation possible)
- Logo that's a gradient blob: ⚠️ (animation less natural)

---

### 12. File Formats Available: SVG, PNG, Favicon Set, CSS
**Criterion**: Logo exists in multiple formats ready for different applications (web, mobile, print, icon).

**Checklist**:
- [ ] SVG master file (editable)
- [ ] SVG optimized (production)
- [ ] PNG (32×32, 48×48, 192×192, 512×512px)
- [ ] Favicon set (16, 32, 48, 180, 192, 512px)
- [ ] Monochrome variants (black/white)
- [ ] CSS class hooks (for theming)

**Pass/Fail**:
- ✅ PASS: SVG master + PNG fallbacks + favicon set ready
- ⚠️ WARNING: SVG + some PNG sizes available
- ❌ FAIL: Only one format; not production-ready

**Why It Matters**: Different use cases require different formats; incomplete delivery limits usability

---

### 13. Favicon Viability: Legible at 16×16px Confirmed
**Criterion**: Logo can be meaningfully reduced to 16×16px favicon without loss of identity.

**How to Test**:
- Mentally render at 16×16 pixels (very small)
- Can you still identify it as the brand?
- Are fine details lost (acceptable if essence remains)?
- Test in browser at actual favicon size

**Pass/Fail**:
- ✅ PASS: Favicon-viable; clear and identifiable at 16×16px
- ⚠️ WARNING: Possible favicon but some detail lost; works if necessary
- ❌ FAIL: Too complex for favicon; fine detail disappears entirely

**Why It Matters**: Favicon is first visual touchpoint in browser tab; must work at smallest scale

**Example**:
- Simple mark (circle, square, swoosh): ✅ (obvious favicon)
- Complex 5-element logo: ❌ (impossible to render at 16px)

---

### 14. Consistency: Maintains Integrity Across Scales, Backgrounds, Formats
**Criterion**: Logo "feels the same" whether displayed at 32px or 512px, on paper or screen, in color or monochrome.

**How to Test**:
- View at 5 different sizes (16, 64, 256, 512, 2000px)
- View on 3 different backgrounds (white, black, color)
- View in 3 formats (SVG, PNG, monochrome)
- Ask: Does it feel like the same logo? Or does it transform?

**Pass/Fail**:
- ✅ PASS: Consistent identity across all contexts
- ⚠️ WARNING: Mostly consistent; minor adjustments acceptable
- ❌ FAIL: Looks different at different scales; loses identity in formats

**Why It Matters**: Brand consistency = trust; if logo feels "different" in different contexts, brand perception weakens

---

### 15. Future-Proof: Not Reliant on 2025-2026 Trends; Flexible for Evolution
**Criterion**: Logo doesn't depend on trendy design elements that will age poorly; flexible enough to adapt as brand evolves.

**How to Test**:
- Remove 2024-2026 trend elements (cosmic gradients, retro-futurism, if added for novelty)
- Would logo look dated in 2030?
- Can colors evolve without redesign?
- Can proportions remain stable if accent colors change?
- Compare to timeless logos (Apple, Nike, Mastercard) — how does it hold up?

**Pass/Fail**:
- ✅ PASS: Timeless foundation; trends are optional layers, not core
- ⚠️ WARNING: Some trendy elements; may require refresh in 5 years
- ❌ FAIL: Heavily trend-dependent; likely to date quickly

**Why It Matters**: 
- Logo redesigns cost 6-7 figures
- Timeless design pays for itself through longevity
- Trends are decoration; principles are structure

**Example**:
- Apple logo (simple fruit): ✅ (works in 1977, 2000, 2024, 2030)
- Logo with 2024 gradient + retro font: ⚠️ (may feel dated by 2028)
- Logo entirely dependent on neon color trend: ❌ (will feel dated in 3 years)

---

## How to Use This Checklist

### For Skill Internal Use (During Generation)
1. **Concept Review**: Before delivering each of the 5 concepts, evaluate against all 15 checkpoints
2. **Scoring**: Count ✅ (pass) vs ⚠️ (warning) vs ❌ (fail)
   - 14-15 ✅: Excellent concept, deliver
   - 12-13 ✅, 1-3 ⚠️: Good concept, note limitations in description
   - <12 ✅: Reconsider; may need iteration
3. **Documentation**: Include checklist assessment in design rationale

### For User Reference (Design Refinement)
- User selects concept → can request refinement on specific checkpoints
- "Make it more timeless" = work on Checkpoint #15
- "Simplify more" = work on Checkpoint #1
- "Test for color blind" = Checkpoint #6

### For Final Delivery
```markdown
✅ Checkpoint Evaluation — Concept 1: Wordmark

1. ✅ Simplicity: ≤3 elements
2. ✅ Monochrome: Legible in B/W
3. ✅ Scalability: Clear at 16-512px
4. ✅ Background agnostic: Tested on white, black, color
5. ✅ Contrast: 8.2:1 (WCAG AAA)
6. ✅ Color blind safe: All simulators pass
7. ✅ SVG optimized: 2.8 KB
8. ✅ Typography: Montserrat Bold + Inter (harmonic)
9. ✅ Negative space: Intentional breathing room
10. ✅ Grid foundation: Proportional, geometric
11. ✅ Motion-ready: Can animate color transition
12. ✅ File formats: SVG, PNG variants, favicon set ready
13. ✅ Favicon viability: Clear at 16×16px
14. ✅ Consistency: Same logo across all contexts
15. ✅ Future-proof: No trend dependency; timeless structure

**Result**: 15/15 ✅ Excellent concept — ready for production
```

---

## Checkpoint Cross-Reference

| Checkpoint | Related Principle | Technical | Modern Trend |
|-----------|------------------|-----------|--------------|
| 1. Simplicity | Core | - | ✓ (Minimalism) |
| 2. Monochrome | Versatility | - | ✓ (Accessibility) |
| 3. Scalability | Core + Technical | ✓ | - |
| 4. Background Agnostic | Versatility | - | - |
| 5. Contrast | Technical | ✓ | ✓ (WCAG, Accessibility) |
| 6. Color Blind Safe | Technical | ✓ | ✓ (Accessibility) |
| 7. SVG Optimized | Technical | ✓ | - |
| 8. Typography | Design | - | ✓ (Custom lettering trend) |
| 9. Negative Space | Memorability | - | ✓ (Trend 2024-2026) |
| 10. Grid Foundation | Timelessness | - | - |
| 11. Motion-Ready | Technical | ✓ | ✓ (Web standard) |
| 12. File Formats | Technical | ✓ | - |
| 13. Favicon Viability | Scalability | ✓ | ✓ (Web standard) |
| 14. Consistency | Core | - | - |
| 15. Future-Proof | Timelessness | - | - |
