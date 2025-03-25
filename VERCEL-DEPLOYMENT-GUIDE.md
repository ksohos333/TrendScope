# TrendScope Deployment Guide for Vercel

Based on the video transcript, here's a step-by-step guide to deploy your TrendScope application to Vercel.

## Step 1: Set Up .gitignore

First, create or update your `.gitignore` file to exclude environment variables:

```
# .gitignore
node_modules/
.env
.env.local
python/__pycache__/
```

## Step 2: Replace Localhost URLs with Environment Variables

Search for all instances of localhost URLs in your codebase and replace them with environment variables:

1. Use `Ctrl+Shift+F` (or `Cmd+Shift+F` on Mac) to search for "localhost" in your project
2. Replace all instances of `http://localhost:3000` or similar with environment variables like `${process.env.NEXT_PUBLIC_API_URL}`

## Step 3: Create Vercel Configuration Files

### For the Backend (Python API)

Create a `vercel.json` file in the root directory:

```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

### For the Frontend (Next.js)

Create a `vercel.json` file in the frontend directory (if you're using a monorepo structure):

```json
{
  "rewrites": [
    {
      "source": "/(.*)",
      "destination": "/index.html"
    }
  ]
}
```

## Step 4: Check Package Versions

If you encounter deployment failures, check your package versions. Some packages might need to be downgraded for compatibility with Vercel:

```json
// Example package.json fix
"dependencies": {
  "cloudinary": "1.37.3"  // Downgraded from 2.x.x
}
```

## Step 5: Push to Git

1. Commit your changes to Git:
   ```bash
   git add .
   git commit -m "Prepare for Vercel deployment"
   git push
   ```

## Step 6: Deploy Backend to Vercel

1. Go to [vercel.com](https://vercel.com) and log in
2. Click on "Add New" > "Project"
3. Import your Git repository
4. Set the framework preset to "Other"
5. Set the root directory to your backend directory (if using a monorepo)
6. Add all your environment variables:
   - `JWT_SECRET` (if applicable)
   - `FRONTEND_URL` (leave empty for now, we'll update it later)
   - Add all other environment variables from your `.env` file
7. Click "Deploy"

## Step 7: Deploy Frontend to Vercel

1. Go to [vercel.com](https://vercel.com) and click on "Add New" > "Project"
2. Import the same Git repository
3. Set the framework preset to your frontend framework (e.g., "Next.js")
4. Set the root directory to your frontend directory (if using a monorepo)
5. Add your environment variables:
   - `NEXT_PUBLIC_API_URL` = `https://your-backend-url.vercel.app` (use the URL from Step 6)
6. Click "Deploy"

## Step 8: Update Backend Environment Variables

1. Go back to your backend project in Vercel
2. Go to "Settings" > "Environment Variables"
3. Update the `FRONTEND_URL` with your frontend URL: `https://your-frontend-url.vercel.app`
4. Save changes
5. Go to "Deployments" and click "Redeploy" to apply the new environment variables

## Troubleshooting

If you encounter issues:

1. **Check Vercel Logs**: Go to your project > Deployments > Latest deployment > View Logs
2. **Environment Variables**: Ensure all environment variables are correctly set
3. **CORS Issues**: Make sure your backend allows requests from your frontend domain
4. **API Routes**: Verify that your API routes are correctly configured in `vercel.json`
5. **Package Versions**: Some packages might need version adjustments for Vercel compatibility

## Next Steps

Once your application is deployed:

1. Test all functionality to ensure everything works as expected
2. Set up a custom domain if needed (in Vercel project settings)
3. Configure automatic deployments from your Git repository
