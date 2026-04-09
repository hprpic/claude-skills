# SVG & Favicon Technical Reference

**Knowledge Base**: Derived from web.dev, MDN Web Docs, SVG on the Web, RealFaviconGenerator, and 80+ technical sources.

---

## Why SVG for Logo Design (Mandatory)

### Advantages
1. **Infinite Scalability**: Vector-based; renders perfectly at 16px and 4000px without quality loss
2. **Small File Size**: Mathematical curves instead of pixel data; typically 2-10 KB vs 50+ KB PNG
3. **Semantic HTML**: `<title>`, `<desc>` for accessibility; `role="img"` for screen readers
4. **CSS Animatable**: Strokes, fills, opacity changes via CSS without separate files
5. **Dark Mode Compatible**: Can change colors via CSS `currentColor` or variables
6. **Resolution Independent**: One file works on all devices (1x, 2x, 3x screens)

### SVG Master File Checklist
- [ ] Created as `.svg` text file (not exported bitmap)
- [ ] Contains all design information (colors, strokes, text)
- [ ] Optimized with SVGO (removes unnecessary attributes)
- [ ] Semantic structure (grouped logically, named elements)
- [ ] Viewbox set correctly (e.g., `viewBox="0 0 256 256"`)
- [ ] Root element has `xmlns="http://www.w3.org/2000/svg"`
- [ ] No embedded raster images (except if intentional)

---

## SVG Structure & Anatomy

### Minimal SVG Template
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="Brand Name">
  <title>Brand Name Logo</title>
  <desc>Logo for Brand Name — description of design</desc>
  <defs>
    <!-- Optional: gradients, filters, patterns -->
  </defs>
  <!-- Logo shapes here -->
  <g id="logo-mark">
    <circle cx="128" cy="128" r="100" fill="#000000"/>
  </g>
</svg>
```

### Key Elements

#### `<svg>` Root
- **xmlns**: Required for SVG namespace
- **viewBox**: "minX minY width height" — defines coordinate system
  - Example: `viewBox="0 0 256 256"` = canvas is 256×256 units
- **width/height**: Optional; if omitted, viewBox ratio applies
- **role="img"**: Tells accessibility tools this is an image
- **aria-label**: Short description (read by screen readers)

#### `<title>` & `<desc>`
- **`<title>`**: Tooltip on hover, read by screen readers (short)
- **`<desc>`**: Full description for accessibility (can be longer)
- **Placement**: First child of `<svg>` or first child of group

#### `<defs>` (Optional)
- Contains gradients, patterns, filters, symbols reused in document
```svg
<defs>
  <linearGradient id="gradient-blue" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" style="stop-color:#0B2D4D;stop-opacity:1" />
    <stop offset="100%" style="stop-color:#1E90FF;stop-opacity:1" />
  </linearGradient>
</defs>
```

#### `<g>` (Grouping)
- Groups related shapes together
- Can set attributes (fill, opacity) on group; applies to all children
- Can be named with `id` for targeting via CSS
```svg
<g id="wordmark" fill="#000000">
  <text x="50" y="100">Brand Name</text>
</g>
```

#### Basic Shapes
- **`<circle>`**: `cx`, `cy` (center), `r` (radius), `fill`, `stroke`, `stroke-width`
- **`<rect>`**: `x`, `y`, `width`, `height`, `rx` (corner radius), `fill`, `stroke`
- **`<path>`**: `d` (data path), `fill`, `stroke` — most flexible
- **`<text>`**: `x`, `y`, `font-family`, `font-size`, `fill`

---

## Stroke Width & Scalability

### The Critical Challenge
**Problem**: Stroke width is absolute (pixel units) + viewBox defines coordinate system.
- If stroke is 2px and viewBox is 16×16, the stroke is 12.5% of canvas
- If viewBox is 256×256, same stroke is 0.78% of canvas
- Result: Stroke looks different at different scales

### Solution: Proportional Stroke Width

**Best Practice**:
- Define stroke as percentage of viewBox size
- Example: viewBox is 256×256; use stroke-width 2-4 for small logos, 8-12 for large
- Test at 16px and 4000px mental renders

**Testing Workflow**:
```
Favicon (16×16 viewport):
  viewBox="0 0 256 256"
  stroke-width=2 or 3 → renders as ~0.78-1.17px in browser
  
Large Format (1000×1000 viewport):
  Same SVG, stroke-width=2 or 3 → renders as ~7.8-11.7px
  
Result: Stroke scales proportionally with viewBox ✓
```

### Recommended Stroke Widths by Use Case
- **Icon/Favicon (16-48px display)**: stroke-width 2-3
- **Web (128px+)**: stroke-width 3-6
- **Print/Large Format**: stroke-width 6-12 (can adjust in production)

### SVG for Color-Free Version (Monochrome)
```svg
<!-- Master: Define stroke and fill as needed -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <circle cx="128" cy="128" r="80" fill="none" stroke="#000000" stroke-width="3"/>
  <rect x="50" y="50" width="156" height="156" fill="#0B2D4D" stroke="#000000" stroke-width="2"/>
</svg>

<!-- For dynamic theming -->
<circle cx="128" cy="128" r="80" fill="none" stroke="currentColor" stroke-width="3"/>
```

---

## Favicon Strategy (2026 Best Practices)

### What is a Favicon?
- Small icon displayed in browser tab, bookmarks, address bar, device home screen
- Required sizes: 16×16px (minimum), 32×32px, 48×48px, 180×180px (Apple), 192×192px (Android), 512×512px (PWA)
- Multiple files needed for full coverage

### Modern Favicon Implementation

#### Option 1: SVG + PNG Fallback (Recommended)
```html
<!-- Modern browsers prefer SVG -->
<link rel="icon" href="/favicon.svg" type="image/svg+xml">

<!-- PNG fallback for older browsers -->
<link rel="icon" href="/favicon-32x32.png" type="image/png" sizes="32x32">

<!-- Apple Touch Icon (iOS home screen) -->
<link rel="apple-touch-icon" href="/apple-touch-icon-180x180.png">

<!-- PWA manifest (Android Chrome home screen) -->
<link rel="manifest" href="/manifest.json">
```

#### Option 2: ICO Format (Legacy, still supported)
```html
<link rel="icon" href="/favicon.ico">
```
- **Note**: ICO supports multiple sizes embedded; less common now but still valid

### Favicon SVG Design Considerations

**Constraints**:
- Must be legible at 16×16px (absolute smallest size)
- High contrast essential (small size = limited color distinction)
- Simple geometry (complex paths muddy at tiny scale)
- No thin strokes (disappear below 1px on display)
- No serif details (blur/disappear)

**Design Approach**:
1. Start with simplest concept
2. Test on 16×16px canvas mentally
3. Remove any detail that vanishes at small size
4. Use solid fills for small favicon; outlines optional if >2px stroke
5. Ensure sufficient color contrast

**SVG Favicon Template**:
```svg
<!-- favicon.svg -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <title>Brand Favicon</title>
  <!-- Simple, bold shapes only -->
  <circle cx="128" cy="128" r="110" fill="#0B2D4D"/>
  <path d="M 100 100 L 150 150 L 100 150 Z" fill="#FFFFFF"/>
  <!-- Avoid: thin lines, small text, complex curves -->
</svg>
```

### PNG Favicon Generation Workflow

**For Each Required Size**, generate PNG:
1. **16×16px**: Simple, high contrast
2. **32×32px**: Can add slightly more detail
3. **48×48px**: More breathing room
4. **180×180px** (Apple): Larger canvas, can add detail
5. **192×192px** (Android): Similar to 180
6. **512×512px** (PWA): Full detail possible

**Manual Generation Process** (if no automated tool):
1. Export SVG to PNG at each size
2. Or use online converter: favicon.io, realfavicongenerator.net, convertio.co
3. Compress PNGs with TinyPNG or PNGQuant

**Recommended Tools**:
- **RealFaviconGenerator** (realfavicongenerator.net) — comprehensive, tests browser compatibility
- **Favicon.io** (favicon.io) — simple, fast
- **Converting.app** — SVG to PNG batch converter

### manifest.json for PWA
```json
{
  "name": "Brand Name",
  "short_name": "Brand",
  "icons": [
    {
      "src": "/android-chrome-192x192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/android-chrome-512x512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "theme_color": "#ffffff",
  "background_color": "#ffffff",
  "display": "standalone"
}
```

---

## SVG Optimization

### Why Optimize
- Reduces file size (2-10 KB typical, optimized = <5 KB)
- Faster load time
- Cleaner code for manual editing
- Better compatibility

### SVGO (SVG Optimizer)
**Command Line**:
```bash
npm install -g svgo
svgo logo.svg --output logo.min.svg
```

**What SVGO Does**:
- Removes unnecessary attributes
- Shortens paths (e.g., `M 100 100 L 150 100 L 150 150 Z` → compressed notation)
- Removes comments, metadata, hidden elements
- Converts colors to most efficient format

**What SVGO Preserves**:
- Semantic structure (title, desc, role, aria-label)
- Group IDs (for CSS targeting)
- Intentional fills and strokes

**Before & After**:
```svg
<!-- Before (400 bytes) -->
<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" 
     width="256" height="256" viewBox="0 0 256 256" fill="none" stroke="black" stroke-width="2">
  <circle cx="128" cy="128" r="100" fill="none" stroke="#000000" stroke-width="2.5"/>
  <rect x="50" y="50" width="156" height="156" fill="none" stroke="#000000" stroke-width="2.5"/>
</svg>

<!-- After (150 bytes) -->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256">
  <circle cx="128" cy="128" r="100" fill="none" stroke="#000" stroke-width="2.5"/>
  <rect x="50" y="50" width="156" height="156" fill="none" stroke="#000" stroke-width="2.5"/>
</svg>
```

---

## SVG Accessibility

### Semantic HTML for SVGs

#### 1. Title & Description
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" role="img" aria-label="Tech Brand Logo">
  <title>Tech Brand Logo</title>
  <desc>Abstract circular mark representing innovation and technology</desc>
  <!-- Logo content -->
</svg>
```

#### 2. Role & Aria-Label
- **role="img"**: Tells assistive tech this is a single image unit
- **aria-label**: Short label (read aloud by screen readers)
- Alternative: **aria-labelledby** pointing to `<title>` ID

#### 3. Grouped Elements with IDs
```svg
<g id="mark" role="presentation"> <!-- presentation = decorative, not narrated separately -->
  <circle cx="128" cy="128" r="80"/>
  <path d="..."/>
</g>
<text id="brand-name">Brand Name</text> <!-- Text is inherently accessible -->
```

#### 4. Testing Accessibility
- Use browser DevTools > Accessibility inspector
- Screen reader testing (NVDA, JAWS, VoiceOver)
- axe DevTools plugin (checks WCAG compliance)

---

## Color Variants in SVG

### Dynamic Theming with CSS
```svg
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256" class="logo">
  <circle id="logo-circle" cx="128" cy="128" r="80" fill="currentColor"/>
  <text id="logo-text" x="128" y="140" fill="currentColor">Brand</text>
</svg>
```

**CSS for Dynamic Color**:
```css
.logo {
  color: #0B2D4D; /* Default dark blue */
}

.logo.light-mode {
  color: #0B2D4D;
}

.logo.dark-mode {
  color: #F0EEE9; /* Light for dark background */
}

.logo.accent {
  color: #D97D5F; /* Terracotta accent */
}
```

### Color Variants (Separate Files)
- `logo.svg` (default colors)
- `logo-mono.svg` (black/white only)
- `logo-light.svg` (for dark background)
- `logo-accent.svg` (with accent color)

---

## Export & File Format Guidance

### Formats Needed for Complete Logo Package
1. **SVG Master** (`logo.svg`) — editable, archival
2. **SVG Optimized** (`logo.min.svg`) — production web use
3. **PNG** (32, 48, 192, 512px) — bitmap fallback for older browsers
4. **Favicon** (16, 32, 48, 180, 192, 512px) — specialized use
5. **Monochrome SVG** (`logo-mono.svg`) — accessibility test + print
6. **Color Variants** (optional) — dark mode, accent colorways

### Export Workflow
```
Master SVG (Figma/Illustrator)
  ↓
Export to SVG (ensure no Figma metadata)
  ↓
Optimize with SVGO
  ↓
Test rendering in browser (Chrome, Firefox, Safari)
  ↓
Test monochrome (grayscale filter)
  ↓
Test favicon sizes (16×16 mentally)
  ↓
Generate PNG variants (at required sizes)
  ↓
Package: SVG master, SVG min, PNGs, favicon set
```

---

## Testing & Quality Gates

### Browser Rendering Test
```html
<!-- Test page: save as test.html -->
<html>
<head>
  <title>Logo Rendering Test</title>
  <style>
    body { font-family: sans-serif; padding: 20px; }
    .test { margin: 20px 0; border: 1px solid #ccc; padding: 10px; }
    .test h3 { margin: 0; font-size: 14px; }
    img { vertical-align: middle; }
  </style>
</head>
<body>
  <h1>Logo Rendering Tests</h1>
  
  <div class="test">
    <h3>16px (Favicon)</h3>
    <img src="logo.svg" width="16" height="16" alt="Logo 16px">
  </div>
  
  <div class="test">
    <h3>32px (Tab icon)</h3>
    <img src="logo.svg" width="32" height="32" alt="Logo 32px">
  </div>
  
  <div class="test">
    <h3>256px (Web)</h3>
    <img src="logo.svg" width="256" height="256" alt="Logo 256px">
  </div>
  
  <div class="test">
    <h3>Monochrome (Grayscale)</h3>
    <img src="logo.svg" width="256" height="256" alt="Logo" style="filter: grayscale(100%);">
  </div>
  
  <div class="test">
    <h3>Dark Background</h3>
    <div style="background: #000; padding: 10px; display: inline-block;">
      <img src="logo.svg" width="256" height="256" alt="Logo" style="filter: invert(1);">
    </div>
  </div>
</body>
</html>
```

### Checklist
- [ ] SVG renders cleanly in Firefox, Chrome, Safari
- [ ] 16px version is legible (test mentally or at actual size)
- [ ] 512px version is crisp, not pixelated
- [ ] Monochrome (grayscale) version maintains identity
- [ ] Dark background version is visible
- [ ] SVGO report shows file size reduction
- [ ] No browser console errors (inspect with DevTools)
- [ ] Favicon sizes generated and tested on real devices

---

## SVG Best Practices Summary

1. **Always start with SVG master** — single source of truth
2. **Optimize with SVGO** — production files
3. **Include accessibility** — `<title>`, `<desc>`, `role="img"`, `aria-label`
4. **Test at extremes** — 16px and 4000px mentally
5. **Stroke widths scale** — use proportional values (2-4 for small, 6-12 for large)
6. **Generate PNG fallbacks** — for older browser support
7. **Create favicon set** — 16, 32, 48, 180, 192, 512px
8. **Document colorways** — monochrome, light, dark variants
9. **Package deliverables** — SVG master, SVG min, PNG variants, favicon manifest
10. **Test browser compatibility** — especially older Safari, IE (if relevant)

---

## SVG Export Checklist for Skill Output

When delivering SVG logo concepts, verify:
- [ ] SVG renders cleanly in browser DevTools
- [ ] File size after SVGO: <5 KB (typical)
- [ ] Monochrome version legible (grayscale test)
- [ ] No warnings in browser console
- [ ] Favicon viability confirmed (16×16px mental test)
- [ ] Accessibility tags present (`<title>`, `<desc>`, `role`, `aria-label`)
- [ ] Stroke widths tested at multiple scales
- [ ] Color contrast meets WCAG AA (3:1 for graphical elements)
- [ ] Ready for favicon generation (separate task)
