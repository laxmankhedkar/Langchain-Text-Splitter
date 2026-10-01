# LangChain Text Splitter

A hands-on repository for learning and implementing **Text Splitting and Chunking in LangChain**.

This repository demonstrates different approaches to splitting large documents into smaller chunks before passing them to **embeddings, vector databases, and RAG applications**.

The examples use a deep learning curriculum PDF to demonstrate different text-splitting strategies.

---

## 📌 What is Text Splitting?

Large documents are usually too long to send directly to an LLM or store efficiently as individual embedding vectors.

**Text splitting** breaks a large document into smaller, meaningful pieces called **chunks**.

A typical RAG pipeline looks like:

```text
Document
   ↓
Text Splitting
   ↓
Chunks
   ↓
Embeddings
   ↓
Vector Database
   ↓
Retriever
   ↓
LLM
   ↓
Answer
```

For example:

```text
Large Document
      ↓
 ┌────┼────┬────┐
 ↓    ↓    ↓    ↓
Chunk 1  Chunk 2  Chunk 3  Chunk 4
```

Each chunk can then be converted into an embedding and stored in a vector database.

---

# 📂 Repository Structure

```text
Langchain-Text-Splitter/
│
├── dl-curriculum.pdf
│
├── document_structured_based.py
├── length_based.py
├── semantic_meaning_based.py
└── text_structure_based.py
```

---

# 🔹 Text Splitting Approaches

This repository covers four important approaches:

1. Length-Based Splitting
2. Text Structure-Based Splitting
3. Document Structure-Based Splitting
4. Semantic Meaning-Based Splitting

---

# 1. Length-Based Splitting

File:

```text
length_based.py
```

Length-based splitting divides text according to a specified size such as the number of characters or tokens.

### Basic idea

```text
Large Text
    ↓
Fixed Size
    ↓
┌────────┬────────┬────────┬────────┐
│Chunk 1 │Chunk 2 │Chunk 3 │Chunk 4 │
└────────┴────────┴────────┴────────┘
```

For example, a document can be divided into chunks of a specific size with an overlap between consecutive chunks.

### Example

```text
Chunk Size = 500
Chunk Overlap = 50
```

The overlap helps preserve context between neighboring chunks.

### Advantages

* Simple
* Fast
* Easy to implement
* Useful for large amounts of text

### Limitation

A fixed-size split may break a sentence, paragraph, or concept in the middle.

---

# 2. Text Structure-Based Splitting

File:

```text
text_structure_based.py
```

Text structure-based splitting uses the natural structure of text to create chunks.

Instead of splitting text at arbitrary positions, the splitter can consider separators such as:

```text
Paragraph
   ↓
Sentence
   ↓
Word
```

A common approach is to use hierarchical separators.

For example:

```text
Paragraph
    ↓
New Line
    ↓
Sentence
    ↓
Word
```

This helps maintain more meaningful chunks.

### Advantages

* Preserves text structure
* Better readability
* Useful for general documents
* Commonly used in RAG pipelines

---

# 3. Document Structure-Based Splitting

File:

```text
document_structured_based.py
```

Document structure-based splitting uses the structure of a particular document format.

Different documents have different structures.

For example:

```text
PDF
 ├── Page
 ├── Section
 ├── Heading
 ├── Paragraph
 └── Table
```

A structured document can therefore be divided according to its logical sections rather than simply using a fixed character count.

### Example

```text
Deep Learning
     ↓
Neural Networks
     ↓
CNN
     ↓
RNN
     ↓
Transformers
```

This can help preserve the relationship between related information.

---

# 4. Semantic Meaning-Based Splitting

File:

```text
semantic_meaning_based.py
```

Semantic splitting focuses on the **meaning of the text** rather than only its size or formatting.

The goal is to keep sentences or passages with similar meanings together.

For example:

```text
Sentence 1 ─┐
Sentence 2 ─┤
            ├──→ Chunk 1
Sentence 3 ─┘

Sentence 4 ─┐
Sentence 5 ─┤
            └──→ Chunk 2
```

The split is determined based on semantic similarity between sections of text.

### Advantages

* Can preserve meaningful context
* Useful for knowledge-heavy documents
* Can improve retrieval quality in some RAG applications

### Limitation

Semantic splitting can require additional processing and may be more computationally expensive than simple rule-based splitting.

---

# 📄 Example Document

The repository includes:

```text
dl-curriculum.pdf
```

This PDF is used to experiment with the different text-splitting approaches.

The same source document can be processed using different strategies to understand how chunking affects the final output.

---

# 🔄 Text Splitting in RAG

Text splitting is an important preprocessing step in a RAG system.

A typical workflow is:

```text
                 PDF / Document
                       ↓
                Document Loader
                       ↓
                 Text Splitter
                       ↓
                  Text Chunks
                       ↓
                  Embeddings
                       ↓
                 Vector Store
                       ↓
                   Retriever
                       ↓
                  Relevant Chunks
                       ↓
                     Prompt
                       ↓
                      LLM
                       ↓
                   Final Answer
```

For example, when a user asks:

```text
"What is backpropagation?"
```

the retriever searches the stored chunk embeddings and returns the chunks that are most relevant to the question.

---

# 🎯 Why Chunking Matters

The quality of chunks can directly affect retrieval quality.

### Poor chunking

```text
Concept A ──────┐
                │
                ├── Broken Chunk
                │
Concept B ──────┘
```

Important context may be separated.

### Better chunking

```text
Concept A
   ↓
Related Explanation
   ↓
Example
   ↓
Complete Chunk
```

The goal is to create chunks that contain enough context to be useful while remaining small enough for efficient retrieval.

---

# 📏 Chunk Size and Chunk Overlap

Two important concepts in text splitting are:

### Chunk Size

The maximum size of a chunk.

```text
Chunk Size = 500
```

means that the splitter attempts to create chunks around that size, depending on the splitting strategy.

### Chunk Overlap

The amount of text shared between consecutive chunks.

```text
Chunk 1
████████████████
        ████████
        Chunk 2
```

For example:

```text
Chunk Size = 500
Chunk Overlap = 50
```

Overlap helps prevent important information from being lost at chunk boundaries.

---

# 🛠️ Technologies Used

* Python
* LangChain
* Text Splitting
* Document Processing
* Semantic Chunking
* RAG Concepts
* Embeddings
* Vector Databases

---

# ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/laxmankhedkar/Langchain-Text-Splitter.git
```

### 2. Navigate to the project

```bash
cd Langchain-Text-Splitter
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install langchain
```

Depending on the implementation and LangChain version, additional packages may be required.

---

# ▶️ Running the Examples

### Length-Based Splitting

```bash
python length_based.py
```

### Text Structure-Based Splitting

```bash
python text_structure_based.py
```

### Document Structure-Based Splitting

```bash
python document_structured_based.py
```

### Semantic Meaning-Based Splitting

```bash
python semantic_meaning_based.py
```

---

# 🎯 Learning Objectives

After working through this repository, you should understand:

* What text splitting is
* Why documents need to be split
* What a chunk is
* Chunk size
* Chunk overlap
* Length-based splitting
* Structure-based splitting
* Document-aware splitting
* Semantic splitting
* How chunking affects RAG
* How chunks are used with embeddings
* How chunks are stored in vector databases

---

# 💡 Key Takeaway

There is no single chunking strategy that works perfectly for every document.

The appropriate strategy depends on:

* Document type
* Document structure
* Content complexity
* Retrieval requirements
* Chunk size
* Context requirements
* Embedding model
* RAG use case

A good RAG pipeline therefore starts with understanding the data and choosing a suitable chunking strategy.

---

# 🚀 Possible Future Improvements

Some useful additions to this repository could include:

* Recursive Character Text Splitter
* Token-based splitting
* Markdown splitting
* HTML splitting
* Python code splitting
* Language-aware splitting
* Parent-child chunking
* Contextual chunking
* Semantic chunking with embeddings
* Chunk quality comparison
* Retrieval evaluation
* ChromaDB integration
* FAISS integration
* Complete RAG implementation

---

# 👨‍💻 Author

**Laxman Khedkar**

Data Scientist & ML Engineer
Python | SQL | Machine Learning | NLP | LLMs | RAG | Generative AI

GitHub: [@laxmankhedkar](https://github.com/laxmankhedkar)

---

## ⭐ About This Repository

This repository is part of my hands-on learning journey with **LangChain and Generative AI**.

The goal is to understand how different text-splitting strategies work and how they fit into real-world **RAG and LLM applications**.

If you find this repository useful, feel free to ⭐ the repository and explore the examples.
