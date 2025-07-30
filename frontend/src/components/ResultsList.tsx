export default function ResultsList({ results }: { results: any[] }) {
  if (!results.length) return null;

  return (
    <div className="max-w-3xl mx-auto mt-8 space-y-4">
      <h3 className="text-xl font-bold">Results</h3>
      {results.map((res, i) => (
        <div key={i} className="p-4 bg-gray-100 rounded shadow">
          <h4 className="font-semibold text-blue-800">{res.name}</h4>
          <p className="text-green-600 font-medium">Score: {res.score}/100</p>
          <p className="mt-2 text-gray-700 whitespace-pre-line">{res.explanation}</p>
        </div>
      ))}
    </div>
  );
}
