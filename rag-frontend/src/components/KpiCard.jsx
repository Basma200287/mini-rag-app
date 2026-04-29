// src/components/KpiCard.jsx
export default function KpiCard({ label, value, badge, badgeType }) {
  const colors = {
    green: "bg-emerald-50 text-emerald-600",
    red:   "bg-red-50 text-red-500",
    purple:"bg-indigo-50 text-indigo-600",
  };
  return (
    <div className="bg-white rounded-2xl p-5 border border-gray-100 shadow-sm hover:shadow-md transition-shadow">
      <p className="text-xs text-gray-400 font-medium mb-1">{label}</p>
      <p className="text-2xl font-semibold text-gray-800 mb-2">{value}</p>
      <span className={`text-[11px] font-medium px-2.5 py-1 rounded-full ${colors[badgeType]}`}>
        {badge}
      </span>
    </div>
  );
}