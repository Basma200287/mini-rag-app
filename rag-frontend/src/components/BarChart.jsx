// src/components/BarChart.jsx
const data = [
  { day: "Lun", val: 320 },
  { day: "Mar", val: 410 },
  { day: "Mer", val: 390 },
  { day: "Jeu", val: 510 },
  { day: "Ven", val: 470 },
  { day: "Sam", val: 180 },
  { day: "Dim", val: 290 },
];

export default function BarChart() {
  const max = Math.max(...data.map(d => d.val));
  return (
    <div className="bg-white rounded-2xl p-6 border border-gray-100 shadow-sm">
      <p className="text-sm font-semibold text-gray-800 mb-5">Requêtes par jour (7 derniers jours)</p>
      <div className="flex items-end gap-2 h-28">
        {data.map(({ day, val }, i) => (
          <div key={day} className="flex-1 flex flex-col items-center gap-1">
            <div
              className={`w-full rounded-t-md transition-opacity hover:opacity-70 cursor-pointer ${
                i === 3 ? "bg-indigo-600" : "bg-indigo-300"
              }`}
              style={{ height: `${(val / max) * 100}%` }}
            />
            <span className="text-[10px] text-gray-400">{day}</span>
          </div>
        ))}
      </div>
    </div>
  );
}