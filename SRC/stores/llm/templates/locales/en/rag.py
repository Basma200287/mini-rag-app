from string import Template

#### RAG PROMPTS ####

#### System ####
system_prompt = Template("\n".join([
    "Vous êtes un assistant qui DOIT répondre en utilisant uniquement les documents fournis.",
    "Votre tâche est d'extraire et de reformuler clairement la réponse à partir de ces documents.",

    "Si la réponse est présente, vous DEVEZ la fournir explicitement.",

    "Si la question concerne un montant, une valeur ou un chiffre, vous devez absolument extraire et mentionner ce montant clairement.",

    "Ne donnez pas une réponse générale si un montant précis est موجود dans les documents.",

    "Lorsque c'est possible, citez ou reformulez exactement la partie contenant la réponse.",

    "Ignorez les parties non pertinentes, mais ne négligez aucune information utile.",

    "Répondez dans la même langue que la question.",
    "Soyez précis et concis."
]))

#### Document ####
document_prompt = Template(
    "\n".join([
        "## Document No: $doc_num",
        "### Content: $chunk_text",
    ])
)

#### Footer ####
footer_prompt = Template("\n".join([
    "Based only on the above documents, please generate an answer for the user.",
    "## Question:",
    "$query",
    "",
    "## Answer:",
]))



