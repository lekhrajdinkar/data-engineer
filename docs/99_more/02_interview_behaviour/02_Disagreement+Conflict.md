## ✅ A. Handling Disagreements and 
### 1 disagreement on system Design (yours)
- **inbound etl**
    - S3 > SQS > `poll`(py) > etl::thread
    - s3 > SQS > lambda-trigger (async + destination) > api >  exposed etl as API. === `PUSH`
- **Aurora config vs DynamoDB** :
    - needed flexibility in schema evolution

### 2 disagreement on system Design (others)


---
## ✅ B. influencing / persuasion / convince
### 1 Convincing others on system design
- **Situation**: I proposed a new system design for the inbound ETL process.
- **Task**: Convince my team to adopt a more modular and scalable approach.
- **Action**: I presented a detailed comparison of the current design vs my proposal, highlighting
  the benefits of modularity, scalability, and maintainability. I also provided a prototype to
  demonstrate the feasibility of my approach.
- **Result**: The team agreed to implement my design, which led to improved system performance
  and easier future enhancements.

### 2 Convincing others on process change

### 3. convince system design

### 4. convince senior
- **story-1**
    - app-6's inbound module 🔸
    - senior over did engineer - aws glue job, cluster serverless, hourly pay
    - I advised, max 2 GB csv coming daily and  single server could handle, no cluster needed for processing
    - advised to write custom etl code with pyspark.
    - start with ECS cluster task with task=1. it will scale task count horizontally in the future.

- **story-2**

### 5. Convince junior / offshore
- Daily doing at offshore call
- **Decision taken for offshore** ? ❓
- offshore usually jumping into implementation directly, with **implementation design** 🔸
    - kafka with single system, initially
    - later on new partner added ( comt,sio,ihd,etc )
    - IAC refactor to create topic with same okta (1-M vs 1-1)
    - wrote java interface + updated spring-boot properties to show my design : serializer
    - code review : redundant code  for  connection
  
---
## ✅ C. Dealing with Conflicts
### 1 Conflict with a colleague
```
sample
- **Situation**: I had a disagreement with a colleague about the best approach to handle a
  specific technical challenge.
- **Task**: Resolve the conflict while maintaining a positive working relationship.
- **Action**: I scheduled a one-on-one meeting to discuss our differing viewpoints. I
  listened to their concerns and shared my perspective. We agreed to run a small experiment to
  test both approaches.
- **Result**: The experiment showed that my approach was more effective, but I acknowledged
  my colleague's contributions. We found common ground and improved our collaboration moving
  forward.

```



