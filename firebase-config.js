// Firebase configuration for EKO project (eko1-4e)
// IMPORTANT: Replace the placeholder values with your actual credentials
// Get these from: https://console.firebase.google.com/u/0/project/eko1-4e/settings/general

const firebaseConfig = {
    apiKey: "AIzaSyBEYWPBzS4wLfPZVDGrof9YcMMdK83b8i4",
    authDomain: "eko1-4e.firebaseapp.com",
    projectId: "eko1-4e",
    storageBucket: "eko1-4e.firebasestorage.app",
    messagingSenderId: "433555664638",
    appId: "1:433555664638:web:768fb8a3e1e9fc01f8bfaf",
    databaseURL: "https://eko1-4e-default-rtdb.firebaseio.com"
};

// Initialize Firebase
let db;
let responsesRef;

function initializeFirebase() {
    try {
        // Initialize Firebase
        firebase.initializeApp(firebaseConfig);

        // Initialize Realtime Database
        db = firebase.database();
        responsesRef = db.ref('responses');

        console.log('Firebase initialized successfully');
        return true;
    } catch (error) {
        console.error('Error initializing Firebase:', error);
        return false;
    }
}

// Save responses to Firebase
async function saveToDatabase(responseData) {
    if (!responsesRef) {
        console.warn('Firebase not initialized. Saving locally only.');
        return false;
    }

    try {
        // Generate a unique ID for this response
        const newResponseRef = responsesRef.push();

        // Save the data
        await newResponseRef.set({
            ...responseData,
            submittedAt: firebase.database.ServerValue.TIMESTAMP,
            id: newResponseRef.key
        });

        console.log('Response saved to database with ID:', newResponseRef.key);
        return newResponseRef.key;
    } catch (error) {
        console.error('Error saving to database:', error);
        return false;
    }
}

// Retrieve all responses (for admin/analysis purposes)
async function getAllResponses() {
    if (!responsesRef) {
        console.error('Firebase not initialized');
        return null;
    }

    try {
        const snapshot = await responsesRef.once('value');
        return snapshot.val();
    } catch (error) {
        console.error('Error retrieving responses:', error);
        return null;
    }
}

// Get responses count
async function getResponsesCount() {
    if (!responsesRef) {
        return 0;
    }

    try {
        const snapshot = await responsesRef.once('value');
        return snapshot.numChildren();
    } catch (error) {
        console.error('Error getting count:', error);
        return 0;
    }
}

// Export responses as CSV for analysis
async function exportResponsesAsCSV() {
    const allResponses = await getAllResponses();

    if (!allResponses) {
        console.error('No responses to export');
        return;
    }

    // Convert to array
    const responsesArray = Object.values(allResponses);

    if (responsesArray.length === 0) {
        alert('No responses to export yet!');
        return;
    }

    // Get all unique keys from all responses
    const allKeys = new Set();
    responsesArray.forEach(response => {
        Object.keys(response).forEach(key => allKeys.add(key));
    });

    // Create CSV header
    const headers = Array.from(allKeys).sort();
    let csv = headers.join(',') + '\n';

    // Create CSV rows
    responsesArray.forEach(response => {
        const row = headers.map(header => {
            const value = response[header];
            // Handle arrays and objects
            if (Array.isArray(value)) {
                return `"${value.join('; ')}"`;
            } else if (typeof value === 'object') {
                return `"${JSON.stringify(value)}"`;
            } else if (typeof value === 'string' && value.includes(',')) {
                return `"${value}"`;
            }
            return value || '';
        });
        csv += row.join(',') + '\n';
    });

    // Download CSV
    const blob = new Blob([csv], { type: 'text/csv' });
    const url = URL.createObjectURL(blob);
    const link = document.createElement('a');
    link.href = url;
    link.download = `eko-responses-${new Date().toISOString().split('T')[0]}.csv`;
    link.click();
    URL.revokeObjectURL(url);
}
