TradeBot — Developer Documentation



1\. Project Overview



TradeBot is a paper-trading dashboard that analyzes selected NSE stocks and generates trading signals using a Simple Moving Average (SMA) strategy.



The project has two main parts:



Frontend: Next.js dashboard



Backend: FastAPI REST API



The frontend gets stock analysis data from the backend and displays the current price, SMA 20, SMA 50, and trading signal.



2\. Technology Used



Frontend



Next.js 16



React



TypeScript



Tailwind CSS



Vercel



Backend



Python 3



FastAPI



Uvicorn



pandas



yfinance



Render



Version Control



Git



GitHub



3\. Project Structure



trading\_agent/

├── backend/

│   ├── config.py

│   ├── main.py

│   ├── market\_data.py

│   ├── strategy.py

│   ├── engine.py

│   ├── logger.py

│   ├── paper\_trade.py

│   ├── report.py

│   └── requirements.txt

│

├── frontend/

│   ├── app/

│   │   └── page.tsx

│   ├── package.json

│   └── ...

│

├── docs/

│   ├── DEVELOPER.md

│   └── USER.md

│

└── README.md



4\. Trading Algorithm



The project uses a Moving Average strategy.



SMA 20: 20-period simple moving average



SMA 50: 50-period simple moving average



The strategy compares the short-term moving average with the long-term moving average and generates a configured BUY, SELL, or HOLD signal.



The strategy implementation is located in:



backend/strategy.py



5\. Configured Stocks



The current stock list is maintained in:



backend/config.py



Current symbols:



RELIANCE.NS

TCS.NS

INFY.NS

HDFCBANK.NS

ICICIBANK.NS



6\. Backend API



Health Check



GET /health



Example response:



{

&#x20; "status": "ok"

}



Stock Analysis



GET /api/stocks



The endpoint returns:



Stock symbol



Current/latest available price



SMA 20



SMA 50



Trading signal



Scan Endpoint



POST /api/scan



This returns the same stock analysis through a POST endpoint.



7\. Local Backend Setup



From the backend directory:



python -m venv .venv

.venv\\Scripts\\Activate.ps1

pip install -r requirements.txt

uvicorn main:app --reload --port 8000



Local API:



http://127.0.0.1:8000



API documentation:



http://127.0.0.1:8000/docs



8\. Local Frontend Setup



From the frontend directory:



npm install

npm run dev



Local frontend:



http://localhost:3000



9\. Deployment



Frontend — Vercel



The Next.js frontend is connected to the GitHub repository and deployed from the main branch.



Production URL:



https://trading-agent-nf7b.vercel.app/



Deployment flow:



GitHub

&#x20;  ↓

main branch

&#x20;  ↓

Vercel

&#x20;  ↓

Next.js build

&#x20;  ↓

Production frontend



Backend — Render



The FastAPI backend is deployed as a Render Web Service.



Production URL:



https://trading-agent-kvj8.onrender.com/



Stocks API:



https://trading-agent-kvj8.onrender.com/api/stocks



Deployment flow:



GitHub

&#x20;  ↓

main branch

&#x20;  ↓

Render Web Service

&#x20;  ↓

Python dependencies

&#x20;  ↓

Uvicorn

&#x20;  ↓

FastAPI production API



Render start command:



uvicorn main:app --host 0.0.0.0 --port $PORT



10\. Frontend–Backend Connection



The frontend requests stock data from the Render backend:



https://trading-agent-kvj8.onrender.com/api/stocks



The backend allows cross-origin requests using FastAPI CORS middleware.



This allows the Vercel frontend to communicate with the Render backend.



11\. Requirements



Backend dependencies are listed in:



backend/requirements.txt



The project uses packages such as:



fastapi

uvicorn

pandas

yfinance



The frontend dependencies are listed in:



frontend/package.json



12\. GitHub Workflow



The project is maintained using Git.



Typical workflow:



git add .

git commit -m "Your change description"

git push origin main



After pushing to main:



Vercel can automatically deploy frontend changes.



Render can automatically deploy backend changes.



13\. Production URLs



Frontend



https://trading-agent-nf7b.vercel.app/



Backend



https://trading-agent-kvj8.onrender.com/



Stock API



https://trading-agent-kvj8.onrender.com/api/stocks



GitHub Repository



https://github.com/Hariprasath308/trading-agent



14\. Important Notes



This is a paper-trading and educational project.



It does not place real stock-market orders.



Market-data availability depends on the external data provider.



Render's free service may sleep when inactive, so the first request after inactivity can take longer.



API keys and other secrets should never be committed to GitHub.



15\. Developer Summary



Frontend  → Next.js → Vercel

Backend   → FastAPI → Render

Data      → yfinance

Analysis  → pandas + SMA 20/SMA 50

Source    → GitHub

Trading   → Paper Trading only

