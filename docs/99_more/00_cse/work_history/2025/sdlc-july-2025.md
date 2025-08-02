## Mind Map: SDLC Stages (Agile) :: July 2025 work

### 1. **Requirement Analysis**

- Business Query
    - Clarified T+2 / T+3 logic
    - Investigated failed SNS alert \& SMTP filter impact
- New VPC Request
    - Requested network capacity with engine team


### 2. **Design**

- Common Kafka Stack
    - Designed shared Kafka infrastructure for SACA, COMET, OIS
    - Okta ID integration
- SACA Project
    - Kafka topics design (MT/MX with 7-year retention)
- Wildcard Certificate on Oz
    - Planned certificate management approach
- SSL on Kafka
    - Discussed SSL strategy on container vs local setup


### 3. **Development**

- Prod API
    - Managed API calls with different scopes (`execute`, `read`, `datamod`)
    - RBAC role configuration \& manual response sending
- Mock API for QA
    - Created partner response simulation for Prod 3 fix testing
- Kafka Bridge with COMET
    - Supported Poland development with replication setup


### 4. **Testing**

- Offshore Test Planning
    - Coordinated DVA training to cover test areas
- DR Script Validation
    - Validated disaster recovery scripts post new model launch
- Prod Issue 2 (Blank file)
    - Coordinated upstream fix for noise file issue


### 5. **Deployment**

- New Model Launch
    - Reviewed \& planned deployment scripts and steps
- DB Deployment
    - Handled DB deployment in senior absence, trained Yubo on Flyway
- Harness Pipeline Status
    - Provided visibility and shared pipeline experience within GitHub Desktop


### 6. **Maintenance \& Support**

- Prod Issue 3
    - Resolved JSON parsing issue (`int` vs `long`/`bigint`)
    - Raised backlog JIRA for unwanted attribute
- Kafka Onboarding (app-4)
    - Assisted with Kafka connectivity (404/network), consumer groups, Okta setup
- ETL File Support
    - Supported E2E team with latest files from S3 ETL bucket
- SACA/COMET/OIS Meetings
    - Participated for planning, progress updates, delivery alignment


### 7. **Security \& Infrastructure Management**

- Wildcard Certificate
    - Created, manually imported SSL certs in AWS regions, documented process
- SSL on Kafka
    - Discussed container security setup
- SMTP Filter Impact on Alerts
    - Supported email alert plan changes due to security filters


### Summary:

- **Cross-functional collaboration:** Worked closely with app teams, offshore test, engineering, and security teams.
- **Hands-on technical fixes:** Debugging prod issues, Kafka onboarding, API \& ETL support.
- **Design \& deployment:** Kafka stack design, new model launch planning, CI/CD pipeline visibility.
- **Security \& infrastructure:** SSL cert management, VPC requests, email alert security impact.


