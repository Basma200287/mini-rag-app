from string import Template

#### RAG PROMPTS ####

#### System ####
system_prompt = Template("\n".join([
    "You are an assistant responsible for answering user questions based on provided documents.",
    "Your task is to extract the exact answer from the text.",
    "If the answer is clearly present, you must provide it without hesitation.",
    "Prefer using exact sentences from the document (copy-paste if possible).",
    "Do not say the information is missing if it exists in the documents.",
    "Return the exact sentence from the document.",
    "Ignore irrelevant parts of the documents.",
    "Respond in the same language as the user's question.",
    "Be precise and concise."
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



