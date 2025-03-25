# TrendScope Deployment Plan

## Current Architecture Issues

The current TrendScope architecture has several issues that prevent successful deployment on Vercel:

1. **Python Process Spawning**: The application uses `child_process.spawn()` to run Python scripts directly from Next.js API routes, which is not supported in Vercel's serverless environment.

2. **Heavy Python Dependencies**: The requirements.txt includes libraries like numpy, pandas, scipy, scikit-learn, and transformers, which exceed Vercel's function size limits.

3. **Database Dependencies**: The application requires PostgreSQL, MongoDB, and Redis, which need separate hosting.

4. **Worker Processes**: The application uses background worker processes for job queues, which cannot run in Vercel's stateless environment.

## Proposed Solution

We'll restructure the application into a modern microservices architecture:

### 1. Frontend (Vercel)
- Deploy the Next.js frontend to Vercel
- Convert API routes to call external API endpoints instead of spawning Python processes

### 2. Backend API (Separate Service)
- Create a FastAPI or Flask service for the Python backend
- Deploy to a platform that supports Python (e.g., Heroku, Railway, or a custom server)
- Expose REST API endpoints that the frontend can call

### 3. Database Services
- Use managed database services:
  - PostgreSQL: Supabase, Neon, or AWS RDS
  - MongoDB: MongoDB Atlas
  - Redis: Upstash or Redis Labs

### 4. Worker Processes
- Deploy worker processes to a platform that supports background jobs
- Options include Heroku workers, AWS Lambda, or a custom server

## Implementation Steps

### Step 1: Restructure the Frontend

1. Create a new Next.js project with the following structure:
```
trendscope-frontend/
├── app/
│   ├── api/
│   │   └── proxy/ (proxy routes to backend API)
│   ├── components/
│   ├── lib/
│   │   └── api-client.ts (replace python-bridge.ts)
│   └── pages/
├── public/
└── package.json
```

2. Create an API client to replace the Python bridge:

```typescript
// lib/api-client.ts
export class ApiClient {
  private baseUrl: string;
  
  constructor() {
    this.baseUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';
  }
  
  async callMethod(endpoint: string, data: any): Promise<any> {
    const response = await fetch(`${this.baseUrl}/${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(data),
    });
    
    if (!response.ok) {
      throw new Error(`API error: ${response.statusText}`);
    }
    
    return response.json();
  }
}
```

3. Update API routes to use the API client instead of the Python bridge.

### Step 2: Create a Backend API Service

1. Create a new Python project with FastAPI:
```
trendscope-api/
├── app/
│   ├── main.py
│   ├── routers/
│   │   ├── bayesian.py
│   │   ├── fractal.py
│   │   └── multidimensional.py
│   ├── models/
│   └── services/
│       ├── bayesian_service.py
│       ├── fractal_service.py
│       └── multidimensional_service.py
├── requirements.txt
└── Procfile (for Heroku deployment)
```

2. Implement the API endpoints that match the frontend's expectations.

3. Deploy the API service to a platform that supports Python.

### Step 3: Set Up Database Services

1. Create managed database instances for PostgreSQL, MongoDB, and Redis.

2. Update the backend API to connect to these managed services.

### Step 4: Set Up Worker Processes

1. Create a separate worker service for background jobs.

2. Deploy the worker service to a platform that supports background jobs.

## Vercel Configuration

1. Create a new Vercel project for the frontend.

2. Set up environment variables in Vercel:
```
NEXT_PUBLIC_API_URL=https://your-backend-api.herokuapp.com
```

3. Deploy the frontend to Vercel.

## Conclusion

This architecture separates concerns and allows each component to be deployed to the most appropriate platform. The frontend can be deployed to Vercel, while the backend services can be deployed to platforms that better support Python and stateful operations.
