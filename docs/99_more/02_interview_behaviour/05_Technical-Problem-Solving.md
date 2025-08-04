### Future improvement ideas ✔️
- Note: Apply use System design skills 👈🏻👈🏻
- x-rays | dd metric : custom performance metric
- dashboard api
- s3 MRAP
- eventbus - deduplication
- SQS fifo with kafka
- lambda cold fix
- VPCE endpoint
- sns - failure : enable delivery log | dlq
- SQS > Lambda trigger > **async call** with destination + exp retry

### 1.1 innovation solutions
- create API for dev and QA profile.
- enable/disable , config API
- mock incoming message | mock vendor behaviour
- create API to S3 bucket view and download + UI ng
- create API for message broker
- merge TIP files + additional logic to decode row and show summarized API. API to validate it.
- For CIAM : day-1 + day-2 response | staging failure response

### 1.2 balance innovation **with stability**

### 3 Complex problem

| **STAR Element** | **Response**                                                                                                                                                                                                                                                                                                                                                           |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ✔️ **Situation** | In our production environment, SNS alerts were intermittently failing, and business users were not receiving critical email notifications.                                                                                                                                                                                                                             |
| ✔️ **Task**      | I needed to identify the root cause and implement a reliable, long-term solution to ensure alert delivery regardless of network issues.                                                                                                                                                                                                                                |
| ✔️ **Action**    | Through investigation, I found the failures occurred during firewall updates that blocked outbound internet traffic. Since SNS used public endpoints, the service was unreachable. I resolved this by configuring a **VPC endpoint for SNS**, enabling private communication via AWS’s internal network. I also tested the solution under simulated outage conditions. |
| ✔️ **Result**    | After the change, SNS alerts became consistently reliable, even during firewall updates. This restored business confidence, improved system reliability, and reduced incident escalations.                                                                                                                                                                             |

| **Problem**                     | **Fix**                                |
| ------------------------------- | -------------------------------------- |
| Large shuffle on join           | Use `broadcast()` on smaller dataset   |
| Shuffle due to groupBy          | Use `.repartition()` by the group key  |
| Inefficient wide transformation | Reduce or chain narrow transformations |
```
-- DUMPs --
- sns alerts, failed multiple time : created 🔸vpce
- message beyond 256 KB, 🔸S3 extended
- outbound enable/disable based on bucket, flexible schema design with RDBMS and then to dynamoDB noSQL
    - complexity incresed > rebalance, allocations, hasetf, etc more attribures
    - multiple vale for  same key > resolve by weight 
- token refresh lambda
- OutOfMemory : created seperate cache server, data grows, used enums
- batch job min : DB call optimize + enums
- cian simulator and dashboard
- app-4 : 15 min password expire 👈🏻
```

### 5. Design phase with business
- how you interact

### 6. Evaluating build vs buy decision
- arch level decision

### 7. Fast delivery
- jira with clear acceptance | expectation | scope
- Automate UT with junit , pytest
- CI pipeline (platform) - wiz and synk scan + fix vul
- CD pipeline (developer) - harness pipleine (generic) + add input set | helm | k8s manifest

### 8. Applied CAP theorem
- Can always be achieved in single region
- for distributed system, B2C
- so never applied but thought about scenarios, how my organization follow CAP.
- being financial org, Data consistency is important
- used Aurora serverless
- no no-SQL distributed DB, becoz of eventual consistency.

### 9. Technical quality vs consistency
- **Technical quality**: Focus on writing clean, maintainable, and efficient code.
- **Consistency**: Ensure that the codebase follows established patterns and practices across the team.