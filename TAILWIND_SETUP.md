# Tailwind CSS Setup Guide for TrekMate

## Current Setup (CDN - Development)

We're currently using **Tailwind CSS via CDN** which is perfect for development and prototyping.

### What's Already Working:
- ✅ **Tailwind CSS** loaded via CDN in `templates/base.html`
- ✅ **Custom color palette** with trek-specific colors
- ✅ **Google Fonts** (Inter) for better typography
- ✅ **Base template** that all pages extend from
- ✅ **Consistent styling** across all templates

### Files Structure:
```
templates/
├── base.html              # Base template with Tailwind CSS
├── core/
│   ├── dashboard.html     # Extends base.html
│   ├── about.html         # Extends base.html
│   └── contact.html       # Extends base.html
├── includes/
│   ├── navbar.html        # Uses Tailwind classes
│   └── footer.html        # Uses Tailwind classes
```

## Future Production Setup Options

### Option 1: Django + Node.js Build Process

#### 1. Install Node.js and npm
```bash
# Install Node.js (if not already installed)
curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash -
sudo apt-get install -y nodejs

# Verify installation
node --version
npm --version
```

#### 2. Initialize npm in your project
```bash
cd "/home/bishal/Booking Project"
npm init -y
```

#### 3. Install Tailwind CSS and build tools
```bash
npm install -D tailwindcss @tailwindcss/forms @tailwindcss/typography autoprefixer postcss postcss-cli
```

#### 4. Initialize Tailwind CSS
```bash
npx tailwindcss init -p
```

#### 5. Configure Tailwind CSS (`tailwind.config.js`)
```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js",
  ],
  theme: {
    extend: {
      colors: {
        'trek-blue': '#1e40af',
        'trek-green': '#059669',
        'trek-orange': '#ea580c',
        'trek-purple': '#7c3aed',
      },
      fontFamily: {
        'sans': ['Inter', 'system-ui', 'sans-serif'],
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
}
```

#### 6. Create CSS source file (`static/src/input.css`)
```css
@tailwind base;
@tailwind components;
@tailwind utilities;

/* Custom styles */
@layer components {
  .btn-primary {
    @apply bg-trek-blue hover:bg-blue-700 text-white font-bold py-2 px-4 rounded transition-colors;
  }
  
  .btn-secondary {
    @apply bg-transparent hover:bg-white text-trek-blue hover:text-gray-800 font-bold py-2 px-4 rounded border-2 border-trek-blue transition-colors;
  }
}
```

#### 7. Add build scripts to `package.json`
```json
{
  "scripts": {
    "build": "tailwindcss -i ./static/src/input.css -o ./static/css/output.css --watch",
    "build-prod": "tailwindcss -i ./static/src/input.css -o ./static/css/output.css --minify"
  }
}
```

#### 8. Update Django templates to use built CSS
Replace in `templates/base.html`:
```html
<!-- Remove this line -->
<script src="https://cdn.tailwindcss.com"></script>

<!-- Add this line instead -->
<link href="{% static 'css/output.css' %}" rel="stylesheet">
```

#### 9. Build CSS
```bash
# Development (watch mode)
npm run build

# Production (minified)
npm run build-prod
```

### Option 2: Django-Tailwind Package (Advanced)

#### 1. Install django-tailwind properly
```bash
pip install django-tailwind[reload]
```

#### 2. Add to INSTALLED_APPS
```python
INSTALLED_APPS = [
    # ... other apps
    'tailwind',
    'theme',
]

TAILWIND_APP_NAME = 'theme'
```

#### 3. Create theme app
```bash
python manage.py tailwind init
python manage.py tailwind install
```

#### 4. Start Tailwind build process
```bash
python manage.py tailwind start
```

## Current Benefits of CDN Approach

✅ **Zero setup time** - Works immediately  
✅ **No build process** - Instant updates  
✅ **Perfect for development** - Fast iteration  
✅ **No Node.js required** - Pure Django  
✅ **Easy to maintain** - Single file to update  

## When to Switch to Build Process

🔄 **Switch when you need:**
- **Production optimization** - Minified CSS
- **Custom Tailwind plugins** - Forms, Typography, etc.
- **Purge unused CSS** - Smaller file sizes
- **Advanced customization** - Custom components
- **Performance optimization** - Better loading times

## Current Custom Colors

```css
trek-blue: #1e40af    /* Primary brand color */
trek-green: #059669   /* Success/nature color */
trek-orange: #ea580c  /* Call-to-action color */
trek-purple: #7c3aed  /* Secondary brand color */
```

## Usage Examples

```html
<!-- Using custom colors -->
<div class="bg-trek-blue text-white">Primary section</div>
<button class="bg-trek-orange hover:bg-orange-600">Book Now</button>

<!-- Using utility classes -->
<div class="max-w-7xl mx-auto px-4 py-20">
  <h1 class="text-5xl font-bold text-gray-800 mb-6">Title</h1>
</div>
```

## Next Steps

1. **Continue development** with current CDN setup
2. **Test all pages** to ensure styling works
3. **When ready for production**, implement build process
4. **Consider adding** Tailwind plugins for forms and typography

---

**Note:** The current CDN setup is perfectly fine for development and small to medium projects. Only switch to a build process when you need production optimization or advanced Tailwind features.
