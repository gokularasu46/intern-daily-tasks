# ðŸš€ Quick Start Guide - Portfolio Website

Get your portfolio live in 5 minutes!

## First Time Setup (5 minutes)

### Step 1: View Your Portfolio (1 minute)
1. Open `index.html` file in your web browser
2. You should see the complete portfolio website!

### Step 2: Update Your Information (3 minutes)

**Using Find & Replace** (Easiest):
1. Open `index.html` in a text editor (VS Code recommended)
2. Press `Ctrl+H` to open Find & Replace
3. Replace these with your info:
   - Find: `GOKULARASU K` â†’ Replace: `YOUR NAME`
   - Find: `gokularasu@example.com` â†’ Replace: `your@email.com`
   - Find: `+91 98765 43210` â†’ Replace: `YOUR PHONE`

**Manually Edit**:
1. Open `index.html` in text editor
2. Update:
   - Line 60: Your name
   - Line 61: Your designation
   - Line 63-66: Your introduction
   - Line 230+: Your education info
   - Line 560+: Your contact info

### Step 3: Add Your Profile Picture (1 minute)
1. Prepare a square profile photo (400x400px minimum)
2. Name it `profile.jpg`
3. Place in `portfolio/assets/images/` folder
4. Save and reload browser - it's done!

### Step 4: Refresh Browser
1. Save all changes to `index.html`
2. Press `F5` or `Ctrl+R` to refresh the browser
3. View your updated portfolio!

---

## Customization Quick Tips

### Change Colors
**File**: `css/style.css` (Line 15-21)

Find this section:
```css
:root {
    --primary-dark-blue: #0a2463;
    --primary-sky-blue: #247ba0;
    --accent-sky-blue: #4ecdc4;
}
```

Replace with your colors. Popular options:
- **Purple**: `#6c5b8e`, `#3d2b56`, `#ff6b9d`
- **Green**: `#1f5f5a`, `#0f3d3c`, `#52b788`
- **Orange**: `#f77f00`, `#332701`, `#fcbf49`

### Add Skills
**File**: `index.html` (Around line 280)

Find `<span class="skill-badge">` and add more with your skills:
```html
<span class="skill-badge">Your Skill</span>
```

### Update Projects
**File**: `index.html` (Around line 320-370)

Edit the project cards with your real projects or examples.

### Change Font
**File**: `css/style.css` (Line 22-23)

Change to any Google Font. Update the import at Line 10 of `index.html`

---

## Testing Checklist (2 minutes)

- [ ] All your information displays correctly
- [ ] Profile picture shows
- [ ] Navigation links work (click and scroll)
- [ ] Mobile menu appears when shrinking window
- [ ] Contact form can be filled
- [ ] No console errors (press F12)

---

## Deploy Your Portfolio (2 minutes)

### Easiest Option: Netlify
1. Go to [netlify.com](https://netlify.com)
2. Sign up with GitHub
3. Click "New site from Git"
4. Select your portfolio repository
5. Done! Your site is live!

### Alternative: GitHub Pages
1. Create GitHub repository named `username.github.io`
2. Upload all your portfolio files
3. Go to repository Settings â†’ Pages
4. Select `main` branch as source
5. Done! Your site is live at `username.github.io`

### See Full Deployment Guide
See `DEPLOYMENT_GUIDE.md` for detailed instructions

---

## File Locations Reference

| What | Where | Example |
|------|-------|---------|
| Main content | `index.html` | Navigation, sections |
| Styling | `css/style.css` | Colors, layout |
| Interactivity | `js/script.js` | Navigation, form |
| Profile picture | `assets/images/profile.jpg` | Your photo |
| Resume | `assets/resume.pdf` | Your resume |

---

## Common Questions

**Q: How do I change the colors?**
A: Edit `css/style.css` lines 15-21, or see CUSTOMIZATION_GUIDE.md

**Q: Where do I add my resume?**
A: Save as `assets/resume.pdf` and the download button will work

**Q: How do I make it live online?**
A: See DEPLOYMENT_GUIDE.md for step-by-step instructions

**Q: Can I change the layout?**
A: Yes! See CUSTOMIZATION_GUIDE.md for advanced changes

**Q: Is there a mobile menu?**
A: Yes! It appears automatically on phones

**Q: How do I add more projects?**
A: Copy a project card in `index.html` and modify it

**Q: Can I use a custom domain?**
A: Yes! See DEPLOYMENT_GUIDE.md

**Q: Do I need coding knowledge?**
A: Not for basic customization! Just edit text and save

---

## Next Steps

1. âœ… **Complete**: View and test your portfolio locally
2. ðŸ“ **Update**: Add your information and pictures
3. ðŸŽ¨ **Customize**: Adjust colors if desired
4. âœ”ï¸ **Check**: Test all links and forms
5. ðŸš€ **Deploy**: Push to live using Netlify/GitHub Pages
6. ðŸ“¢ **Share**: Update LinkedIn, resume, social media

---

## Documentation Files

- **README.md** - Complete project documentation
- **CUSTOMIZATION_GUIDE.md** - How to customize colors, fonts, content
- **SETUP_CHECKLIST.md** - Pre-launch checklist
- **DEPLOYMENT_GUIDE.md** - How to deploy online

---

## Quick Command Reference

### Using Git
```bash
# Navigate to portfolio folder
cd portfolio

# Check status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Update portfolio"

# Push to GitHub
git push origin main
```

### Local Testing
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000

# Node.js
npx http-server
```
Then visit: `http://localhost:8000`

---

## Troubleshooting

**Portfolio looks broken:**
- Clear browser cache (Ctrl+Shift+Delete)
- Hard refresh (Ctrl+Shift+R)
- Check browser console for errors (F12)

**Profile picture not showing:**
- Check file is named `profile.jpg`
- Verify it's in `assets/images/` folder
- Check file permissions

**Links don't work:**
- Make sure `index.html` is open in browser
- Not opened as file path, but with local server
- Or use Netlify/GitHub Pages to deploy

**Form not working:**
- Fill out all fields
- Use valid email format
- Check browser console for errors

---

## Tips for Success

âœ¨ **Pro Tips**:
- Keep your resume updated at `assets/resume.pdf`
- Update portfolio every time you complete a project
- Add GitHub links to your projects
- Use clear, professional language
- Test on your phone
- Get feedback from friends

ðŸ“± **Mobile First**:
- Always test on mobile phone size
- Make sure buttons are clickable on touch
- Text should be readable on small screens
- Test horizontal orientation too

ðŸŽ¨ **Design Tips**:
- Don't use too many colors (stick to 3-4)
- Use consistent spacing
- Make important content stand out
- White space is your friend
- Professional > Fancy

ðŸ“ˆ **Growth Tips**:
- Share your portfolio URL everywhere
- Include link in email signature
- Update LinkedIn with portfolio link
- Add to GitHub profile
- Mention in interviews

---

## Need More Help?

ðŸ“š **Read These Files**:
1. README.md - Project overview
2. CUSTOMIZATION_GUIDE.md - How to customize
3. DEPLOYMENT_GUIDE.md - How to deploy
4. SETUP_CHECKLIST.md - Before launching

ðŸ”— **Useful Links**:
- [Netlify Docs](https://docs.netlify.com/)
- [GitHub Pages](https://pages.github.com/)
- [MDN Web Docs](https://developer.mozilla.org/)
- [Color Picker](https://coolors.co/)
- [Font Finder](https://fonts.google.com/)

---

## You're All Set! ðŸŽ‰

Your professional portfolio is ready to go. Now:
1. Update your information
2. Add your picture
3. Deploy online
4. Start sharing!

Good luck showcasing your amazing work! ðŸš€

---

**Questions? Issues?**
Check the documentation files or try:
- Clearing browser cache
- Using a different browser
- Re-reading the error messages
- Checking file locations

