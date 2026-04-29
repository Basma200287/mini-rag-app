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

    // Ajouter message user
    setMessages(prev => [
      ...prev,
      { role: 'user', text: question }
    ]);

    setLoading(true);

    try {
      const response = await askQuestion(question);

      console.log("API RESPONSE:", response.data);

      setMessages(prev => [
        ...prev,
        {
          role: 'bot',
          text: response.data?.answer || "Pas de réponse disponible"
        }
      ]);

    } catch (err) {
      console.error("API ERROR:", err.response?.data || err.message);

      setMessages(prev => [
        ...prev,
        {
          role: 'bot',
          text: err.response?.data?.signal
            ? `Erreur: ${err.response.data.signal}`
            : "Erreur serveur ou connexion impossible"
        }
      ]);

    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto' }}>

      {/* Messages */}
      <div style={{ minHeight: '300px', padding: '10px' }}>
        {messages.map((m, i) => (
          <div
            key={i}
            style={{
              textAlign: m.role === 'user' ? 'right' : 'left',
              margin: '8px 0'
            }}
          >
            <span
              style={{
                display: 'inline-block',
                padding: '8px 12px',
                borderRadius: '10px',
                background: m.role === 'user' ? '#d1e7ff' : '#eee'
              }}
            >
              {m.text}
            </span>
          </div>
        ))}

        {loading && (
          <div style={{ textAlign: 'left', color: 'gray' }}>
            Recherche en cours...
          </div>
        )}
      </div>

      {/* Input */}
      <div style={{ display: 'flex', gap: '8px' }}>
        <input
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => e.key === 'Enter' && send()}
          placeholder="Votre question..."
          style={{
            flex: 1,
            padding: '10px',
            border: '1px solid #ccc',
            borderRadius: '6px'
          }}
        />

        <button
          onClick={send}
          disabled={loading}
          style={{
            padding: '10px 16px',
            cursor: 'pointer'
          }}
        >
          Envoyer
        </button>
      </div>

    </div>
  );
}