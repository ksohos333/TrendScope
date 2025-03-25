# TrendScope - AI News Analysis Platform

TrendScope is an AI-driven news platform that uses Bayesian probability to synthesize non-biased news articles, find connections between global events, and make market predictions using fractal market theory.

## Project Overview

This platform combines advanced AI techniques with data visualization to provide users with:

- Unbiased news analysis across multiple sources
- Geopolitical risk assessment and visualization
- Market trend predictions based on news sentiment
- Multi-dimensional analysis of global events

## Technology Stack

- **Frontend**: Next.js, React 18, TypeScript, Tailwind CSS
- **Backend**: Node.js, Python
- **Data Visualization**: D3.js, Mapbox GL, React Simple Maps
- **AI/ML**: Bayesian analysis, Fractal analysis
- **Deployment**: Vercel

## Project Structure

```
├── app/                    # Next.js app directory
│   ├── api/                # API routes
│   ├── components/         # React components
│   ├── lib/                # Utility functions
│   └── pages/              # Page components
├── public/                 # Static assets
├── python/                 # Python analysis modules
├── database/               # Database schemas and migrations
├── trendscope/             # Core TrendScope module
└── ai-news-platform/       # Alternative implementation
```

## Development Environment Setup

### Prerequisites

- Node.js v22.14.0 or later
- Python 3.10 or later
- npm or yarn

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/trendscope.git
   cd trendscope
   ```

2. Install JavaScript dependencies:
   ```
   npm install
   ```

3. Install Python dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```
   cp .env.example .env.local
   ```
   Edit `.env.local` with your API keys and configuration.

### Running the Development Server

```
npm run dev
```

The application will be available at http://localhost:3000.

### Scripts

- `npm run dev` - Start the development server
- `npm run build` - Build the production application
- `npm run start` - Start the production server
- `npm run lint` - Run ESLint
- `npm run lint:fix` - Fix ESLint issues
- `npm run type-check` - Run TypeScript type checking
- `npm run format` - Format code with Prettier
- `npm run clean` - Clean build directories
- `npm run test` - Run tests
- `npm run test:watch` - Run tests in watch mode
- `npm run vercel-build` - Build for Vercel deployment
- `npm run analyze` - Analyze bundle size

## Deployment

The application is configured for deployment on Vercel. The `vercel.json` file contains the necessary configuration.

To deploy:

```
vercel
```

For production deployment:

```
vercel --prod
```

## Contributing

1. Ensure you're using the correct Node.js version (see `.nvmrc`)
2. Follow the code style guidelines
3. Write tests for new features
4. Update documentation as needed

## License

ISC
