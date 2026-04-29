// src/components/PipelineSteps.jsx
const steps = ["⬆️ Upload", "⚙️ Processing", "🔍 Indexation", "✅ Terminé"];

export default function PipelineSteps({ currentStep }) {
  // currentStep: 0=idle, 1=upload, 2=processing, 3=indexing, 4=done
  return (
    <div className="flex gap-3 mt-5">
      {steps.map((label, i) => {
        const stepNum = i + 1;
        const isDone   = stepNum < currentStep;
        const isActive = stepNum === currentStep;
        return (
          <div key={label} className={`flex-1 rounded-xl px-3 py-3 text-center text-xs font-medium border transition-all ${
            isDone   ? "border-emerald-300 bg-emerald-50 text-emerald-600" :
            isActive ? "border-indigo-400 bg-indigo-50 text-indigo-600"   :
                       "border-gray-200 bg-white text-gray-400"
          }`}>
            {label}
          </div>
        );
      })}
    </div>
  );
}