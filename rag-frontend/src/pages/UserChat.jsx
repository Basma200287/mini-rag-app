import { useState } from 'react';
import { askQuestion } from '../api/rag';

export default function UserChat() {
  const [messages, setMessages] = useState([
    { role: 'bot', text: 'Bonjour ! Posez-moi une question.' }
  ]);
  const [input, setInput] = useState('');
  const [loading, setLoading] = useState(false);

  const send = async () => {
    if (!input.trim() || loading) return;
    const question = input.trim();
    setInput('');
    setMessages(prev => [...prev, { role: 'user', text: question }]);
    setLoading(true);

    try {
      const { data } = await askQuestion(question);
      // Adaptez "data.answer" selon la structure de votre réponse API
      setMessages(prev => [...prev, { role: 'bot', text: data.answer }]);
    } catch (err) {
      setMessages(prev => [...prev, {
        role: 'bot', text: 'Erreur de connexion au serveur.'
      }]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      {/* Liste des messages */}
      {messages.map((m, i) => (
        <div key={i} className={m.role}>{m.text}</div>
        ))}
      {loading && <div>Recherche en cours...</div>}

      {/* Zone de saisie */}
      <input
        value={input}
        onChange={e => setInput(e.target.value)}
        onKeyDown={e => e.key === 'Enter' && send()}
        placeholder="Votre question..."
      />
      <button onClick={send} disabled={loading}>Envoyer</button>
    </div>
  );
}