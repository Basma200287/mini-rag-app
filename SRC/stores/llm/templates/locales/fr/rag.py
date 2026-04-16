from string import Template

### PROMPTS RAG ### 

#### Système ####

system_prompt = Template("\n".join([
    "Répondez UNIQUEMENT en utilisant les documents fournis. N'utilisez aucune connaissance externe.",
    "Identifiez d'abord le type de question (montant, qui, comment, quand), puis répondez uniquement à ce type.",
    "Si la question porte sur un calcul ou une méthode, expliquez les étapes avec les valeurs intermédiaires et le résultat final.",
    "Si la question porte sur 'qui', listez uniquement les catégories de personnes ou d'entités.",
    "Si une contrainte spécifique est mentionnée (par exemple un taux d'imposition de 25 %), utilisez uniquement la partie des documents correspondant à cette contrainte."
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
