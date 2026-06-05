---
name: nano-banana
description: Generate or edit images using Google Gemini 2.5 Flash Image (Nano Banana). Use when the user asks to create, generate, draw, design, or edit an image — including logos, illustrations, mockups, photo edits, background changes, and multi-image composition. Triggers include "generate an image", "create a picture", "make a logo", "draw X", "edit this photo", "change the background", "combine these images", "napravi sliku", "generiraj sliku", "izradi sliku", "nacrtaj", "uredi sliku", "promijeni pozadinu", "spoji slike". Outputs PNG to ~/Downloads/ by default.
allowed-tools: Bash(nano-banana:*), Bash(~/.claude/bin/nano-banana:*)
---

# nano-banana — Gemini 2.5 Flash Image

CLI wrapper around Google's `gemini-2.5-flash-image` model (a.k.a. Nano Banana). Generates or edits images and returns a PNG file path.

## Usage

Text-to-image:

```bash
nano-banana "a red sailboat at golden hour, cinematic, 35mm"
```

Edit an existing image (1 input):

```bash
nano-banana "change the background to a snowy mountain" -i ~/Downloads/photo.jpg
```

Multi-image composition (up to 3 inputs):

```bash
nano-banana "combine these into a single product mockup on a marble desk" \
  -i product.png -i background.jpg -i logo.png
```

Custom output path:

```bash
nano-banana "minimalist blue lightning-bolt logo, flat vector" -o ~/Pictures/logo.png
```

The script prints the saved file path to stdout (one line). Default location: `~/Downloads/nano-banana-<timestamp>-<slug>.png`.

## After generating

Always surface the result to the user with `SendUserFile` and a short caption — don't just mention the path in text. Example:

```
SendUserFile(files=["/Users/hrvoje/Downloads/nano-banana-20260529-...-red-sailboat.png"],
             caption="Crveni jedrenjak, golden hour", status="normal")
```

## Prompting tips

- Works in English **and** Croatian — Hrvoje često piše prompt na hrvatskom.
- For logos/branding, specify style + colors + era: "flat", "minimalist", "1980s retro", "neon synthwave".
- For edits, describe **only the change**, not the whole image — the model preserves what you don't mention.
- Aspect ratio: mention it explicitly in the prompt ("wide 16:9 banner", "square 1:1").
- For text inside images, put the exact words in quotes in the prompt.

## Failure modes

- **`ERROR: GEMINI_API_KEY not set`** → user needs to add the key to `~/.zshrc`. Get it at https://aistudio.google.com/apikey.
- **`model returned no image`** → prompt was rejected (safety filter) or model returned only text. Read stderr for the model's text response and rephrase.
- **`API call failed`** → check the error; often quota or wrong model id. Retry with `--model gemini-2.5-flash-image-preview` if the default fails.

## Cost note

Nano Banana is paid per-image on the Gemini API (free tier has limits). The user pays from their own Google AI Studio billing — fine to use freely on request but don't loop generations without asking.
