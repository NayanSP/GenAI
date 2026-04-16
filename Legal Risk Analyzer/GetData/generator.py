from langchain_openai import ChatOpenAI
from langchain_classic.output_parsers import OutputFixingParser
from GetData.reteriver import RetrieverClass


class Generator:
    print('Generator begins')
    def __init__(self, model="gpt-4o-mini", temperature=0):
        print('Generator initialization')
        self.llm = ChatOpenAI(
            model=model,
            temperature=temperature
        )
        self.retriever = RetrieverClass()

    def generate(self, prompt, parser=None, mode="Answer"):
        query = ""
        print('Generate the context')
        # 🔹 Adjust retrieval based on mode
        if mode in ["Summary", "Risk Analysis"]:
            k = 8
        else:
            k = 3

        # 🔹 Step 1: Retrieve documents
        docs = self.retriever.get_documents(query, k)

        # 🔹 Step 2: Build context
        context = "\n\n".join([doc.page_content for doc in docs])

        # 🔹 Step 3: Format prompt
        final_prompt = prompt.format(
            context=context,
            question=query,
            format_instructions=parser.get_format_instructions() if parser else ""
        )

        # 🔹 Step 4: LLM call
        response = self.llm.invoke(final_prompt)
        text = response.content

        # 🔹 Step 5: Parse output
        if parser:
            try:
                return parser.parse(text)
            except Exception:
                fixing_parser = OutputFixingParser.from_llm(
                    parser=parser,
                    llm=self.llm
                )
                return fixing_parser.parse(text)

        return text