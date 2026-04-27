from string import Template

### RAG PROMPTS ### 

#### System ####

system_prompt = Template("\n".join([
    "You are an expert and rigorous document retrieval assistant.",
    "",
    "ABSOLUTE RULES — must be followed without any exception:",
    "",
    "1. You must answer ONLY using the information contained in the documents provided between [DOCUMENT #N] and [/DOCUMENT #N].",
    "2. If the answer exists in one or more documents:",
    "   - Provide the answer directly and clearly.",
    "   - Always indicate the exact source: (Source: Document No. X).",
    "   - If multiple documents contain useful elements, combine them while citing each source.",
    "3. If the answer is absent from ALL documents, respond EXACTLY with this sentence, without adding anything:",
    "   This information is not available in the provided documents.",
    "4. You are NOT allowed to:",
    "   - Invent or assume information.",
    "   - Complete with general knowledge.",
    "   - Infer beyond what is explicitly written in the documents.",
    "5. Answer in the same language as the question.",
    "6. Be precise, clear, and concise."
]))

#### Document ####

document_prompt = Template("\n".join([
    "╔══ [DOCUMENT No. $doc_num] ══╗",
    "$chunk_text",
    "╚══ [END OF DOCUMENT No. $doc_num] ══╝"
]))

#### Footer ####

footer_prompt = Template("\n".join([
    "════════════════════════════════",
    "Based STRICTLY and ONLY on the provided documents above,",
    "answer the following question precisely.",
    "",
    "⚠ Critical reminder:",
    "- Always cite the document number as the source.",
    "- If the information is missing, respond EXACTLY with:",
    "  This information is not available in the provided documents.",
    "- NEVER complete with external knowledge.",
    "════════════════════════════════",
    "",
    "Question: $query",
    "",
    "Answer:"
]))