# 🌍 Claudestay

**Claudestay** is an intelligent hotel information assistant powered by the **Claude Opus 3** Large Language Model (LLM). It allows users to ask natural language queries about hotels worldwide and receive accurate, contextual answers along with audio playback. The system combines **web scraping**, **vector databases**, **retrieval-augmented generation (RAG)**, and a **Streamlit interface** to create a smooth and interactive user experience.

---

## 🚀 Features

* Supports hotel data from **112 countries**
* Extracted fields include:

  * Hotel name
  * Check-in & check-out times
  * Lowest nightly rate
  * Hotel class
  * Overall & location ratings
  * Nearby places and distances
* Uses **SerpAPI** for data scraping
* Vector search powered by **FAISS**
* Integrated with **LangChain** for document handling
* Query processing via **Claude Opus 3 LLM**
* Audio output for answers
* 🖥Built using **Streamlit** for user interface

---

## Tech Stack

| Component     | Technology           |
| ------------- | -------------------- |
| LLM           | Claude Opus 3        |
| Data Scraping | SerpAPI              |
| Vector DB     | FAISS                |
| RAG Framework | LangChain            |
| UI            | Streamlit            |
| Audio Output  | Text-to-Speech (TTS) |
| Storage       | Plain Text File      |

---

## How It Works

1. **Data Collection**:

   * Scraped hotel information using **SerpAPI**
   * Collected hotel data from **112 countries** and saved to a text file

2. **Vectorization**:

   * Processed text file using **LangChain** and stored vector embeddings in **FAISS**

3. **Query Flow**:

   * User submits a query via the Streamlit app
   * Query is matched with relevant hotel data using FAISS
   * The user query + relevant context are sent to **Claude Opus 3**
   * Generated answer is shown to the user along with **TTS audio**

---
## 📬 Contact

If you'd like to collaborate or have any feedback, feel free to reach out:
**Ahmad Talha Ansari** | \[[ahmadtalha963@gmail.com](mailto:ahmadtalha963@gmail.com)]
