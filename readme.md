## Data Engineering & Analytics Docs

🔶 in progress...

### Python

Master Python for data engineering, scripting, and backend fundamentals.

- **Kickoff:** Quick intro and learning goals
- **Language Fundamentals:** Core Python syntax, datatypes, and language constructs
- **Global Functions:** Essential built-in and custom functions for developers
- **Modules & Design Patterns:** Organizing Python code; using modules and core design patterns
- **OOPS:** Object-oriented programming best practices
- **Useful Functions:** Handy snippets and frequently used utilities
- **More 🗨️:** Q&A, notes, or extra discussions


### Spark

Practical, hands-on approach to PySpark, big data processing, and analytics.

- **Index:** Table of contents and overview
- **Pandas:** Using pandas in conjunction with Spark for data handling
- **Setup Locally:** Step-by-step local PySpark environment setup
- **Architecture:** How Spark works under the hood
- **ETL 01 & 02:** Example ETL (Extract, Transform, Load) workflows with PySpark
- **File Formats:** Working with various data formats (CSV, Parquet, etc.) in Spark
- **PySpark 01:** Beginner’s guide to PySpark APIs and operations


### Database (Postgres RDBMS)

Comprehensive guide to relational databases, focusing on PostgreSQL.

- **Start:** PostgreSQL intro, getting started
- **Data Types & Constraints:** Exploring supported types and table constraints
- **Normalization:** Principles and processes for data normalization
- **Index:** Indexes and their performance implications
- **DDL, DML, DQL, DCL:** Core SQL command types—definitions and use cases
- **ACID & Locks:** Transaction management and locking mechanisms
- **Functions, CTEs, Views:** Advanced SQL, reusable logic, and virtual tables
- **Partitioning & Sharding:** Scaling relational databases
- **Project 01:** Real-world Postgres project—a Shopping App schema and practices


### Data Platform (Databricks) 🔸🔸🔸

- **Databricks Start:** Introduction, workspace setup, and first steps in the Databricks environment


---

## RoadMap

```
Databricks + PySpark
│
├── 1. Fundamentals
│   ├── Spark Architecture
│   │   ├── Driver & Executors
│   │   └── DAG & Stages
│   ├── Spark Cluster Modes
│   └── Databricks Architecture
│       ├── Workspaces
│       ├── Clusters & Jobs
│       └── Notebooks & Repos
│
├── 2. PySpark Core
│   ├── RDDs vs DataFrames
│   ├── Transformations & Actions
│   ├── Schema Inference & Explicit Schemas
│   └── Spark SQL
│
├── 3. Databricks Essentials
│   ├── Delta Lake
│   │   ├── ACID Transactions
│   │   ├── Time Travel
│   │   └── Merge (Upserts)
│   ├── Unity Catalog (Security & Governance)
│   └── Lakehouse Paradigm
│
├── 4. Data Engineering Workflows
│   ├── Autoloader (Streaming ingestion)
│   ├── Structured Streaming
│   ├── Jobs (Workflow Orchestration)
│   └── Task Dependencies
│
├── 5. Optimization Techniques
│   ├── Caching & Persistence
│   ├── Broadcast Joins
│   ├── Predicate Pushdown
│   └── Adaptive Query Execution (AQE)
│
├── 6. CI/CD & Deployment
│   ├── Repos & Git Integration
│   ├── dbx CLI
│   └── Workflow deployment (Job APIs)
│
├── 7. Monitoring & Debugging
│   ├── Spark UI
│   ├── Cluster Metrics
│   └── Logging & Alerting
│
├── 8. Real Projects / Practice
│   ├── ETL Pipeline (Batch + Delta)
│   ├── Streaming Pipeline (Kafka → Delta)
│   ├── CDC with Merge + Time Travel
│   └── ML Integration (MLflow intro)
│
└── 9. Certifications (Optional)
    ├── Databricks Data Engineer Associate
    └── Databricks Data Engineer Professional

```