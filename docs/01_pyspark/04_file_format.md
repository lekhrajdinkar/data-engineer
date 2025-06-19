# Columnar storage formats (for big data processing)
- [parquet_demo.py](../../src/demoModule/parquet_demo.py)
- **columnar** : all the values of a single column are stored together
  - Advantages:
    - Efficiency for Analytical Queries
    - Better Compression: Values in a column are often similar, making compression more efficient.
    - Predicate Pushdown: Enables faster filtering.
```
# Column
Row 1: id=1, name="Alice", salary=1000
Row 2: id=2, name="Bob", salary=1500

# Columnar
Column "id": 1, 2, 3
Column "name": "Alice", "Bob", "Charlie"
Column "salary": 1000, 1500, 2000

```

## A Parquet
- support **Schema** Evolution.
- Columnar storage format optimized for **analytical queries**.
  - Optimized for reading specific columns in wide tables.
- efficient **compression** and encoding.
  - Compression: Supports multiple compression codecs (e.g., Snappy, GZIP, ZSTD).
- use case:
  - If your workload involves accessing a **subset of columns** from a large dataset.
```
# == install  
brew install parquet-tools  # MacOS
apt-get install parquet-tools  # Ubuntu

    # inspect
    parquet-tools schema output/sample.parquet
    parquet-tools head output/sample.parquet

```      
---
## B ORC
- designed by the Apache Hive team for `Hadoop`.
- Focuses on high compression ratios and high-speed I/O.
  - advanced compression techniques (e.g., ZLIB, Snappy, LZO).
- for better query **performance** (min/max values, row counts, etc.).
  - **Built-in indexes**
  - Enables filtering at the storage layer for `faster queries`.
  - **Block Splitting**: 
    - Data split into stripes, 
    - improving parallel processing.
- use case :
  - If working in a Hadoop/Hive ecosystem or need advanced indexing and compression for large datasets

---
## C Avro
- **Row-based**
- better for streaming
