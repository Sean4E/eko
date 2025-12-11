# EKO - Embodied Kinetic Orchestra

An interactive questionnaire designed to gather insights for an immersive art installation combining movement, sound, visuals, and AR.

🌐 **Live Site**: [https://sean4e.github.io/eko](https://sean4e.github.io/eko)

## About

EKO is a participatory design tool that helps shape an immersive experience. Through thoughtful questions, we collect ideas about:

- 🌟 Personal myths and their cultural significance
- 💫 Emotional experiences and preferences
- 🕺 Movement and interaction styles
- 🎵 Sound and music preferences
- 👁️ Visual and AR design choices
- 💭 Themes and meanings
- 🕯️ Personal and cultural rituals

## Features

- **Interactive Questionnaire**: 20 carefully crafted questions
- **Real-time Progress Tracking**: Visual progress bar showing completion
- **Database Integration**: Firebase backend to store all responses
- **Data Export**: Download responses as JSON or CSV
- **Responsive Design**: Works on desktop and mobile devices
- **Beautiful UI**: Glassmorphic design with animated backgrounds

## Local Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/Sean4E/eko.git
   cd eko
   ```

2. Open `index.html` in a web browser

3. (Optional) Set up Firebase for database storage:
   - Follow instructions in [FIREBASE_SETUP.md](FIREBASE_SETUP.md)
   - Update `firebase-config.js` with your credentials

## Firebase Database Setup

To store user responses in a database:

1. Create a Firebase project at [console.firebase.google.com](https://console.firebase.google.com)
2. Enable Realtime Database
3. Update `firebase-config.js` with your project credentials
4. Deploy to GitHub Pages

See [FIREBASE_SETUP.md](FIREBASE_SETUP.md) for detailed instructions.

## Deployment

This site is configured to deploy automatically to GitHub Pages:

1. Push your code to the `main` branch
2. Go to repository Settings → Pages
3. Set source to "Deploy from a branch"
4. Select `main` branch and `/ (root)` folder
5. Click Save

Your site will be available at: `https://sean4e.github.io/eko`

## Project Structure

```
eko/
├── index.html              # Main questionnaire page
├── firebase-config.js      # Firebase configuration (update with your credentials)
├── FIREBASE_SETUP.md      # Firebase setup guide
└── README.md              # This file
```

## Technologies Used

- **HTML5** - Structure and markup
- **CSS3** - Styling with glassmorphism effects
- **Vanilla JavaScript** - Interactive functionality
- **Firebase** - Realtime database for storing responses
- **GitHub Pages** - Free hosting

## Data Collection

User responses include:

- Myth creation and cultural significance
- Emotional preferences
- Movement and interaction styles
- Sound/music preferences (with custom input)
- Visual design preferences
- Thematic interests
- Personal and cultural rituals
- Participant name (optional)
- Timestamp

All data is stored securely in Firebase Realtime Database.

## Viewing Responses

### Method 1: Firebase Console
View responses directly in the Firebase Console under Realtime Database.

### Method 2: Export to CSV
Use the `exportResponsesAsCSV()` function in browser console to download all responses.

### Method 3: Admin Dashboard
Create a separate admin page to view and analyze responses (see FIREBASE_SETUP.md).

## Privacy

- Participant names are optional
- All responses are stored securely in Firebase
- Data is used solely for designing the EKO installation
- No personal identifying information is collected

## Contributing

This is a research project for the EKO art installation. If you have suggestions or find issues, please open an issue or submit a pull request.

## License

© 2025 EKO Project. All rights reserved.

## Contact

For questions about this project, please reach out through GitHub issues.

---

Built with ❤️ for the EKO - Embodied Kinetic Orchestra installation
