// src/components/Sidebar.jsx
export default function Sidebar({ view, setView }) {
  const navItem = (label, icon, key) => (
    <div
      onClick={() => setView(key)}
      className={`flex items-center gap-3 px-3 py-2.5 rounded-xl cursor-pointer text-sm transition-all ${
        view === key
          ? "bg-indigo-600 text-white shadow-md shadow-indigo-200"
          : "text-gray-400 hover:bg-indigo-50 hover:text-indigo-600"
      }`}
    >
      <span className="w-5 text-center">{icon}</span>
      {label}
    </div>
  );

  return (
    <div className="w-56 bg-white border-r border-gray-100 flex flex-col p-5 gap-1 shrink-0">
      {/* Logo */}
      <div className="flex items-center gap-3 pb-6 px-1">
        <div className="w-8 h-8 bg-indigo-600 rounded-lg grid place-items-center text-white text-sm">🧠</div>
        <div>
          <p className="font-semibold text-sm text-gray-800">KnowledgeBase</p>
          <p className="text-[10px] uppercase tracking-widest text-gray-400">Admin Panel</p>
        </div>
      </div>

      <p className="text-[10px] font-semibold uppercase tracking-widest text-gray-400 px-2 pb-1">Tableau de bord</p>
      {navItem("KPI & Métriques", "📊", "dashboard")}

      <p className="text-[10px] font-semibold uppercase tracking-widest text-gray-400 px-2 pb-1 pt-4">Documents</p>
      {navItem("Mes documents", "📁", "documents")}
      {navItem("Ajouter un document", "⬆️", "upload")}

      <p className="text-[10px] font-semibold uppercase tracking-widest text-gray-400 px-2 pb-1 pt-4">Système</p>
      {navItem("Configuration", "⚙️", "config")}
    </div>
  );
}