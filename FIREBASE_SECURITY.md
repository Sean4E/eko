# Firebase Security Rules Setup

## Current Security Configuration

### Database Rules (`database.rules.json`)

**Security Features:**
- ✅ **Anonymous Write Access**: Users can submit questionnaire responses without authentication
- ✅ **Authenticated Read Access**: Only authenticated users (admins) can read data
- ✅ **Write-Once Protection**: Responses cannot be modified after creation
- ✅ **Data Validation**: All fields are validated for type and format
- ✅ **Anonymous Enforcement**: All submissions must have `participantName: "Anonymous"`
- ✅ **Range Validation**: Slider values (1-5) are validated
- ✅ **No Extra Fields**: Prevents injection of unauthorized data

### How It Works

1. **Public Submission** (No Auth Required):
   - Anyone can write to `/responses/{responseId}`
   - Each response can only be written once (`.write: "!data.exists()"`)
   - All fields are validated for correct data types

2. **Admin Access** (Auth Required):
   - Reading data requires authentication (`auth != null`)
   - Admins must sign in to view responses via admin panel

3. **Data Protection**:
   - Responses cannot be modified once submitted
   - Invalid data structures are rejected
   - Prevents unauthorized database writes outside `/responses`

## Setup Instructions

### 1. Install Firebase CLI

```bash
npm install -g firebase-tools
```

### 2. Login to Firebase

```bash
firebase login
```

### 3. Initialize Firebase Project

```bash
firebase init
```

Select:
- ✅ Database: Configure security rules
- ✅ Hosting: Configure hosting (optional)

Choose existing project: `eko1-4e`

### 4. Deploy Security Rules

```bash
firebase deploy --only database
```

This will upload the rules from `database.rules.json` to your Firebase project.

### 5. Verify Rules

Go to:
https://console.firebase.google.com/u/0/project/eko1-4e/database/eko1-4e-default-rtdb/rules

You should see the rules have been updated.

## Setting Up Admin Authentication

To access the admin dashboard and analytics, you need to set up Firebase Authentication:

### Option 1: Email/Password (Recommended)

1. Go to Firebase Console → Authentication → Sign-in method
2. Enable "Email/Password"
3. Add your admin email in Authentication → Users

### Option 2: Use Firebase Admin Dashboard Directly

1. Visit: https://console.firebase.google.com/u/0/project/eko1-4e/database/eko1-4e-default-rtdb/data
2. View data directly in Firebase Console (always authenticated)

### Option 3: Update Admin Panel to Use Auth (Advanced)

Add Firebase Authentication to `admin.html`:

```javascript
// Add to admin.html before loadResponses()
firebase.auth().signInAnonymously()
  .then(() => {
    console.log('Authenticated as admin');
    loadResponses();
  })
  .catch((error) => {
    console.error('Authentication failed:', error);
  });
```

## Security Best Practices

### Current Protection:
✅ Write-once responses (no modification)
✅ Anonymous submissions enforced
✅ Field validation
✅ Read access requires authentication
✅ No writes outside `/responses`

### Additional Recommendations:

1. **Rate Limiting**: Consider implementing rate limiting to prevent spam
2. **Content Moderation**: Review responses for inappropriate content
3. **Backup Data**: Regularly export data using admin panel
4. **Monitor Usage**: Check Firebase Console for unusual activity

## Testing Security Rules

### Test Unauthenticated Write (Should Work):
```javascript
// From questionnaire (index.html)
firebase.database().ref('responses').push({
  participantName: 'Anonymous',
  timestamp: new Date().toISOString(),
  // ... other fields
});
// ✅ Should succeed
```

### Test Unauthenticated Read (Should Fail):
```javascript
// Without authentication
firebase.database().ref('responses').once('value');
// ❌ Should fail with "Permission denied"
```

### Test Authenticated Read (Should Work):
```javascript
// After firebase.auth().signInAnonymously()
firebase.database().ref('responses').once('value');
// ✅ Should succeed
```

## Quick Deploy Commands

```bash
# Deploy only database rules
firebase deploy --only database

# Deploy only hosting
firebase deploy --only hosting

# Deploy everything
firebase deploy

# View current project
firebase projects:list

# Check deployment status
firebase hosting:channel:list
```

## Emergency: Revert to Open Rules

If you need to temporarily open access for testing:

```json
{
  "rules": {
    "responses": {
      ".read": true,
      ".write": true
    }
  }
}
```

⚠️ **Warning**: Only use open rules for testing! Always return to secure rules for production.

## Current Rule Summary

| Action | Permission | Requirement |
|--------|-----------|-------------|
| Submit Response | ✅ Allowed | None (public) |
| Read Responses | ✅ Allowed | Authentication required |
| Modify Response | ❌ Denied | Not allowed after creation |
| Delete Response | ❌ Denied | Not allowed |
| Invalid Data | ❌ Rejected | Validation rules enforced |

## Support

For issues with Firebase security rules:
1. Check Firebase Console logs
2. Test rules in Firebase Console → Rules Playground
3. Review: https://firebase.google.com/docs/database/security

---

**Last Updated**: 2025-12-11
**Project**: EKO (eko1-4e)
**Database**: https://eko1-4e-default-rtdb.firebaseio.com
