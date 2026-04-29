import Sidebar    from "./components/Sidebar";
import KpiCard    from "./components/KpiCard";
import BarChart   from "./components/BarChart";
import Documents  from "./pages/Documents";
import Upload     from "./pages/Upload";

export default function AdminDashboard() {
  const [view, setView] = useState("dashboard");
  // ... ton state existant

  return (
    <div className="flex h-screen bg-gray-50 font-sans">
      <Sidebar view={view} setView={setView} />
      <main className="flex-1 overflow-y-auto p-8">
        {view === "dashboard" && <DashboardView />}
        {view === "documents" && <Documents setView={setView} />}
        {view === "upload"    && <Upload />}
        {view === "config"    && <Config />}
      </main>
    </div>
  );
}