export default function HomePage() {
  return (
    <div className="space-y-8">
      {/* Overview Header */}
      <div className="bg-slate-900/60 border border-slate-800 rounded-lg p-6 flex flex-col md:flex-row md:items-center md:justify-between gap-4">
        <div>
          <h2 className="text-xl font-bold text-slate-100">Telemetry Ingestion &amp; Overview</h2>
          <p className="text-sm text-slate-400 mt-1">
            Endpoint collection status, normalized event pipeline, and system health.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <div className="px-3 py-1.5 bg-slate-800/80 border border-slate-700/60 rounded text-xs text-slate-300">
            Phase 1 Scaffolding Ready
          </div>
        </div>
      </div>

      {/* Metrics Row */}
      <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
        <div className="bg-slate-900/40 border border-slate-800/80 rounded-lg p-5">
          <span className="text-xs uppercase font-medium text-slate-400 tracking-wider">Total Endpoints</span>
          <div className="text-2xl font-bold text-white mt-2">0</div>
          <span className="text-xs text-slate-500 mt-1 block">Awaiting enrollment</span>
        </div>
        <div className="bg-slate-900/40 border border-slate-800/80 rounded-lg p-5">
          <span className="text-xs uppercase font-medium text-slate-400 tracking-wider">Active Collectors</span>
          <div className="text-2xl font-bold text-emerald-400 mt-2">0</div>
          <span className="text-xs text-slate-500 mt-1 block">0 offline</span>
        </div>
        <div className="bg-slate-900/40 border border-slate-800/80 rounded-lg p-5">
          <span className="text-xs uppercase font-medium text-slate-400 tracking-wider">Events Today</span>
          <div className="text-2xl font-bold text-blue-400 mt-2">0</div>
          <span className="text-xs text-slate-500 mt-1 block">Normalized via schema</span>
        </div>
        <div className="bg-slate-900/40 border border-slate-800/80 rounded-lg p-5">
          <span className="text-xs uppercase font-medium text-slate-400 tracking-wider">Database Status</span>
          <div className="text-2xl font-bold text-slate-200 mt-2">SQLite</div>
          <span className="text-xs text-slate-500 mt-1 block">Storage ready</span>
        </div>
      </div>

      {/* Event Pipeline Architecture Card */}
      <div className="bg-slate-900/40 border border-slate-800/80 rounded-lg p-6">
        <h3 className="text-base font-semibold text-slate-200 mb-3">Pipeline Flow</h3>
        <div className="grid grid-cols-1 md:grid-cols-5 gap-3 text-center text-xs">
          <div className="p-3.5 bg-slate-800/40 border border-slate-700/50 rounded-lg">
            <span className="font-semibold text-slate-200 block mb-1">1. Windows Host</span>
            <span className="text-slate-400">Winevt / Security Log (4624, 4625, 4688)</span>
          </div>
          <div className="p-3.5 bg-slate-800/40 border border-slate-700/50 rounded-lg">
            <span className="font-semibold text-slate-200 block mb-1">2. Collector Agent</span>
            <span className="text-slate-400">Normalization &amp; Local JSONL Queue</span>
          </div>
          <div className="p-3.5 bg-slate-800/40 border border-slate-700/50 rounded-lg">
            <span className="font-semibold text-slate-200 block mb-1">3. HTTPS / FastAPI</span>
            <span className="text-slate-400">Token Auth &amp; Server-side ID Resolution</span>
          </div>
          <div className="p-3.5 bg-slate-800/40 border border-slate-700/50 rounded-lg">
            <span className="font-semibold text-slate-200 block mb-1">4. SQLite Store</span>
            <span className="text-slate-400">Indexed Common Event Schema</span>
          </div>
          <div className="p-3.5 bg-slate-800/40 border border-slate-700/50 rounded-lg">
            <span className="font-semibold text-slate-200 block mb-1">5. Next.js Dashboard</span>
            <span className="text-slate-400">Real-time Telemetry &amp; Event Analysis</span>
          </div>
        </div>
      </div>
    </div>
  );
}
