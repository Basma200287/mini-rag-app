from string import Template

### PROMPTS RAG ### 

#### Système ####

system_prompt = Template("\n".join([

"Vous êtes un assistant chargé de générer une réponse pour l'utilisateur.",           
"Un ensemble de documents associés à la requête de l'utilisateur vous sera fourni.",
"Vous devez générer une réponse basée sur les documents fournis.", 
"Ignorer les documents qui ne sont pas pertinents pour la requête de l'utilisateur.",
"Vous pouvez vous excuser auprès de l'utilisateur si vous n'êtes pas en mesure de générer une réponse.",
"Vous devez générer la réponse dans la même langue que la requête de l'utilisateur."
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