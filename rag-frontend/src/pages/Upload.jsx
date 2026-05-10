export default function Upload() {
  return (
    <div className="p-6">
      <h1 className="text-xl font-semibold">📤 Upload Documents</h1>
      <p className="text-gray-500 mt-2">
        Drop your files here to index them in the RAG system.
      </p>

      <div className="mt-6 border-2 border-dashed p-10 rounded-xl text-center text-gray-400">
        Drag & Drop or Click to Upload
      </div>
    </div>
  );
}