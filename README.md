# Offline Library Management System

## Project Overview

LibrarySync is a comprehensive library management system designed to function fully offline while offering seamless synchronization capabilities when connectivity is restored. The application enables librarians and users to manage book collections, track borrowing/returning processes, and maintain library operations even without an internet connection. It leverages modern web technologies to provide a responsive, reliable experience in various connectivity scenarios.

## Key Features

### Offline Functionality
- **Complete Offline Access**: Full library management capabilities without internet connection
- **Offline Check-in/Check-out**: Process book borrowing and returns even when offline
- **Local Search and Filtering**: Advanced search capabilities for books, members, and transactions
- **Barcode Scanning Support**: Works offline for quick book or member identification

### Synchronization
- **Background Sync**: Automatic data synchronization when connection is restored
- **Conflict Resolution**: Smart merging of offline changes with server data
- **Sync Status Indicators**: Clear visual indicators of synchronization status
- **Prioritized Sync**: Critical data syncs first when connection is limited

### Data Management
- **Book Catalog**: Comprehensive book metadata management including titles, authors, genres, ISBN
- **Member Management**: Track member information, borrowing history, and account status
- **Circulation Tracking**: Monitor book checkouts, returns, reservations, and due dates
- **Fine Calculation**: Automatic calculation of overdue fines (works offline)
- **Reports and Analytics**: Usage statistics and library operation insights

## Technologies Used

### Frontend
- **HTML5/CSS3/JavaScript**: Core web technologies
- **Progressive Web App (PWA)**: For offline capabilities and installable experience
- **Service Workers**: Enable offline functionality and background synchronization
- **IndexedDB**: Client-side storage for offline data persistence in browsers
- **Workbox**: For service worker management and offline caching strategies

### Backend
- **Node.js**: Server-side JavaScript runtime
- **Express.js**: Web application framework
- **SQLite**: Local database for desktop application variant
- **RESTful API**: For client-server communication

### Data Storage & Sync
- **IndexedDB**: Browser-based database for web client offline storage
- **SQLite**: Embedded database for local storage in desktop variants
- **Sync Adapters**: Custom middleware for handling data synchronization
- **JWT**: For secure authentication across online/offline states

### Development Tools
- **Webpack**: Module bundling and build optimization
- **Babel**: JavaScript compiler for compatibility
- **ESLint**: Code quality and consistency
- **Jest**: Testing framework
- **Electron**: (Optional) For desktop application packaging

## System Architecture

LibrarySync follows a hybrid architecture designed for resilience and offline capabilities:

1. **Client Tier**
   - Progressive Web App interface with responsive design
   - Service Workers for intercepting network requests and enabling offline functionality
   - IndexedDB for client-side data storage and offline operations
   - Background sync registration for deferred server updates

2. **Synchronization Layer**
   - Queue-based sync system for tracking offline changes
   - Timestamp-based conflict resolution strategies
   - Differential sync to minimize data transfer
   - Prioritization system for critical data synchronization

3. **Server Tier**
   - RESTful API endpoints for CRUD operations
   - Authentication and authorization services
   - Master database for centralized data when online
   - Sync controllers to handle client reconciliation

4. **Deployment Options**
   - Cloud-hosted central server
   - Local network server for institutional deployment
   - Standalone mode for completely offline operations

## Data Model

### Core Collections/Tables

**books**
- `id`: Unique identifier
- `title`: Book title
- `author`: Book author(s)
- `isbn`: ISBN number
- `publishDate`: Publication date
- `category`: Book category/genre
- `description`: Book description
- `location`: Physical location in library
- `status`: Available, checked out, reserved, etc.
- `coverImage`: Book cover image (stored as path or blob)

**members**
- `id`: Unique identifier
- `name`: Member name
- `email`: Contact email
- `phone`: Contact phone
- `membershipDate`: Date of joining
- `membershipStatus`: Active, expired, suspended
- `borrowingLimit`: Maximum books allowed

**transactions**
- `id`: Unique identifier
- `bookId`: Reference to book
- `memberId`: Reference to member
- `checkoutDate`: Date of checkout
- `dueDate`: Expected return date
- `returnDate`: Actual return date (null if not returned)
- `fineAmount`: Fine for late returns
- `status`: Transaction status
- `syncStatus`: Indicates if transaction is synced with server

**syncQueue**
- `id`: Unique operation identifier
- `operation`: Create, update, delete
- `entityType`: Books, members, transactions
- `entityId`: ID of the affected entity
- `changeData`: Data payload of the change
- `timestamp`: When the change occurred
- `priority`: Sync priority level
- `attempts`: Number of sync attempts
- `status`: Pending, completed, failed

## Setup Instructions

### Prerequisites
- Node.js (v14 or higher)
- npm (v6 or higher)
- Modern web browser (for PWA support)

### Installation

1. Clone the repository
   ```
   git clone https://github.com/yourusername/library-sync.git
   cd library-sync
   ```

2. Install dependencies
   ```
   npm install
   ```

3. Configure environment variables
   ```
   cp .env.example .env
   ```
   Edit the `.env` file to match your environment

4. Initialize the database
   ```
   npm run init-db
   ```

5. Start the development server
   ```
   npm run dev
   ```

6. Access the application
   - Web app: http://localhost:3000
   - For offline capability, open the app once while online to cache necessary resources

### Building for Production
```
npm run build
```

### Project Structure
```
library-sync/
├── client/                     # Frontend code
│   ├── public/                 # Static assets
│   ├── src/
│   │   ├── components/         # React components
│   │   ├── pages/              # Page components
│   │   ├── services/           # API and sync services
│   │   ├── utils/              # Utility functions
│   │   ├── hooks/              # Custom React hooks
│   │   ├── context/            # React context providers
│   │   ├── serviceWorker.js    # Service worker configuration
│   │   └── App.js              # Main App component
│   └── package.json            # Frontend dependencies
├── server/                     # Backend code
│   ├── controllers/            # Request handlers
│   ├── models/                 # Data models
│   ├── routes/                 # API routes
│   ├── services/               # Business logic services
│   ├── utils/                  # Utility functions
│   ├── db/                     # Database setup and migrations
│   ├── middleware/             # Express middleware
│   ├── sync/                   # Synchronization logic
│   └── server.js               # Server entry point
├── tests/                      # Unit and integration tests
├── .env.example                # Example environment variables
├── README.md                   # Project documentation
└── package.json                # Project dependencies
```

## Contributing

Contributions to LibrarySync are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow the established code style (enforced by ESLint)
- Write tests for new functionality
- Update documentation for any changed features
- Ensure all tests pass before submitting PR
- Consider offline functionality for all features

### Bug Reports
If you find a bug, please create an issue with:
- Detailed description of the problem
- Steps to reproduce
- Expected behavior
- Screenshots if applicable
- Environment information (browser, OS, device)


