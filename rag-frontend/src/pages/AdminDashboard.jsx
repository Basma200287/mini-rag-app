import { useEffect, useState } from 'react';
import { getIndexInfo, uploadDocument,
         processDocuments, indexDocuments } from '../api/rag';

// Dans le composant :
const [info, setInfo] = useState(null);

useEffect(() => {
  getIndexInfo().then(({ data }) => setInfo(data));
}, []);

// Affichage :
// info.num_documents → nombre de documents
// info.num_chunks    → nombre de chunks
// info.last_updated  → dernière mise à jour
// (adaptez selon votre réponse réelle)


const [file, setFile] = useState(null);
const [status, setStatus] = useState('');

const runPipeline = async () => {
  if (!file) return;
  setStatus('Envoi du fichier...');

  // Étape 1 : upload
  const form = new FormData();
  form.append('file', file);
  await uploadDocument(form);
  setStatus('Traitement des chunks...');

  // Étape 2 : processing
  await processDocuments();
  setStatus('Indexation vectorielle...');

  // Étape 3 : indexation
  await indexDocuments();
  setStatus('Terminé !');
};

// JSX :
// <input type="file" onChange={e => setFile(e.target.files[0])} />
// <button onClick={runPipeline}>Lancer le pipeline</button>
// <p>{status}</p>