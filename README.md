# InnerWorks Web SDK Demo

Demo application for testing the InnerWorks Web SDK (@innerworks-me/iw-auth-sdk) for device fingerprinting and metrics collection.

## Features

- Device fingerprinting and metrics collection
- Automatic user ID construction from user details
- Real-time metrics sending to InnerWorks API
- Beautiful UI with response visualization
- TypeScript support

## Project Structure

```
innerworks-web-sdk/
├── src/
│   ├── App.tsx          # Main demo application
│   ├── App.css          # Styling
│   ├── main.tsx         # Application entry point
│   └── index.css        # Global styles
├── package.json         # Dependencies and scripts
└── vite.config.ts       # Vite configuration
```

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn

### Installation

```bash
npm install
```

### Development

Start the development server:

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### Build

Build for production:

```bash
npm run build
```

Preview production build:

```bash
npm run preview
```

## Usage

The demo app allows you to test the InnerWorks SDK by:

1. **Fill in required fields:**
   - Device Name (e.g., MacbookProIntel)
   - Browser Name (e.g., Chrome)

2. **User ID is auto-constructed** in the format:
   ```
   {email}_{name}_{deviceName}_{browserName}
   ```

   Email and Name are pre-configured:
   - Email: `abubakr.hbai@gmail.com`
   - Name: `Abubakr`

3. **Click "Send Metrics"** to send device fingerprinting data to the InnerWorks API

4. **View the response** including:
   - Result status (success/partial/error)
   - Request ID
   - Detection results (JWT)
   - Errors (if any)

## API Configuration

The demo uses:
- **Project ID:** `e9933f85-5b08-4f08-ad98-4f8213d26eae`
- **API Endpoint:** `https://api.dev.innerworks.me/api/v1`
- **Metrics Endpoint:** `https://api.dev.innerworks.me/api/v1/innerworks/metrics`

## Response Format

The SDK sends data in the following format:

```json
{
  "project_id": "e9933f85-5b08-4f08-ad98-4f8213d26eae",
  "user_id": "abubakr.hbai@gmail.com_Abubakr_MacbookProIntel_Chrome",
  "sdk_type": "Web",
  "alg": "gcm",
  "detection_types": {
    "fingerprinting": { "enabled": true },
    "vpn": { "enabled": true },
    "botdetection": { "enabled": false }
  },
  "flow_id": "019b6320-17f6-7c4b-b305-5edec1d675a8",
  "metrics": { ... }
}
```

## Dependencies

- **React 19** - UI framework
- **TypeScript** - Type safety
- **Vite** - Build tool
- **@innerworks-me/iw-auth-sdk** - InnerWorks SDK for metrics collection

## License

ISC
