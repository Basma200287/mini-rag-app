// src/pages/Documents.jsx
const docs = [
  { name: "Rapport_Q4_2024.pdf",   meta: "2.4 MB · 342 chunks · il y a 2 jours", status: "Indexé",     pill: "bg-emerald-50 text-emerald-600", icon: "📄", iconBg: "bg-red-50"    },
  { name: "Guide_utilisateur.docx",meta: "1.1 MB · en cours · il y a 10 min",     status: "Processing", pill: "bg-amber-50 text-amber-600",    icon: "📝", iconBg: "bg-blue-50"   },
  { name: "KPIs_dashboard.xlsx",   meta: "800 KB · 97 chunks · il y a 5 jours",   status: "Indexé",     pill: "bg-emerald-50 text-emerald-600", icon: "📊", iconBg: "bg-green-50"  },
];

export default function Documents({ setView }) {
  return (
    <>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-xl font-semibold text-gray-800">Mes documents</h1>
        <button onClick={() => setView("upload")} className="bg-indigo-600 text-white px-4 py-2 rounded-xl text-sm font-medium shadow-sm hover:bg-indigo-700 transition">
          + Ajouter
        </button>
      </div>
      <div className="flex flex-col gap-3">
        {docs.map(doc => (
          <div key={doc.name} className="bg-white border border-gray-100 rounded-2xl p-4 flex items-center gap-4 shadow-sm hover:shadow-md transition cursor-pointer">
            <div className={`w-10 h-10 rounded-xl grid place-items-center text-xl ${doc.iconBg}`}>{doc.icon}</div>
            <div className="flex-1">
              <p className="text-sm font-medium text-gray-800">{doc.name}</p>
              <p className="text-xs text-gray-400 mt-0.5">{doc.meta}</p>
            </div>
            <span className={`text-xs font-medium px-3 py-1 rounded-full ${doc.pill}`}>{doc.status}</span>
          </div>
        ))}
      </div>
    </>
  );
}