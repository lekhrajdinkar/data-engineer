```
== CSV ==
id,name,age
1,Alice,30
2,Bob,25


📦 Parquet
Columnar binary format, optimized for big data analytics (e.g., Spark, Athena).

Column: id    → [1, 2]
Column: name  → ["Alice", "Bob"]
Column: age   → [30, 25]


📦 Avro
Row-based binary format, good for streaming and schema evolution.

{
  "schema": {
    "type": "record",
    "name": "Person",
    "fields": [
      {"name": "id", "type": "int"},
      {"name": "name", "type": "string"},
      {"name": "age", "type": "int"}
    ]
  },
  "data": [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25}
  ]
}


```

| Format  | Type      | Readable?       | Optimized for              |
| ------- | --------- | --------------- | -------------------------- |
| CSV     | Row-based | ✅ Text          | Simplicity                 |
| Parquet | Columnar  | ❌ Binary        | Analytics/Queries          |
| Avro    | Row-based | ❌ Binary/JSON\* | Streaming/Schema evolution |

