# Firebase Setup Guide for EKO

This guide will help you set up Firebase to store user responses from the EKO questionnaire.

## Step 1: Create a Firebase Project

1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Click "Add project"
3. Enter project name: "EKO-Responses" (or your preferred name)
4. Follow the setup wizard (you can disable Google Analytics if not needed)

## Step 2: Set Up Realtime Database

1. In your Firebase project, click on "Realtime Database" in the left sidebar
2. Click "Create Database"
3. Choose a location (closest to your users)
4. **Start in test mode** for now (we'll add security rules later)
5. Click "Enable"

## Step 3: Get Your Firebase Configuration

1. In Firebase Console, click the gear icon ⚙️ next to "Project Overview"
2. Click "Project settings"
3. Scroll down to "Your apps"
4. Click the web icon `</>` to add a web app
5. Register your app with a nickname (e.g., "EKO Web")
6. Copy the `firebaseConfig` object that appears

## Step 4: Update Your Code

1. Open `firebase-config.js`
2. Replace the placeholder values in `firebaseConfig` with your actual values:

```javascript
const firebaseConfig = {
    apiKey: "YOUR_ACTUAL_API_KEY",
    authDomain: "your-project-id.firebaseapp.com",
    projectId: "your-project-id",
    storageBucket: "your-project-id.appspot.com",
    messagingSenderId: "123456789",
    appId: "1:123456789:web:abcdef",
    databaseURL: "https://your-project-id-default-rtdb.firebaseio.com"
};
```

## Step 5: Add Firebase Scripts to HTML

The Firebase SDK scripts are already included in your `index.html` file. Make sure these lines are present before the closing `</body>` tag:

```html
<!-- Firebase SDKs -->
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
<script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-database-compat.js"></script>

<!-- Your Firebase configuration -->
<script src="firebase-config.js"></script>
```

## Step 6: Security Rules (Important!)

After testing, update your database rules for better security:

1. Go to Firebase Console → Realtime Database → Rules
2. Replace with these rules:

```json
{
  "rules": {
    "responses": {
      ".write": true,
      ".read": "auth != null",
      "$responseId": {
        ".validate": "newData.hasChildren(['timestamp', 'participantName'])"
      }
    }
  }
}
```

This allows:
- **Anyone** to write responses (submit the form)
- **Only authenticated users** can read responses (for viewing data)
- Validates that submissions include required fields

## Step 7: Viewing Your Data

### Method 1: Firebase Console
- Go to Realtime Database in Firebase Console
- You'll see all responses in a tree structure

### Method 2: Export as CSV
- Open your webpage
- Open browser console (F12)
- Run: `exportResponsesAsCSV()`
- This will download a CSV file with all responses

### Method 3: Get All Data in Console
```javascript
getAllResponses().then(data => console.log(data));
```

## Admin Dashboard (Optional)

Create a separate admin page (`admin.html`) to view and export responses:

```html
<!DOCTYPE html>
<html>
<head>
    <title>EKO Admin Dashboard</title>
</head>
<body>
    <h1>EKO Responses Dashboard</h1>
    <button onclick="exportResponsesAsCSV()">Export All Responses as CSV</button>
    <div id="count"></div>
    <div id="responses"></div>

    <script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-app-compat.js"></script>
    <script src="https://www.gstatic.com/firebasejs/9.22.0/firebase-database-compat.js"></script>
    <script src="firebase-config.js"></script>
    <script>
        initializeFirebase();

        // Display count
        getResponsesCount().then(count => {
            document.getElementById('count').innerHTML = `<h2>Total Responses: ${count}</h2>`;
        });

        // Display responses
        getAllResponses().then(data => {
            const responsesDiv = document.getElementById('responses');
            responsesDiv.innerHTML = `<pre>${JSON.stringify(data, null, 2)}</pre>`;
        });
    </script>
</body>
</html>
```

## Troubleshooting

### "Permission denied" error
- Check that your database rules allow writing to `responses`
- Make sure you're in test mode during development

### "Firebase not initialized"
- Verify your config values are correct
- Check browser console for errors
- Make sure Firebase scripts load before your config file

### Data not saving
- Open browser console and check for errors
- Verify your database URL is correct
- Check Firebase Console to see if data appears there

## Cost & Limits

Firebase Realtime Database free tier includes:
- **1 GB stored data**
- **10 GB/month downloaded**
- **100 simultaneous connections**

This should be more than enough for a questionnaire with a few hundred responses.

## Next Steps

1. Set up Firebase Authentication for admin access
2. Create admin dashboard for easy data viewing
3. Set up automated exports or analytics
4. Configure proper security rules for production
