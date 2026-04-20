---
pubDatetime: 2026-02-01T01:58:22Z
title: "Hugo Mermaid Integration Complete Guide"
postSlug: "hugo-mermaid-integration-complete-guide"
description: "Hugo Mermaid Integration Complete Guide"
tags:
  - visualization
  - development
  - hugo
  - tutorial
---

## Introduction

This comprehensive guide covers the complete process of integrating Mermaid diagrams into a Hugo site using the Ananke theme. We'll walk through the migration process, setup, and best practices for creating beautiful technical documentation.

## Background: From PaperMod to Ananke

Our Hugo site originally used the PaperMod theme but we successfully migrated to Ananke theme for better responsiveness and features. This migration included:

- Theme replacement and configuration updates
- Mermaid shortcode compatibility verification
- Template structure adjustments
- Build system optimization

## Mermaid Integration Architecture

### Components Required

1. **Mermaid Shortcode** (`layouts/shortcodes/mermaid.html`)
2. **JavaScript Partial** (`layouts/partials/mermaid.html`)
3. **Head Extension** (`layouts/partials/extend_head.html`)
4. **Hugo Configuration** (`config.toml`)

### File Structure

```
/media/docker/website/
├── layouts/
│   ├── shortcodes/
│   │   └── mermaid.html          # Mermaid shortcode
│   └── partials/
│       ├── mermaid.html          # Mermaid JavaScript
│       └── extend_head.html      # Head extension
├── config.toml                   # Hugo configuration
└── content/posts/               # Your content
```

## Step 1: Creating the Mermaid Shortcode

Create `/layouts/shortcodes/mermaid.html`:

```html
<div class="mermaid">
{{ .Inner }}
</div>
```

This shortcode wraps Mermaid diagram code in a div with the "mermaid" class for proper styling and JavaScript targeting.

## Step 2: Setting Up JavaScript Support

Create `/layouts/partials/mermaid.html`:

```html
<script src="https://cdn.jsdelivr.net/npm/mermaid@9.4.3/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({ 
    startOnLoad: true,
    theme: 'default',
    flowchart: {
        useMaxWidth: true,
        htmlLabels: true
    }
});
</script>
```

## Step 3: Integrating with Head Template

Create or update `/layouts/partials/extend_head.html`:

```html
{{ partial "mermaid.html" . }}
```

This ensures Mermaid JavaScript is loaded on every page.

## Step 4: Hugo Configuration

Update your `config.toml`:

```toml
[markup]
  [markup.goldmark]
    [markup.goldmark.renderer]
      unsafe = true  # Required for HTML in shortcodes

[params]
  # Ananke theme specific settings
  description = "Hugo site with Mermaid diagrams"
  author = "Your Name"
  
  # Mermaid configuration (if theme supports it)
  mermaid = true
```

## Using Mermaid in Content

### Basic Syntax

```markdown
{{< mermaid >}}
graph TD
    A[Start] --> B{Decision}
    B -->|Yes| C[Action 1]
    B -->|No| D[Action 2]
    C --> E[End]
    D --> E
{{< /mermaid >}}
```

### Example Diagrams

#### 1. Migration Process Flow

{{< mermaid >}}
graph TB
    A[PaperMod Theme] --> B{Migration Decision}
    B -->|Migrate| C[Ananke Theme]
    B -->|Stay| D[Keep PaperMod]
    
    C --> E[Backup Site]
    E --> F[Update config.toml]
    F --> G[Install Ananke]
    G --> H[Update Shortcodes]
    H --> I[Test Build]
    I --> J[Verification]
    
    D --> K[Continue PaperMod]
    
    J --> Success{Migration Complete?}
    Success -->|Yes| L[Deploy]
    Success -->|No| M[Debug Issues]
    M --> H
{{< /mermaid >}}

#### 2. Technical Architecture

{{< mermaid >}}
graph TB
    subgraph "Content Layer"
        A[Markdown Files]
        B[Frontmatter]
        C[Mermaid Code]
    end
    
    subgraph "Hugo Processing"
        D[Template Engine]
        E[Shortcode Processor]
        F[Markdown Parser]
    end
    
    subgraph "Theme Layer"
        G[Ananke Theme]
        H[Layouts]
        I[Partials]
    end
    
    subgraph "Output Layer"
        J[HTML Generation]
        K[CSS/JS Assets]
        L[Static Files]
    end
    
    A --> F
    B --> F
    C --> E
    F --> D
    E --> D
    D --> G
    G --> H
    H --> I
    I --> J
    J --> K
    K --> L
{{< /mermaid >}}

#### 3. Development Workflow

{{< mermaid >}}
graph LR
    A[Content Creation] --> B[Local Development]
    B --> C[Auto-Reload]
    C --> D[Visual Testing]
    D --> E{Content OK?}
    E -->|No| A
    E -->|Yes| F[Build Verification]
    F --> G[Deployment]
    G --> H[Production Testing]
    H --> I{Live Site OK?}
    I -->|No| J[Rollback]
    I -->|Yes| K[Success]
    J --> A
{{< /mermaid >}}

## Best Practices

### 1. Diagram Design

- **Keep it simple**: Complex diagrams are hard to read
- **Use consistent colors**: Maintain visual harmony
- **Label clearly**: All elements should have descriptive labels
- **Test on mobile**: Ensure diagrams work on small screens

### 2. Content Organization

- **Use H2/H3 headings**: Structure your content logically
- **Add context**: Explain what each diagram shows
- **Provide examples**: Show different diagram types
- **Include troubleshooting**: Help readers solve common issues

### 3. Performance Optimization

- **Minimize JavaScript**: Load Mermaid only when needed
- **Use CDN**: Leverage CDN for better performance
- **Configure properly**: Set appropriate Mermaid options
- **Test load times**: Ensure fast page loads

## Supported Diagram Types

Mermaid supports various diagram types:

### Flowcharts
{{< mermaid >}}
graph TD
    A --> B
    B --> C
{{< /mermaid >}}

### Sequence Diagrams
{{< mermaid >}}
sequenceDiagram
    participant A as Actor
    participant S as System
    A->>S: Request
    S->>A: Response
{{< /mermaid >}}

### Gantt Charts
{{< mermaid >}}
gantt
    title Project Timeline
    section Phase 1
    Task 1: 2024-01-01, 7d
    Task 2: 2024-01-08, 5d
{{< /mermaid >}}

### Pie Charts
{{< mermaid >}}
pie
    title Distribution
    "A": 45
    "B": 30
    "C": 25
{{< /mermaid >}}

## Troubleshooting Guide

### Common Issues

#### 1. Diagrams Not Rendering

**Symptoms**: Diagram code appears as text instead of rendered diagrams

**Solutions**:
- Check that `mermaid.min.js` is loading
- Verify shortcode syntax is correct
- Ensure `unsafe = true` in config.toml
- Check browser console for JavaScript errors

#### 2. Build Errors

**Symptoms**: Hugo build fails with template errors

**Solutions**:
- Validate HTML syntax in shortcode files
- Check file paths and permissions
- Verify Hugo version compatibility

#### 3. Styling Issues

**Symptoms**: Diagrams appear broken or misaligned

**Solutions**:
- Check CSS conflicts with theme
- Verify responsive design settings
- Test different Mermaid themes

### Debug Checklist

- [ ] Mermaid JavaScript loaded in browser
- [ ] Shortcode files exist and are accessible
- [ ] Hugo configuration allows unsafe HTML
- [ ] No JavaScript errors in browser console
- [ ] Diagram HTML appears in DOM
- [ ] Mermaid initialization successful
- [ ] Responsive design works correctly

## Advanced Features

### Custom Themes

You can customize Mermaid appearance:

{{< mermaid >}}
%%{init: {'theme':'base','themeVariables':{'primaryColor':'#e74c3c','primaryTextColor':'#ffffff'}}}%%
graph TD
    A[Custom Theme] --> B[Red Colors]
    B --> C[Styled Diagram]
    C --> D[Professional Look]
{{< /mermaid >}}

### Integration with Other Tools

- **Git workflow**: Version control your diagrams
- **CI/CD**: Automated testing of diagram rendering
- **Documentation**: Combine with other documentation tools
- **Analytics**: Track diagram engagement

## Migration Checklist

If you're migrating from another theme:

### Pre-Migration
- [ ] Backup current site
- [ ] Document current Mermaid setup
- [ ] Test in development environment
- [ ] Plan rollback strategy

### During Migration
- [ ] Install Ananke theme
- [ ] Update configuration
- [ ] Create/update shortcodes
- [ ] Test diagram rendering
- [ ] Verify responsive design

### Post-Migration
- [ ] Test all pages
- [ ] Check mobile responsiveness
- [ ] Verify performance
- [ ] Update documentation
- [ ] Deploy to production

## Performance Considerations

### JavaScript Loading

Mermaid.js adds approximately 200KB to your page size. Consider:

- **Lazy loading**: Load only on pages with diagrams
- **Caching**: Use appropriate cache headers
- **CDN**: Leverage CDN for better distribution
- **Minification**: Use minified version

### Build Optimization

- **Selective loading**: Include mermaid.js only when needed
- **Async loading**: Load JavaScript asynchronously
- **Critical CSS**: Optimize CSS loading
- **Image optimization**: Compress other assets

## Future Enhancements

### Potential Improvements

1. **Dynamic diagrams**: Interactive Mermaid diagrams
2. **Dark mode support**: Theme-aware diagram styling
3. **Accessibility**: Better screen reader support
4. **Performance**: Further optimization techniques

### Integration Opportunities

- **Search**: Make diagram content searchable
- **Export**: Allow users to export diagrams
- **Collaboration**: Real-time diagram editing
- **Analytics**: Track diagram usage patterns

## Conclusion

Integrating Mermaid with Hugo and Ananke theme provides a powerful combination for technical documentation and visual storytelling. The shortcode approach maintains clean content while enabling rich visualizations.

### Key Benefits

- **Clean content**: Markdown stays readable
- **Version control**: Diagrams tracked in Git
- **Responsive**: Works on all devices
- **Professional**: Publication-ready diagrams
- **Flexible**: Support for multiple diagram types

### Next Steps

1. **Experiment**: Try different diagram types
2. **Customize**: Adapt themes to match your brand
3. **Automate**: Set up testing and deployment workflows
4. **Share**: Document your experience for others

With this setup, you have a robust foundation for creating engaging technical content that combines the best of Hugo's performance and Mermaid's visualization capabilities.

## Resources

- [Hugo Documentation](https://gohugo.io/)
- [Mermaid Official Site](https://mermaid-js.github.io/)
- [Ananke Theme](https://github.com/theNewDynamic/gohugo-theme-ananke)
- [Hugo Shortcodes Guide](https://gohugo.io/templates/shortcode-templates/)
- [Web Performance Best Practices](https://web.dev/performance/)