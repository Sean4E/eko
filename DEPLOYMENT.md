# GitHub Pages Deployment Guide

Your code has been pushed to GitHub! Now let's enable GitHub Pages to make it live.

## Step 1: Enable GitHub Pages

1. Go to your repository: **https://github.com/Sean4E/eko**

2. Click on **Settings** (top right, gear icon)

3. In the left sidebar, click **Pages**

4. Under "Build and deployment":
   - **Source**: Select "Deploy from a branch"
   - **Branch**: Select `main` and `/ (root)`
   - Click **Save**

5. Wait 1-2 minutes for deployment

## Step 2: Access Your Live Site

Your site will be available at:
### **https://sean4e.github.io/eko**

You can find this URL at the top of the Pages settings once deployment is complete.

## Step 3: Set Up Firebase (Important!)

Your site will work without Firebase, but responses won't be saved to a database. To enable database storage:

1. Follow the instructions in [FIREBASE_SETUP.md](FIREBASE_SETUP.md)

2. Update `firebase-config.js` with your Firebase credentials:
   ```javascript
   const firebaseConfig = {
       apiKey: "YOUR_ACTUAL_API_KEY",
       authDomain: "your-project.firebaseapp.com",
       // ... other config values
   };
   ```

3. Commit and push the changes:
   ```bash
   git add firebase-config.js
   git commit -m "Configure Firebase database"
   git push origin main
   ```

4. GitHub Pages will automatically redeploy with your Firebase configuration

## Step 4: Test Your Site

1. Visit **https://sean4e.github.io/eko**
2. Fill out the questionnaire
3. Submit your responses
4. Check Firebase Console to verify data is being saved

## Making Updates

Whenever you make changes to your site:

```bash
# Stage your changes
git add .

# Commit with a descriptive message
git commit -m "Your update description"

# Push to GitHub
git push origin main
```

GitHub Pages will automatically rebuild and deploy your site within 1-2 minutes.

## Custom Domain (Optional)

Want to use your own domain instead of `sean4e.github.io/eko`?

1. In repository Settings → Pages
2. Under "Custom domain", enter your domain (e.g., `eko.yourdomain.com`)
3. Add a CNAME record in your domain's DNS settings pointing to `sean4e.github.io`
4. Wait for DNS propagation (can take up to 24 hours)

## Troubleshooting

### Site not loading after 5 minutes
- Check the Actions tab in your repository for deployment status
- Ensure the branch is set to `main` in Pages settings
- Try clearing your browser cache

### 404 Error
- Make sure `index.html` is in the root directory (not in a subfolder)
- Verify the branch name is `main` (not `master`)

### Firebase not working
- Check browser console (F12) for errors
- Verify your Firebase configuration in `firebase-config.js`
- Make sure Firebase scripts are loading (check Network tab in DevTools)
- Confirm database rules allow writing

### Changes not showing up
- GitHub Pages can take 1-2 minutes to rebuild
- Try a hard refresh: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
- Clear browser cache

## Monitoring & Analytics

### View Deployment Status
- Go to repository → Actions tab
- See all deployments and their status

### Monitor Traffic (Optional)
Add Google Analytics by inserting this in `<head>` of `index.html`:
```html
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=GA_MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'GA_MEASUREMENT_ID');
</script>
```

## Security Best Practices

1. **Never commit Firebase credentials directly** if they contain sensitive keys
2. Use environment variables or Firebase App Check for production
3. Set proper security rules in Firebase Console
4. Consider adding reCAPTCHA for form submission

## Next Steps

- [ ] Enable GitHub Pages (follow Step 1 above)
- [ ] Test the live site
- [ ] Set up Firebase database (see FIREBASE_SETUP.md)
- [ ] Share the URL with your audience
- [ ] Monitor responses in Firebase Console
- [ ] Export and analyze collected data

---

Need help? Open an issue in the repository or check the README.md for more information.
