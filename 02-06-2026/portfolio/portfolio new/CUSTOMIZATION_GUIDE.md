# ðŸŽ¨ Portfolio Customization Guide

This guide provides step-by-step instructions to personalize your portfolio website.

## Table of Contents
1. [Quick Start](#quick-start)
2. [Content Changes](#content-changes)
3. [Color Customization](#color-customization)
4. [Typography](#typography)
5. [Images & Media](#images--media)
6. [Advanced Customization](#advanced-customization)

---

## Quick Start

### Step 1: Replace Your Information
The easiest way to customize is by finding and replacing text directly in `index.html`:

1. Open `index.html` in your text editor
2. Use Ctrl+H (or Cmd+H on Mac) to open Find and Replace
3. Replace all instances of "GOKULARASU K" with your name
4. Replace contact information with your details
5. Update all section content with your information

### Step 2: Add Your Profile Picture
1. Prepare a square profile photo (minimum 400x400px, recommended 600x600px)
2. Save it as `profile.jpg` in the `assets/images/` folder
3. The image will automatically scale for all devices

### Step 3: Choose Your Colors
1. Open `css/style.css`
2. Find the `:root` section (around line 15)
3. Replace the color codes with your preferred colors (see examples below)

---

## Content Changes

### Update Hero Section

**File**: `index.html` (Around line 70-90)

**Original**:
```html
<h1 class="hero-title">GOKULARASU K</h1>
<p class="hero-designation">AI & Data Analytics Enthusiast | Web Developer</p>
<p class="hero-intro">
    Welcome to my portfolio! I'm a Computer Science and Business Systems student...
</p>
```

**Updated Example**:
```html
<h1 class="hero-title">John Developer</h1>
<p class="hero-designation">Full Stack Developer | Open Source Contributor</p>
<p class="hero-intro">
    Welcome to my portfolio! I'm a passionate full-stack developer with 5+ years of 
    experience building scalable web applications and contributing to open-source projects.
</p>
```

### Update About Section

**File**: `index.html` (Around line 160-190)

**Original**:
```html
<p class="about-paragraph">
    I am a dedicated Computer Science and Business Systems student...
</p>
```

**Updated Example**:
```html
<p class="about-paragraph">
    I am an experienced software engineer specializing in cloud infrastructure 
    and DevOps solutions. With a passion for building robust systems and 
    mentoring junior developers...
</p>
```

### Add/Remove Skills

**File**: `index.html` (Around line 270-300)

**Original**:
```html
<div class="skill-list">
    <span class="skill-badge">Python</span>
    <span class="skill-badge">Java</span>
    <span class="skill-badge">JavaScript</span>
</div>
```

**Add Skills**:
```html
<div class="skill-list">
    <span class="skill-badge">Python</span>
    <span class="skill-badge">Java</span>
    <span class="skill-badge">JavaScript</span>
    <span class="skill-badge">TypeScript</span>    <!-- New -->
    <span class="skill-badge">Rust</span>          <!-- New -->
    <span class="skill-badge">Go</span>            <!-- New -->
</div>
```

### Update Projects

**File**: `index.html` (Around line 320-370)

**Original**:
```html
<article class="project-card">
    <div class="project-header">
        <h3 class="project-title">AI-Powered Chat Application</h3>
        <span class="project-category">AI & Web Dev</span>
    </div>
    <p class="project-description">
        A modern web-based chatbot application...
    </p>
    <div class="project-tech">
        <span class="tech-tag">Python</span>
        <span class="tech-tag">React</span>
        <span class="tech-tag">ML</span>
    </div>
    <a href="#" class="project-link">View Project â†’</a>
</article>
```

**Updated Example**:
```html
<article class="project-card">
    <div class="project-header">
        <h3 class="project-title">E-Commerce Platform</h3>
        <span class="project-category">Web Development</span>
    </div>
    <p class="project-description">
        A complete e-commerce platform with payment integration, inventory management, 
        and real-time analytics dashboard. Handles 10K+ daily transactions.
    </p>
    <div class="project-tech">
        <span class="tech-tag">React</span>
        <span class="tech-tag">Node.js</span>
        <span class="tech-tag">PostgreSQL</span>
        <span class="tech-tag">Stripe</span>
    </div>
    <a href="https://github.com/yourname/ecommerce" class="project-link">View Project â†’</a>
</article>
```

---

## Color Customization

### Primary Colors

**File**: `css/style.css` (Lines 15-21)

**Original**:
```css
:root {
    --primary-dark-blue: #0a2463;      /* Dark Blue */
    --primary-sky-blue: #247ba0;       /* Sky Blue */
    --accent-sky-blue: #4ecdc4;        /* Accent Sky Blue */
    --light-bg: #f0f4f8;               /* Light Background */
    --dark-bg: #1a1a2e;                /* Dark Background */
}
```

### Color Scheme Examples

#### Example 1: Purple & Pink Theme
```css
:root {
    --primary-dark-blue: #2d1b3d;      /* Dark Purple */
    --primary-sky-blue: #6c5b8e;       /* Purple */
    --accent-sky-blue: #ff6b9d;        /* Pink */
    --light-bg: #f5f0ff;               /* Light Purple */
    --dark-bg: #1a1a2e;                /* Dark Background */
}
```

#### Example 2: Green & Teal Theme
```css
:root {
    --primary-dark-blue: #0f3d3c;      /* Dark Teal */
    --primary-sky-blue: #1f5f5a;       /* Teal */
    --accent-sky-blue: #52b788;        /* Green */
    --light-bg: #e8f5f1;               /* Light Teal */
    --dark-bg: #1a1a2e;                /* Dark Background */
}
```

#### Example 3: Orange & Yellow Theme
```css
:root {
    --primary-dark-blue: #332701;      /* Dark Orange */
    --primary-sky-blue: #f77f00;       /* Orange */
    --accent-sky-blue: #fcbf49;        /* Yellow */
    --light-bg: #fff3e0;               /* Light Orange */
    --dark-bg: #1a1a2e;                /* Dark Background */
}
```

#### Example 4: Red & Coral Theme
```css
:root {
    --primary-dark-blue: #5a1a1a;      /* Dark Red */
    --primary-sky-blue: #d6373f;       /* Red */
    --accent-sky-blue: #ff7f7f;        /* Coral */
    --light-bg: #ffe5e5;               /* Light Red */
    --dark-bg: #1a1a2e;                /* Dark Background */
}
```

### How to Find Color Codes

1. **Online Color Picker**: Use tools like [Coolors.co](https://coolors.co/)
2. **Extract from Image**: Use [Google's Color Picker](https://www.google.com/search?q=color%20picker)
3. **Complementary Colors**: Use [Adobe Color Wheel](https://color.adobe.com/)

---

## Typography

### Change Primary Font

**File**: `css/style.css` (Lines 22-23)

**Original**:
```css
--font-primary: 'Poppins', sans-serif;
--font-secondary: 'Inter', sans-serif;
```

**Alternative Fonts**:

Option 1: Modern Sans-Serif
```css
--font-primary: 'Montserrat', sans-serif;
--font-secondary: 'Open Sans', sans-serif;
```

Option 2: Professional
```css
--font-primary: 'Playfair Display', serif;
--font-secondary: 'Lato', sans-serif;
```

Option 3: Tech-Focused
```css
--font-primary: 'JetBrains Mono', monospace;
--font-secondary: 'Roboto', sans-serif;
```

### Update Google Fonts Import

**File**: `index.html` (Line 10)

**Original**:
```html
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
```

**Updated Example** (For Montserrat + Open Sans):
```html
<link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;500;600;700&family=Open+Sans:wght@300;400;500;600&display=swap" rel="stylesheet">
```

### Adjust Font Sizes

**File**: `css/style.css` (Lines 24-27)

**Original**:
```css
--font-size-h1: 3rem;
--font-size-h2: 2.2rem;
--font-size-h3: 1.5rem;
--font-size-body: 1rem;
```

**Larger (Bolder Impact)**:
```css
--font-size-h1: 3.5rem;
--font-size-h2: 2.8rem;
--font-size-h3: 1.8rem;
--font-size-body: 1.1rem;
```

**Smaller (Compact)**:
```css
--font-size-h1: 2.5rem;
--font-size-h2: 1.8rem;
--font-size-h3: 1.2rem;
--font-size-body: 0.95rem;
```

---

## Images & Media

### Replace Profile Picture

1. Prepare a square image (recommended: 600x600px)
2. Name it `profile.jpg`
3. Save in `assets/images/` folder
4. No code changes needed!

### Add Project Images

**File**: `index.html` (Update project cards)

```html
<article class="project-card">
    <!-- Add image before project header -->
    <img src="assets/images/project-1.jpg" alt="Project Name" class="project-image">
    
    <div class="project-header">
        <h3 class="project-title">Project Name</h3>
        <span class="project-category">Category</span>
    </div>
    <!-- ... rest of card ... -->
</article>
```

**Add CSS** (in `style.css`):
```css
.project-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: var(--border-radius-md) var(--border-radius-md) 0 0;
    margin: -var(--spacing-lg) -var(--spacing-lg) var(--spacing-md) -var(--spacing-lg);
}
```

### Add Background Images

**File**: `css/style.css` (Update hero section)

```css
.hero {
    background: linear-gradient(135deg, var(--light-bg) 0%, var(--white) 100%),
                url('path/to/background.jpg') no-repeat center/cover;
    background-blend-mode: overlay;
}
```

---

## Advanced Customization

### Add New Sections

**Example: Add a "Testimonials" Section**

1. **Add HTML** (in `index.html`):
```html
<!-- Add to navigation -->
<li><a href="#testimonials" class="nav-link">Testimonials</a></li>

<!-- Add new section after education -->
<section id="testimonials" class="testimonials">
    <div class="container">
        <h2 class="section-title">What Others Say</h2>
        
        <div class="testimonials-grid">
            <div class="testimonial-card">
                <p class="testimonial-text">"GOKULARASU is an exceptional developer..."</p>
                <p class="testimonial-author">- Client Name, Company</p>
            </div>
        </div>
    </div>
</section>
```

2. **Add CSS** (in `style.css`):
```css
.testimonials {
    background: var(--light-bg);
    padding: var(--spacing-xxl) 0;
}

.testimonials-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--spacing-lg);
}

.testimonial-card {
    background: var(--white);
    padding: var(--spacing-lg);
    border-radius: var(--border-radius-md);
    border-left: 4px solid var(--primary-sky-blue);
    transition: var(--transition-smooth);
}

.testimonial-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 20px rgba(36, 123, 160, 0.1);
}
```

### Add Smooth Page Transitions

Add this to `css/style.css`:

```css
/* Page fade-in effect */
body {
    animation: pageLoad 0.5s ease-out;
}

@keyframes pageLoad {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}
```

### Create a Dark Mode

Add this to `js/script.js`:

```javascript
// Toggle dark mode
function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

// Load dark mode preference
if (localStorage.getItem('darkMode') === 'true') {
    document.body.classList.add('dark-mode');
}
```

Add this to `css/style.css`:

```css
body.dark-mode {
    background-color: var(--dark-bg);
    color: var(--white);
}

body.dark-mode section {
    background-color: var(--dark-bg);
    color: var(--white);
}
```

---

## Tips & Best Practices

âœ… **DO**:
- Keep changes consistent across all pages
- Test changes in multiple browsers
- Backup original files before major changes
- Use consistent spacing and sizing
- Test on mobile devices
- Keep file sizes optimized

âŒ **DON'T**:
- Mix too many colors (stick to 3-4 main colors)
- Use too many different fonts (max 2-3)
- Make text too small (minimum 16px for body)
- Add too many animations (keep it professional)
- Forget to update all instances of changed text

---

## Need More Help?

- Check the main [README.md](README.md) for more information
- Review code comments in HTML, CSS, and JavaScript files
- Test changes incrementally
- Use browser developer tools (F12) to debug
- Compare with original files if something breaks

Happy customizing! ðŸŽ¨

