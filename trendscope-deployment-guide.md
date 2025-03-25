# TrendScope Deployment Guide

This guide explains how to deploy the TrendScope application using a microservices architecture that separates the frontend and backend components.

## Project Structure

The application is split into two main components:

1. **Frontend (Next.js)** - Deployed on Vercel
2. **Backend API (FastAPI)** - Deployed on Heroku or similar platform

### Directory Structure

```
trendscope/
├── trendscope-frontend/     # Next.js frontend
│   ├── app/                 # Next.js app directory
│   │   ├── api/             # API routes (proxy to backend)
│   │   └── ...              # Pages and components
│   ├── lib/                 # Utility functions
│   │   └── api-client.ts    # API client for backend
│   ├── package.json         # Frontend dependencies
│   └── vercel.json          # Vercel configuration
│
└── trendscope-api/          # FastAPI backend
    ├── app/                 # FastAPI app directory
    │   ├── main.py          # Main FastAPI application
    │   ├── routers/         # API route handlers
    │   └── services/        # Business logic
    ├── requirements.txt     # Python dependencies
    └── Procfile             # Heroku configuration
```

## Deployment Steps

### 1. Deploy the Backend API

1. Create a new Heroku application:
   ```bash
   cd trendscope-api
   heroku create trendscope-api
   ```

2. Add PostgreSQL, MongoDB, and Redis add-ons:
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   heroku addons:create mongolab:sandbox
   heroku addons:create heroku-redis:hobby-dev
   ```

3. Deploy the application:
   ```bash
   git push heroku main
   ```

4. Note the URL of your deployed API (e.g., `https://trendscope-api.herokuapp.com`).

### 2. Deploy the Frontend

1. Create a new Vercel project:
   ```bash
   cd trendscope-frontend
   vercel
   ```

2. Set up environment variables in Vercel:
   - Go to the Vercel dashboard
   - Navigate to your project settings
   - Add the following environment variable:
     ```
     NEXT_PUBLIC_API_URL=https://trendscope-api.herokuapp.com
     ```

3. Deploy to production:
   ```bash
   vercel --prod
   ```

## Configuration

### Backend API Configuration

The backend API requires the following environment variables:

- `DATABASE_URL`: PostgreSQL connection string
- `MONGODB_URI`: MongoDB connection string
- `REDIS_URL`: Redis connection string
- `SECRET_KEY`: Secret key for JWT tokens

These are automatically set by Heroku when you add the respective add-ons.

### Frontend Configuration

The frontend requires the following environment variables:

- `NEXT_PUBLIC_API_URL`: URL of the backend API

## Local Development

### Running the Backend API

1. Install dependencies:
   ```bash
   cd trendscope-api
   pip install -r requirements.txt
   ```

2. Set up environment variables:
   ```bash
   export DATABASE_URL=postgresql://localhost:5432/trendscope
   export MONGODB_URI=mongodb://localhost:27017/trendscope
   export REDIS_URL=redis://localhost:6379
   export SECRET_KEY=your_secret_key
   ```

3. Run the API:
   ```bash
   uvicorn main:app --reload
   ```

### Running the Frontend

1. Install dependencies:
   ```bash
   cd trendscope-frontend
   npm install
   ```

2. Set up environment variables:
   ```bash
   echo "NEXT_PUBLIC_API_URL=http://localhost:8000" > .env.local
   ```

3. Run the development server:
   ```bash
   npm run dev
   ```

## Troubleshooting

### Common Issues

1. **CORS Errors**: Ensure that the backend API has CORS configured to allow requests from the frontend domain.

2. **Environment Variables**: Double-check that all required environment variables are set correctly.

3. **API Connection**: Verify that the frontend can connect to the backend API by checking the network requests in the browser developer tools.

4. **Deployment Logs**: Check the deployment logs in Vercel and Heroku for any errors.

## Conclusion

This deployment architecture separates the frontend and backend components, allowing each to be deployed to the most appropriate platform. The frontend is deployed to Vercel, which is optimized for Next.js applications, while the backend is deployed to Heroku, which provides better support for Python applications and stateful services.
