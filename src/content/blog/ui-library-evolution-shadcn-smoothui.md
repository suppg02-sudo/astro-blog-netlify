---
pubDatetime: 2026-03-07T23:30:00Z
title: "UI Library Evolution: The Rise of shadcn/ui v4.0.0 and the Legacy of Smooth-UI"
postSlug: "ui-library-evolution-shadcn-smoothui"
description: "UI Library Evolution: The Rise of shadcn/ui v4.0.0 and the Legacy of Smooth-UI"
tags:
  - frontend
  - ui-library
  - shadcn
  - design-system
  - react
---

## Introduction

The UI library landscape has undergone significant transformations in recent years. Two notable projects—Smooth-UI and shadcn/ui—represent different approaches to component library development. While Smooth-UI pioneered modern React UI patterns but was eventually deprecated, shadcn/ui has emerged as a dominant force with the recent release of version 4.0.0.

This post explores the evolution of these libraries, examines shadcn/ui v4.0.0's groundbreaking features, and provides insights into what developers should consider when choosing UI solutions in 2026.

{{< mermaid >}}
graph LR
    A[UI Library Evolution] --> B[Smooth-UI<br/>2018-2019<br/>Deprecated 2022]
    A --> C[shadcn/ui<br/>2023-2026<br/>Active: v4.0.0]
    
    B --> B1[Styled Components]
    B --> B2[Bootstrap-inspired]
    B --> B3[Developer Experience Focus]
    
    C --> C1[Copy-Paste Pattern]
    C --> C2[Tailwind CSS]
    C --> C3[Radix UI Primitives]
    C --> C4[Design System Foundation]
    
    C --> D[v4.0.0 Updates]
    D --> D1[Monorepo Support]
    D --> D2[New Color System]
    D --> D3[Astro Integration]
    D --> D4[shadcn/skills]
{{< /mermaid >}}

## The Legacy of Smooth-UI: Innovation and Sunset

Smooth-UI, created by Greg Bergé and the smooth-code team, was a modern React UI library that prioritized developer experience and productivity. It gained popularity for its clean API and integration with styled-components and Emotion.

**Key Characteristics:**
- **Style System Approach**: Component-first design with style consistency
- **Dual CSS-in-JS Support**: Compatible with both styled-components and Emotion
- **Bootstrap-Inspired**: Familiar patterns for Bootstrap developers
- **Small Bundle Size**: Optimized for performance

**Why Smooth-UI Was Deprecated:**
Smooth-UI was archived on June 20, 2022, with the last release being v11.1.5 on December 27, 2019. Several factors contributed to its decline:

1. **Emergence of New Patterns**: The React ecosystem shifted toward new styling paradigms
2. **Maintenance Burden**: Maintaining a full component library requires significant resources
3. **Alternative Solutions**: Libraries like Material-UI, Chakra UI, and later shadcn/ui offered different approaches
4. **Community Migration**: Developers migrated to more actively maintained alternatives

**Smooth-UI's Lasting Impact:**
Despite its deprecation, Smooth-UI influenced modern UI library development:
- Emphasized developer experience as a core metric
- Demonstrated the value of style systems over traditional component libraries
- Showed the importance of framework flexibility (styled-components vs Emotion)

## shadcn/ui: A New Paradigm for Component Libraries

shadcn/ui represents a fundamental shift in how developers approach UI components. Unlike traditional libraries that provide pre-built, opinionated components, shadcn/ui introduced the "copy-paste" pattern.

### Core Philosophy

**Not a Component Library, but a Design System:**
- Components are copied into your codebase, giving you full control
- No runtime dependency—your code becomes the library
- Tailwind CSS + Radix UI primitives = accessible, customizable components
- Design system foundation that evolves with your project

**Key Advantages:**
1. **Full Customization**: Every component is yours to modify
2. **No Breaking Updates**: Your code doesn't change unexpectedly
3. **Zero Runtime Cost**: No additional bundle size
4. **Type Safety**: Full TypeScript support with autocompletion
5. **Accessibility**: Built on Radix UI primitives with ARIA compliance

### Growth and Adoption

Since its launch, shadcn/ui has seen explosive growth:
- **108k+ GitHub stars** (as of March 2026)
- **8,000+ forks** demonstrating community engagement
- **Active development** with frequent releases
- **108k+ stars** on GitHub, making it one of the most popular UI libraries

## shadcn/ui v4.0.0: Major Enhancements (March 6, 2026)

Released just two days ago (March 6, 2026), version 4.0.0 introduces significant improvements that expand shadcn/ui's capabilities and developer experience.

### 1. Monorepo Support

**New Flag: `--monorepo`**
- Native support for Vite, Start, and React Router monorepos
- Workspace-aware component installation
- Proper dependency management across packages
- Simplified setup for multi-package projects

**Impact:** Teams working on large-scale applications can now use shadcn/ui seamlessly across monorepo architectures.

### 2. Expanded Color System

**New Base Colors:**
- **Mauve**: Soft purple-pink tones for modern aesthetics
- **Olive**: Earthy green for nature-inspired designs
- **Mist**: Subtle gray-blue for neutral palettes
- **Taupe**: Warm gray for sophisticated interfaces

**Improved Radius Calculation:**
- Changed from additive to multiplicative calculation
- More consistent border radius scaling
- Better visual harmony across component sizes

**Deprecation:** The `--base-color` flag is deprecated in favor of the new color system.

### 3. Preset System

**New Flag: `--preset` for init command:**
- Quick project initialization with pre-configured setups
- Consistent design starting points
- Community-driven preset sharing
- Faster onboarding for new projects

**Example:**
```bash
npx shadcn@latest init --preset minimal
npx shadcn@latest init --preset ecommerce
```

### 4. Astro Template Support

**New Framework Integration:**
- Official Astro templates now supported
- Leverages Astro's island architecture
- Optimized for static site generation
- Server component compatibility

**Use Case:** Perfect for documentation sites, blogs, and content-heavy applications built with Astro.

### 5. Enhanced CLI Features

**New Command Flags:**
- `--dry-run`: Preview changes without applying them
- `--diff`: Show exactly what will change
- `--view`: Interactive diff viewer
- `--reinstall`: Clean reinstall of components
- `--base`: Base path specification for init

**Updated Commands:**
- `create` is now an alias for `init`
- `shadcn docs` command for documentation access
- `registry add` command for registry management
- Improved error messages and warnings

### 6. shadcn/skills Integration

**New Feature:**
- Integrated skill system for component patterns
- AI-friendly output from `shadcn info` command
- Better tooling support for AI code generation
- Structured component metadata

**Impact:** Enhances compatibility with AI coding assistants and automated code generation tools.

### 7. Deprecations and Breaking Changes

**Deprecated Features:**
- `--base-color`: Replaced by new color system
- `--src-dir`: Automatic detection now preferred
- `--no-base-style`: Configured via presets
- `--css-variables`: Standardized in new workflow
- `create` command: Use `init` instead
- `registry:build` and `registry:mcp`: New registry commands

**Migration Notes:**
- Most flags have automatic migration paths
- Breaking changes are well-documented
- Migration guides available in changelog

### 8. Workspace Support

**Enhanced Package Management:**
- Support for `hooks`, `lib`, and `ui` directories in workspaces
- Smart path resolution
- Automatic workspace detection
- Proper TypeScript configuration

{{< mermaid >}}
graph TD
    A[shadcn/ui v4.0.0 Features] --> B[CLI Enhancements]
    A --> C[Design System]
    A --> D[Framework Support]
    A --> E[Developer Experience]
    
    B --> B1[--monorepo flag]
    B --> B2[--dry-run, --diff, --view]
    B --> B3[--reinstall flag]
    B --> B4[Improved error messages]
    
    C --> C1[4 new base colors]
    C --> C2[Multiplicative radius]
    C --> C3[Presets system]
    C --> C4[Color migration path]
    
    D --> D1[Astro templates]
    D --> D2[React Router support]
    D --> D3[Vite integration]
    D --> D4[Monorepo architecture]
    
    E --> E1[shadcn/skills]
    E --> E2[AI-friendly output]
    E --> E3[Component registry]
    E --> E4[Documentation command]
{{< /mermaid >}}

## Comparison: Smooth-UI vs shadcn/ui

| Aspect | Smooth-UI | shadcn/ui |
|--------|-----------|-----------|
| **Status** | Deprecated (archived 2022) | Active (v4.0.0, March 2026) |
| **Styling** | styled-components / Emotion | Tailwind CSS |
| **Distribution** | npm package | Copy-paste components |
| **Bundle Impact** | Runtime dependency | Zero runtime cost |
| **Customization** | Theming API | Full code ownership |
| **TypeScript** | Partial support | Full support |
| **Accessibility** | Custom implementation | Radix UI primitives |
| **Maintenance** | Community-only | Active development |
| **Community** | 1.6k stars | 108k stars |
| **Last Update** | Dec 2019 | March 2026 |

## Developer Experience Evolution

The shift from Smooth-UI to shadcn/ui reflects broader trends in React development:

### From Black-Box Components to Open Source Your Code

**Smooth-UI Era (2018-2022):**
```javascript
import { Button, Card } from '@smooth-ui/core-sc'

const MyComponent = () => (
  <Card>
    <Button variant="primary">Click me</Button>
  </Card>
)
```

**shadcn/ui Era (2023-2026):**
```javascript
// Copy button component to your codebase
// Fully customizable, typed, and accessible
import { Button } from '@/components/ui/button'
import { Card, CardHeader, CardContent } from '@/components/ui/card'

const MyComponent = () => (
  <Card>
    <CardHeader>
      <Button>Click me</Button>
    </CardHeader>
    <CardContent>
      Content here
    </CardContent>
  </Card>
)
```

### Key Differences:

1. **Ownership**: shadcn/ui components live in your repo—you control every line
2. **Updates**: You choose when and how to update components
3. **Learning**: Reading component code is part of the learning process
4. **Flexibility**: No limitations on customization
5. **Type Safety**: Better TypeScript integration since code is local

## Recommendations for Developers

### When to Use shadcn/ui

✅ **Perfect for:**
- New projects starting with React + Tailwind
- Teams prioritizing customization and control
- Projects requiring strong accessibility standards
- Applications needing consistent design systems
- Monorepo architectures (v4.0.0+)

### When to Consider Alternatives

⚠️ **Consider if you need:**
- Pre-built, opinionated design systems (Material-UI, Chakra UI)
- Zero-setup component libraries (Mantine, NextUI)
- Frameworks with built-in styling solutions (Solid, Svelte)
- Teams without TypeScript experience

### Migration Path from Smooth-UI

If you're still using Smooth-UI:

1. **Assess Current Usage**: Catalog components and patterns
2. **Plan Migration Strategy**: Gradual vs complete rewrite
3. **Adopt Tailwind CSS**: Learn Tailwind fundamentals
4. **Explore shadcn/ui**: Start with core components
5. **Customize Components**: Adapt to your design system
6. **Remove Smooth-UI Dependencies**: Once migration complete

## Future Outlook

### shadcn/ui Roadmap Indicators:

Based on v4.0.0 changes, expect future developments in:
- **Enhanced AI Integration**: More tools for AI-assisted development
- **Framework Expansion**: Additional framework support beyond Astro
- **Advanced Presets**: More community-driven presets
- **Improved Monorepo Tools**: Better multi-package workflows
- **Component Intelligence**: Smart component suggestions

### Community Growth:

The 108k+ GitHub stars indicate strong community momentum:
- Active issue resolution
- Frequent feature releases
- Growing ecosystem of extensions
- Third-party integrations and templates

## Conclusion

The UI library landscape has evolved significantly from Smooth-UI's pioneering approach to shadcn/ui's innovative copy-paste paradigm. While Smooth-UI is now deprecated, its influence on developer experience design remains. shadcn/ui v4.0.0 represents the current state of the art, offering unprecedented control, customization, and developer satisfaction.

The key takeaway is that modern UI development prioritizes:
- **Control over convenience**
- **Customization over opinionation**
- **Ownership over dependency**
- **Sustainability over quick adoption**

For developers building new projects in 2026, shadcn/ui v4.0.0 offers a compelling balance of power, flexibility, and community support that aligns with modern development practices.

## Resources

- **shadcn/ui Documentation**: https://ui.shadcn.com
- **shadcn/ui GitHub**: https://github.com/shadcn-ui/ui
- **Smooth-UI (Archived)**: https://github.com/smooth-code/smooth-ui
- **shadcn/ui v4.0.0 Changelog**: https://github.com/shadcn-ui/ui/releases/tag/shadcn%404.0.0

---

*Published: March 7, 2026*
*Last Updated: March 7, 2026*