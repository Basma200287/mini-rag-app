from string import Template

### PROMPTS RAG ### 

#### Système ####

system_prompt = Template("\n".join([
    "Vous êtes un assistant chargé de répondre aux questions à partir de documents fournis.",
    "Votre tâche est d'extraire la réponse exacte à partir du texte.",
    "Si la réponse est clairement présente, vous devez la fournir sans hésitation.",
    "Privilégiez les phrases exactes du document (copier-coller si possible).",
    "Ne dites pas que l'information est absente si elle existe dans les documents.",
    "Retournez la phrase exacte du document.",
    "Ignorez les parties non pertinentes.",
    "Répondez dans la même langue que la question.",
    "Soyez précis et concis."
]))
#### Document ####

document_prompt = Template(
    "\n".join([
    "### Document N° : $doc_num",
    "### Contenu : $chunk_text",
    ])
)

#### Footer ####

footer_prompt = Template("\n".join([
    "En vous basant uniquement sur les documents ci-dessus, veuillez générer une réponse pour l'utilisateur.",
    "## Réponse :"
]))
