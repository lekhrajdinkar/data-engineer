## ✅ A. How to Collaborate with Offshore Developers 
### dumps
- **communication** : `collaboration | leadership | ownership | empathy`
    - transparent with them.
    - **listen** | no friction | no blame
    - make sure no one has any personal problem
    - comm based on their strength and background | not want to overload | step-by-step approaches
    - appreciate work and keep motivated.
    - periodic 1-2-1 session : clarification + highlight area of improvement
    - async comm - confluence + developer guide
    - sync comm - teams daily chat, tag,
    - summary for long session + ping bullet point/minutes
    - collaborate with team, trust team, seek help from offshore, delegate task
- **leaning** : empower with guidance
    - taught them terraform, and now they rae doing all IAC and pipeline
    - guide on tech  and soft skills
    - my design review and feedback.
    - taught harsh py
    - scale people
- **planning**
    - assign work based on strenght.
    - plan work with available bandwidth | jira > subtask
    - set clear expectation + set context | discuss roadmap and timeline
    - stepping only when needed.
    - shared UT scenario list, i add more.
    - discuss high level implementation pla and give feedback
    - everyone tell upfront their vacation plan
    - network outage + laptop taken for security
- code review and daily commit
- delegate unplanned work | discuss daily priority | set clear expectation

### 1. **Establishing Communication & Building Relationships**

- **Situation:**
    - Offshore teams in different time zones
    - Don't have full visibility into the project.
    - things might be misaligned.
- **Task:** Ensure ongoing alignment, engagement, and smooth daily collaboration.
- **Action:**
    - Set up regular calls for **daily stand-ups, sprint planning, and retrospectives.**
    - share docs (confluence)
    - instant messaging tools (Teams) to maintain **real-time communication and transparency**.
    - **Invest time in getting to know individual developers** — show empathy, and involve them in decisions.
- **Result:**
    - Improved team trust + zero friction
    - fewer misunderstandings
    - and enhanced engagement
    - discuss, AWS training and certifications, leetcode, etc
    - they add improvements idea on confluence and discuss. eg: eng response


### 2. **Providing Technical Guidance**

- **Situation:** needed support on architectural decisions on new enhancement.
- **Task:** Guide the team to deliver robust, scalable solutions.
- **Action:**
    - Hold regular code reviews with **constructive feedback and best-practice demonstrations**.
    - **Document technical standards and share architecture diagrams**.
    - **Pair program**
    - organize technical **deep dives** as needed.
- **Result:** Increased code quality, faster onboarding for new team members, smoother project delivery
- [https://www.perplexity.ai/search/explain-pair-programs-construc-F4XuuqW3TU28dhUBmGJg5g](https://www.perplexity.ai/search/explain-pair-programs-construc-F4XuuqW3TU28dhUBmGJg5g)
```text
## Pair program ✔️
- Enhances knowledge sharing: 
    Pairing on coding tasks helps transfer knowledge 
    and best practices between onshore and offshore teams.
- Improves quality: 
    The immediate review reduces bugs and misunderstandings.
    
## Constructive Feedback ✔️
- focused on providing helpful, actionable comments
- aimed at improvement without demotivating the receiver

Focus on the work, not the person.
Be specific and provide examples.
Balance negative feedback with positive points.
Encourage questions and open dialogue to ensure understanding.

## Best-Practice Demonstrations ✔️
- showing, rather than just telling offshore developers,
  how to perform tasks according to your standards and processes.
  eg: 
  Conduct live coding sessions 
  share recorded tutorials demonstrating coding standards
  architecture patterns : discuss trade-offs and design decisions.
  Use real-world examples , put scenarios, analogies, and metaphors to explain complex concepts.
```

### 3. **Soft Skills & Management**

- **Situation:** The team had varying communication styles and experience levels.
- **Task:** Facilitate a collaborative, high-performing culture.
- **Action:**
    - **Encourage knowledge sharing**
    - Encourage **mentorship** among cross-location teammates.
    - Show **appreciation** and recognize offshore **contributions** publicly.
- **Result:** Offshore developers became **proactive**, **more confident**, and **felt like valued team members**


### 4. **Assigning Work**

- **Situation:** Project deadlines required careful task distribution.
- **Task:** Allocate the right work to offshore developers based on strengths.
- **Action:**
    - **Break down stories into clear, manageable tasks with acceptance criteria**.
    - Assign tasks during sprint planning, **ensuring everyone understands priorities and dependencies**.
    - **Encourage offshore developers to participate in grooming and estimation**.
- **Result:**
    - Deadlines were met
    - offshore teams **took greater ownership of deliverables**


### 5. **Providing Feedback**

- **Situation:** Quality or process gaps surfaced in regular deliverables.
- **Task:** **Provide feedback to drive improvement without harming morale**.
- **Action:**
    - Offer feedback as soon as an issue is detected
    - **focus on specific behaviors, not personalities.**
    - Balance positive and constructive feedback during `1:1s`
    - **Collaboratively identify solutions and agree on measurable next steps**.
- **Result:** Offshore team performance improved, with clear growth in quality and confidence


### 6. **Running Agile Ceremonies** ❌

- **Situation:** The Scrum team was split across multiple time zones.
- **Task:** Ensure agile events are meaningful for everyone.
- **Action:**
    - Schedule stand-ups, sprint planning, demos, and retrospectives at overlapping hours.
    - If full overlap isn’t possible, combine live meetings with asynchronous updates.
    - Ensure offshore team members have equal voice—actively invite their input.
- **Result:** Offshore developers felt included; continuous improvement was visible in sprint retrospectives

---
### ✔️**Pro Tips to Showcase**

- **Empathy and Adaptability:** Show you’re sensitive to cultural and time-zone differences.
- **Clear Documentation:** Highlight consistent use of written specs, tickets, and diagrams.
- **Inclusivity:** Offshore team feels like a true extension, not an afterthought.
- **Regular Recognition:** Celebrate offshore team wins to foster motivation and belonging.

### ✔️**Red Flags to Avoid**

- Speaking negatively about remote/offshore capabilities.
- Acting as a “command and control” boss, not a collaborator.
- Ignoring feedback from offshore team members.
- Skipping documentation or assuming things will “just work.”
- Not investing in relationship or trust-building.

### ✔️**Sample Mind Map (Textual Layout)**

- **Collaboration**
    - Communication → Standups, Docs, Video, Messaging
    - Technical Guidance → Code Review, Docs, Pair Programming
    - Soft Skills → Inclusion, Cultural Empathy, Recognition
    - Task Assignment → Clarify, Prioritize, Track Progress
    - Feedback → Timely, Specific, Balanced, Measurable
    - Agile Ceremonies → Adjust for Time-Zone, Include All Voice

---

## ✅ B. leadership 
- initiative | problem-solving
- don't wait for order and continue the work
- lead junior by example | take decision
- **re-evaluate design and write future upgrade** 
    - SNS + add dlq + enable SSN delivery logs
    - de-duplicationID
    - Dashboard API for UI team
    - helix : mc, eks, custom metrics (engine request process rate)

### 1. short term sacrifice for long term gain
- created CIAM dashboard
- removed hardcoding so many thing.
- created config table. perform datamod with doing release in prod.

### 2. calculated risk
- share_qty | t+2
- UMC : quick fix - added feature to stage file and update it then release it
    - create endpoints to stage and manually publish.
    - Documented steps. since  manual steps so risk

### 3. Simplified Complex Problem
- **outbound config:**
    - flexibility in active/deactivate outbound
    - future changes were considered
    - weight based, k1=[v1,v2,...], resolve by weight
    - future state : dynamoDB
- **UMC**
    - added staging areas/s3, for manual update
    - api to enable/disable
- **processing bucket**
    - all event driver by some bucket_mapping_id
    - will be used for tracking and custom metric
- **pySpark Job**

| **STAR Element** | **Answer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **✔️ Situation** | We had a batch job system that processed customer data overnight. It was slow, hard to debug, and frequently failed. Performance degradation became a concern as data volume grew.                                                                                                                                                                                                                                                                                                                                                |
| **✔️ Task**      | I was asked to improve performance and reliability without a full rewrite.                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **✔️ Action**    | - Investigated the PySpark code and found the **main bottleneck was excessive data shuffling** due to wide transformations (like `groupBy` and `join`) on large datasets.<br>- Refactored the job by **optimizing partitioning**, reducing wide transformations, and using `broadcast joins` where applicable.<br>- Rewrote the pipeline using **modular PySpark on AWS Glue**, and replaced manual shell-based triggers with **event-driven Lambda** orchestration.<br>- Added **CloudWatch logs and alerts** for observability. |
| **✔️ Result**    | - **Job runtime reduced by \~50%**<br>- **Failure rate dropped significantly**<br>- The pipeline became **easier to maintain and debug**<br>- Business gained **faster and more reliable data processing**                                                                                                                                                                                                                                                                                                                        |

```python
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName("ShufflingExample").getOrCreate()

# Large dataset A
df_large = spark.read.csv("s3://bucket/large_data.csv", header=True, inferSchema=True)
# Medium dataset B
df_medium = spark.read.csv("s3://bucket/medium_data.csv", header=True, inferSchema=True)
# This join will cause a shuffle across the cluster
joined_df = df_large.join(df_medium, on="customer_id")
# Followed by groupBy - another shuffle
result = joined_df.groupBy("region").count()
result.show()


# Hint Spark to use broadcast join to avoid shuffle
joined_df = df_large.join(broadcast(df_medium), on="customer_id") # 👈🏻

# Repartition by region to optimize groupBy
df_partitioned = joined_df.repartition("region") # 👈🏻
# Aggregation now happens within partition
result = df_partitioned.groupBy("region").count()

result.show()
```
### 4. decision with limited time Data

### 5. project with tight deadline
- CIAM

### 6. lead end2end project
- **maps**
    - scalable system design : ms + event-driven + eventpayload
    - API design
    - implementation
    - handle 
