# bank-statement-qa

Bank Statements Query Application using local LLMs. Read more [here](https://docs.llamaindex.ai/en/stable/getting_started/concepts/)


## Features:

- Input: Credit card or bank statement with password in pdf format
- Preprocessing the pdf and extracting tables to csv format
- RAG system with local LLM
- Can answer query based on the data
- Visualizations of credits and debits

## Assumptions:
- Input file name like 'statement_01.pdf' where 01 represents the month number
- Add the environment variables 
```
INPUT_PATH="../data/encrypted/"
OUTPUT_PATH="../data/decrypted/"
PASSWORD="password"
```


## Installation

### 1. Clone the repository:

```sh
git clone https://github.com/kaus19/bank-statement-qa.git

cd bank-statement-qa
```

### 2. Start the server:

```sh
docker compose up --build
```

### 3. Accessing the application:
- Access jupyter notebook at http://localhost:8888
- Run the commands in pre_processing.ipynb 
- Run queries in query.ipynb
- View visualization in pre_processing.ipynb

### 4. Shut down the server:

```sh
docker compose down
```


Notes:
- Embeddings were bottleneck when used 'BAAI/bge-small-en-v1.5'
- Also llama3.2(1billion parameters) did not give correect results.


## Directory Structure:

bank-statement-qa/  
├── Dockerfile  
├── docker-compose.yml  
├── data/  
│   └── decrypted/  
│   └── output/  
├── indexes/  
├── workspace/  
│   └── pre_processing.ipynb  
│   └── dashboard.ipynb  
│   └── query.ipynb  
├── README.md  
├── requirements.txt  


## Future Work

- Support for generic statements
- Make the dashboard interactive
- Include new graphs
- Support for different file formats
- Give insisgts about different categories