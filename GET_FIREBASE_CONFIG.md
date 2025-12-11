# Get Your Firebase Configuration

Follow these steps to get your Firebase configuration and complete the setup:

## Step 1: Enable Realtime Database

1. Go to https://console.firebase.google.com/u/0/project/eko1-4e/database
2. Click **"Create Database"** under Realtime Database
3. Choose your location (e.g., `us-central1`)
4. Start in **test mode** (we'll add security rules later)
5. Click **Enable**

## Step 2: Get Your Web App Configuration

1. Go to https://console.firebase.google.com/u/0/project/eko1-4e/settings/general
2. Scroll down to **"Your apps"** section
3. If you don't see a web app:
   - Click the `</>` (web icon) button
   - Register app nickname: **"EKO Web"**
   - Don't enable Firebase Hosting (we're using GitHub Pages)
   - Click **Register app**
4. You'll see a code snippet with `firebaseConfig` object that looks like:

```javascript
const firebaseConfig = {
  apiKey: "AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
  authDomain: "eko1-4e.firebaseapp.com",
  projectId: "eko1-4e",
  storageBucket: "eko1-4e.appspot.com",
  messagingSenderId: "123456789012",
  appId: "1:123456789012:web:abcdef123456",
  databaseURL: "https://eko1-4e-default-rtdb.firebaseio.com"
};
```

## Step 3: Update firebase-config.js

1. Open `firebase-config.js` in your Code folder
2. Replace these three values with your actual values:
   - `YOUR_API_KEY_HERE` → Your actual apiKey (starts with "AIza...")
   - `YOUR_MESSAGING_SENDER_ID_HERE` → Your actual messagingSenderId (numbers)
   - `YOUR_APP_ID_HERE` → Your actual appId (starts with "1:...")

**Example:**
```javascript
const firebaseConfig = {
    apiKey: "AIzaSyA1B2C3D4E5F6G7H8I9J0K1L2M3N4O5P6Q",  // ← Replace this
    authDomain: "eko1-4e.firebaseapp.com",              // ✓ Already correct
    projectId: "eko1-4e",                                // ✓ Already correct
    storageBucket: "eko1-4e.appspot.com",               // ✓ Already correct
    messagingSenderId: "123456789012",                   // ← Replace this
    appId: "1:123456789012:web:abc123def456",           // ← Replace this
    databaseURL: "https://eko1-4e-default-rtdb.firebaseio.com"  // ✓ Already correct
};
```

## Step 4: Set Database Security Rules

1. Go to https://console.firebase.google.com/u/0/project/eko1-4e/database/rules
2. Replace the rules with:

```json
{
  "rules": {
    "responses": {
      ".write": true,
      ".read": true,
      "$responseId": {
        ".validate": "newData.hasChildren(['timestamp'])"
      }
    }
  }
}
```

3. Click **Publish**

⚠️ **Note**: These rules allow anyone to read and write. For production, you should add authentication or more restrictive rules.

## Step 5: Test Locally

1. Open `index.html` in your browser
2. Open DevTools Console (F12)
3. You should see: "Firebase initialized successfully"
4. Fill out the form and submit
5. Check Firebase Console → Realtime Database to see your data

## Step 6: Push to GitHub

Once you've updated `firebase-config.js` with your credentials:

```bash
git add firebase-config.js
git commit -m "Configure Firebase for eko1-4e project"
git push origin main
```

Your site will be live at: **https://sean4e.github.io/eko**

## Troubleshooting

### "Permission denied" error
- Check that database rules allow writing to `/responses`
- Verify you're in test mode or have correct security rules

### "Firebase not initialized" in console
- Check that all three placeholder values are replaced in `firebase-config.js`
- Make sure there are no syntax errors (missing quotes, commas)
- Verify the Firebase scripts are loading (check Network tab)

### Database URL error
- Make sure Realtime Database is enabled (not just Firestore)
- The database URL should end with `.firebaseio.com`

### Still having issues?
- Check the browser console for specific error messages
- Verify your Firebase project is on the Spark (free) plan or higher
- Make sure billing is enabled if required

---

Need help? Check [FIREBASE_SETUP.md](FIREBASE_SETUP.md) for more detailed instructions.
