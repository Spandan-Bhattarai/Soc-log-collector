import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "SOC Log Collector | SOCUaTrace",
  description: "Endpoint security event collection and defensive analysis platform",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="dark">
      <body className="antialiased min-h-screen bg-[#0b0f17] text-slate-100 flex flex-col">
        <header className="border-b border-slate-800 bg-[#0f172a]/80 backdrop-blur px-6 py-4 flex items-center justify-between sticky top-0 z-50">
          <div className="flex items-center space-x-3">
            <div className="w-8 h-8 rounded bg-blue-600 flex items-center justify-center font-bold text-white tracking-wider text-sm">
              SOC
            </div>
            <div>
              <h1 className="text-base font-semibold text-white leading-none">
                SOC Log Collector
              </h1>
              <span className="text-xs text-slate-400">SOCUaTrace Family &bull; Project 1</span>
            </div>
          </div>
          <div className="flex items-center space-x-4 text-xs text-slate-400">
            <span className="inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full bg-emerald-950/60 text-emerald-400 border border-emerald-800/50">
              <span className="w-1.5 h-1.5 rounded-full bg-emerald-400"></span>
              Platform Active
            </span>
          </div>
        </header>
        <main className="flex-1 max-w-7xl w-full mx-auto p-6">{children}</main>
        <footer className="border-t border-slate-800/80 px-6 py-4 text-center text-xs text-slate-500">
          SOC Log Collector &mdash; Defensive Endpoint Telemetry &amp; Analysis
        </footer>
      </body>
    </html>
  );
}
