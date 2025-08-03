## ✔️ **Common Issues (AWS-related)**

1. **IAM Role Deletion**
    - Blocked by **SCP (Service Control Policy)**
2. **Pipeline Role Missing**
    - pipeline-role is missing from production AWS account.
3. **Access Denied Errors**
    - Denied on pipeline-role
    - Related to:
        - **CloudFormation** (CF)
        - **S3 bucket access**
4. **S3 Bucket Creation Error**
    - Caused by lack of universally unique bucket names
5. **Route 53 (R53) Hosted Zone Issues**
    - Error creating/updating hosted zone due to permission issues
6. **Broad Access Role Errors**
    - Apps unable to access S3 buckets
    - Missing resource-based policies
    - Example: Missing permissions for `s3:GetObject`
7. **Service-Specific Issues**
    - **ses:CreateEmailIdentity**
        - Permission issue—possibly due to SCP
    - **Security Group Deletion Error**
        - Manually added rule—unable to delete
    - **NLB (Network Load Balancer) Creation Failing**
8. MFT file drop issues on S3 bucket

---

## ✔️ ** synchronous communication (teams)**
- Used for Internal Communication
- These are Microsoft Teams channels your organization uses for internal communication:

- **app chat | partner app chat**
- **vendor | Swift Update Chat**
- **business Support**
- **Production Issue | Engage Interface**
- **AWS cloud Support**

Also includes specific technical and support team chats:

- **Developer and Engineer**
- **multi tenant EKS**
- **CD pipeline | terraform | ansible | DevSecOps | D-Hub**
- **Kafka | Message brokers**
- **Java | Frontend | Python**

Additionally:

- Weekly release update on AWS
- eg: **SCP Policy Update** discussions for preventing deployment of **non-golden AMIs**

---
## ✔️ **D2D Discussion**
- PR review and merge process
- Discussion about conference call and outstanding technical checks
- **Created Follow-up Jira on Prod Issue**
    - API analysis task \& “Pound your course” analysis
    - test hotfix
    - mock API for testing 
    - mock vendor like behavior
- **Config Review**
    - Kafka: Retry logic (50 attempts, exponential backoff)
    - Producer/Consumer settings (latest/earliest offset logic)
- **partner app migrated from mulesoft to fastapi**
- **Manual Actions**
    - Manually calling API to send response to partner app
    - Fallback option
- **Certificates & Security**
    - Wildcard certificate creation
    - Token refresh Lambda enhancements
    - OAuth integration (scope) with new partner app
- **Future Enhancements**
    - new downstream. 
    - call API to pull data from partner app 1
    - API to send data to partner app 2
    - new vehicle (buy but can sell after some time, not right away)
- **Engineering Tech Stack**
    - On-prem Confluent Kafka enhancements (topics, replication)
    - Changelog updates (Spark home updates)
    - Spring Boot containers (token refresh bean work)
- **Other Improvements**
    - Content-Type (415 Unsupported Media) bug fixed (duplicated headers)
    - Toggle/Fallback options: rmq vs kafka | mulesoft vs fastapi 
    - **Spring Boot property loading**
    - token refresh Lambda enhancements
    - token refresh bean
    - Deserialization only required for specific API responses


## ✔️ Suggestions for Ongoing Improvement

- **Consider tracking action items by priority/urgency.**
- **Document recurring issues or blockers for quicker resolution.**
- **Regularly update technical decisions and architecture changes.**
- **Keep a record of meetings with SMEs or cross-functional teams for accountability.**
- **Maintain a checklist for weekly release or deployment readiness.**

