"use client";

import { useEffect, useState } from "react";

type Stock = {
  stock: string;
  price: number | null;
  sma20: number | null;
  sma50: number | null;
  signal: string;
};

export default function Home() {
  const [stocks, setStocks] = useState<Stock[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch("https://trading-agent-kvj8.onrender.com/api/stocks")
      .then((res) => {
        if (!res.ok) throw new Error("Backend request failed");
        return res.json();
      })
      .then((data) => {
        setStocks(data.stocks || []);
        setLoading(false);
      })
      .catch(() => {
        setError("Backend connection failed");
        setLoading(false);
      });
  }, []);

  return (
    <main className="min-h-screen bg-black text-white p-8">
      <div className="max-w-6xl mx-auto">
        <h1 className="text-4xl font-bold">TradeBot</h1>

        <p className="mt-2 text-gray-400">
          Paper Trading Dashboard
        </p>

        {loading && (
          <p className="mt-8 text-yellow-400">
            Loading market data...
          </p>
        )}

        {error && (
          <p className="mt-8 text-red-400">
            {error}
          </p>
        )}

        {!loading && !error && (
          <div className="mt-8 overflow-x-auto">
            <table className="w-full border border-gray-800">
              <thead>
                <tr className="border-b border-gray-800">
                  <th className="p-4 text-left">Stock</th>
                  <th className="p-4 text-left">Price</th>
                  <th className="p-4 text-left">SMA 20</th>
                  <th className="p-4 text-left">SMA 50</th>
                  <th className="p-4 text-left">Signal</th>
                </tr>
              </thead>

              <tbody>
                {stocks.map((item) => (
                  <tr
                    key={item.stock}
                    className="border-b border-gray-900"
                  >
                    <td className="p-4">{item.stock}</td>
                    <td className="p-4">{item.price ?? "N/A"}</td>
                    <td className="p-4">{item.sma20 ?? "N/A"}</td>
                    <td className="p-4">{item.sma50 ?? "N/A"}</td>
                    <td className="p-4">{item.signal}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        )}
      </div>
    </main>
  );
}