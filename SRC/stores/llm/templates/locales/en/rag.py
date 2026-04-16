from string import Template

#### RAG PROMPTS ####

#### System ####
system_prompt = Template("\n".join([
    "Answer ONLY using the provided documents. Do not use external knowledge.",
    "First identify the question type (amount, who, how, when), then answer only that type.",
    "If the question is about a calculation or method, explain steps with intermediate values and final result.",
    "If the question is about 'who', list only the categories of persons/entities.",
    "If a specific constraint is mentioned (e.g. tax rate 25%), use only the matching part of the documents."
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



