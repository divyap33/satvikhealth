import streamlit as st
from google import genai
from google.genai import types
import smtplib
from email.mime.text import MIMEText

print("inside app.py") 
# ==========================================
# 1. CORE RESUME & LINKEDIN KNOWLEDGE BASE
# ==========================================
# Pro-tip: Keep your background data as clean structured text directly inside the script.
MY_PROFILE_DATA = """
NAME: Divya Prakash
TITLE: Sr. Director – Data Strategy, Architecture & Engineering
LINKEDIN PROFILE SUMMARY: Contact
21236, Hillgate cir., Trabuco
Canyon, CA - 92679
5714238561 (Mobile)
divya.prakash.work@gmail.co
m
www.linkedin.com/in/divyaprakash
(LinkedIn)
Top Skills
Biotechnology Industry
OEM negotiations
Fast Healthcare Interoperability
Resources (FHIR)
Languages
English (Full Professional)
Hindi (Native or Bilingual)
Certifications
Artificial Intelligence: Implications for
Business Strategy
Managing Team Software Processes
SCRUM Master - Agile Methodology
Practice
Honors-Awards
Most Valuable Person (MVP) award
All India Talent Search Scholarship
Publications
Usability Testing and Acceptance
of an Electronic Medication Inquiry
System for CKD Patients
Remote usability testing and
satisfaction with a mobile health
medication inquiry system in CKD
Duration of First Line Therapy in
Metastatic Non-Small Cell Lung
Cancer
Usability of a Drug-Drug Interaction
Inquiry System for Kidney Transplant
Patients
Divya Prakash
Data Engineering and Governance Leader | Building Scalable Data/
AI Solutions
Trabuco Canyon, California, United States
Summary
With over two decades in data-driven innovation, I currently lead the
Data Platform Architecture team at Mars Veterinary Health, where
we are building a cutting-edge Azure Databricks-based Enterprise
Data Lake Warehouse. Our focus lies in creating a scalable and
reliable analytics platform, guiding data migration to the cloud, and
enabling actionable insights through advanced Power BI services.
Collaborating with stakeholders, we define data and AI strategies
that drive impactful outcomes across multiple veterinary banners.
As the Head of Data Architecture @ i-GenticAI , we are building
a first agentic AI platform built to govern AI, privacy, data, and
cybersecurity policies across enterprise infrastructure — in real time.
Experience
Mars Veterinary Health
Director, Data Platform Architecture
September 2024 - Present (1 year 11 months)
Trabuco Canyon, CA
Leading Data Architects, Data Engineers and Data Analysts in building an
Azure Databricks based Enterprise Data Lake Warehouse for Mars Veterinary
Health (MVH). The Enterprise Data Platform serves as a central Data Lake for
various banners acquired under MVH like VCA, Anicura, Banfield, Blue Pearl.
• Collaborating closely with stakeholders and decision makers to formulate
Data & AI strategy and product road map for MVH Data Platform.
• Constructing high scalable and reliable Data & Analytics Platform based on
Azure Databricks Medallion Architecture and Power BI services from ground
up.
• Migrating on-prem Data warehouse platform to Cloud-based MVH Enterprise
Data Platform BI reports.
• Real-time data processing pipelines based on KafkaConnect-Azure Eventhub
and Spark streaming services.
Page 1 of 7
• Collaborating with stakeholders to define Data Governance framework and
processes to streamline Data Quality use cases, request intake process and
leveraging Microsoft Purview for Data Catalog documentation.
• Implementation of cost optimization strategies for azure Databricks
workspaces - data pipelines, storage, and cluster configurations
i-GENTIC AI
Head, Data Architecture (Advisory role)
June 2024 - December 2025 (1 year 7 months)
Building AI and Data Architecture for i-GenticAI Governance and Compliance
platform. Working with AI engineers and Architects to design and construct
scalable AI Platform to support onboarding clients with AI Governance and
compliance automation needs.
Satvik Health LLC
Founder
March 2024 - June 2025 (1 year 4 months)
Trabuco Canyon, CA
Satvik Health is dedicated to infusing purity and excellence into the US
healthcare and insurance domain. Derived from the Sanskrit word meaning
"Pure" or "Pious," our name reflects our commitment to integrity, quality, and
innovation in every aspect of our operations.
At Satvik Health, we specialize in leveraging data intelligence to drive
transformative outcomes in healthcare and benefits management. Our team
comprises seasoned Data and Analytics experts with extensive experience in
the healthcare and benefits domain. With a deep understanding of clinical and
benefits data sets, we excel in developing cutting-edge data products tailored
to meet the unique needs of our clients.
Evolent
Managing Director , Data & Analytics
January 2021 - May 2024 (3 years 5 months)
Brea, California, United States
As a Managing Director at Evolent, I led the Business Intelligence Center of
Excellence (BI CoE) department, building the next generation Specialty Data
Platform on Azure (PowerBI, Synapse Analytics/Databricks) to support data
and analytics needs for oncology, cardiology, and musculoskeletal specialties.
My responsibilities included :
Page 2 of 7
Core member of NCH Technology Steering Co. responsible for charting NCH
technology road map including digital analytics, data and AI strategies.
Accountable for success of Data & Reporting Governance Committee
(comprises of Exec Leads), facilitating prioritizations of strategic initiatives and
setting up annual goals for the team.
Leading a global teams of 50+ dedicated people (US & India teams)
comprising Directors, Architects, Data/ BI Developers, Data Analysts, QA
and Data Scientists in building azure cloud-based Specialty Data & Analytics
platform.
Led AI (JohnSnow Lab NLP) driven Utilization Management automation
initiative to support optimization effort in UM staffing by building prediction
model for metastasis condition in patient based on their Lab results.
Designed and developed Claims Analytics Platform (PMPM Model) for
Healthcare claims and authorization data sets. The platform enabled advanced
analytics and supported operational reporting platform (PowerBI) for CMS
compliance reporting.
Introduced metric driven DevOps processes to measure results and support
OKRs.
New Century Health (now Evolent)
5 years 2 months
Senior Director, Data & Analytics
January 2018 - December 2020 (3 years)
Brea
Continued to build on the EDWBI platform to deliver new data driven
applications and providing deep insights into auth and claims data mart.
My focus as Sr. Director was to set up data driven development operations
(DevOps) for the newly built EDWBI platform. My responsibilities include:
Managed the EDWBI budgets and reorganized personnel and tasks
resulting in a reduction of product and operation costs by 15% while
improving operational efficiency in data operations through smart automation
approaches. 
Built and grew a high-performing core development team of FTEs (Team size:
20 onsite (Brea, CA), 6 offshore -Pune, India) by insourcing consultants, hiring
the right resources for the job hence reducing the dependencies with vendor
organizations.
Page 3 of 7
Collaborated with business stakeholders to conceptualize a request intake
process leading to Data & Reporting Governance (DRGC) framework to work
efficiently with various departments within NCH.
Built data driven applications on top of EDWBI to drive value for NCH
Operations and a platform to support innovation projects including few
publications on ASCO and NCCN.
Director, Data & Analytics
November 2015 - December 2017 (2 years 2 months)
Orange County, California Area
New Century Health (NCH) is a leading Specialty Management Organization
providing utilization & spend management solutions in Oncology and
Cardiology domains. I led EDWBI team reporting under Chief Information
Officer building Enterprise Data Warehouse & Business Intelligence platform
from ground up for the organization. My responsibilities included:
Built an on-prem NCH Data Lake and EDWBI platform hosting clinical, claims
and Finance Data Marts from ground-up using Microsoft BI suite to enable
operational/BI reporting & advanced analytics.
Led a team of 20+ people across geographies (FTEs and consultants)
comprising Architects, Data & BI engineers, Data Analysts, QA and Data
Scientists in building the EDWBI and Analytics platform.
Went live with Authorization and Claims Data Mart with Operational BI
Reporting within a short span of 8 months there by saving ongoing cost of ad
hoc analytics and erroneous data reporting through silo databases.
PatSage LLC
Founder, CEO
January 2014 - January 2016 (2 years 1 month)
Irvine
PatSage.com – A cost effective Patent Analytics application for IP research
fellows with advanced analytics features based on Natural Language
Processing algorithms using AWS (MySQL, Elastic Search, Lambda, ReactJS/
NodeJS based tools).
Patient-Physician Engagement Platform: - Developed AWS cloud-based
application for engaging Patient and Physician workflows to reduce Clinic’s
Page 4 of 7
cost of call center and reducing patient visits. A highly customizable platform
to enable any clinical workflow supports all four modes of interactions –Web
Portal, IVR, SMS and iPhone App. The platform was evaluated at University of
Maryland Medical Center and the results were published in AJKD journals.
St. Joseph Health (now Providence Health)
Senior Data Manager
January 2012 - September 2015 (3 years 9 months)
Led BI & EDW team for a 16-hospital health system spanning California and
Texas, managing a 100+ TB Enterprise Data Warehouse with daily load rates
of ~100M records/day.
St. Joseph's Health System
Sr. Manager, EDW & Analytics
January 2012 - July 2015 (3 years 7 months)
Orange County, California Area
Leading St Joseph's Enterprise BI/ Analytics and Enterprise Information
Management/MDM platforms teams - Amalga UIS, MS BI Suites, Tableau,
Explorys Big Data implementation, Informatica Master Data Management
initiative.
Responsibilities include Program Management, Enterprise Architecture,
Processes Improvement, Vendor Selection and Contracts Management,
Technical Leadership and Strategy, Managing BAs & Dev, Level-2 and
Production Support teams.
Team size: 15 onsite (Anaheim, CA) , 10 offshore (Bengaluru, India)
Calance
Sr. Program Manager
December 2007 - December 2011 (4 years 1 month)
- With GE Healthcare as Lead Architect, I was part of core group envisioning
innovative product for Patient Care (GE Healthcare), Prototyping new ideas,
building product development team from ground up. I was part of a core group
defining product strategy and road map of a path-breaking Clinical Analytics
product based on predictive modeling of clinical data to predict outcomes
guiding effective patient care.
- As Technical Manager with Microsoft , managed Amalga UIS/ HealthVault
Community Connect roll out at various client locations. I have facilitated Health
IT workshops to help solve business problems using Amalga and other MS
HSG products. I have been instrumental in developing Amalga Practice group
Page 5 of 7
within Calance corp and positioning Calance as Health IT system Integrator in
Health IT market place.
Skills: Business Intelligence · Data Warehousing · Business Analysis · Program
Management · SDLC · Analytics · Healthcare Information Technology ·
Integration · Agile Methodologies · Cross-functional Team Leadership · Product
Evangelism
Led an Onsite-Offshore mix of team for the development of a patent pending
solution “BedSide TV” to bring patient care to a digital TV using IPTV
technology.
Worked for Microsoft and GE Healthcare as consultant in various roles.
Calance Corp. (Microsoft Partner)
Senior Program Manager
December 2007 - December 2011 (4 years 1 month)
Led enterprise BI program delivery for Microsoft partner engagements.
Microsoft Corporation
2 years 1 month
Program Manager, BI Center of Excellence
December 2005 - December 2007 (2 years 1 month)
Worked on building specialized offshore team of BI and Data Warehousing
professionals to develop and manage Business Intelligence & DW platform for
Microsoft's Sales & Marketing group which caters to world wide Sales force to
manage there their Budget, Quota and opportunities.
I led MS offshore development team and external vendor team in delivery of
new enhancements and maintenance of MS EPG Sales & Marketing portal
and DW platform.
Business Program Manager
December 2005 - December 2007 (2 years 1 month)
Drove BI Center of Excellence programs and internal data platform strategies.
Siebel Systems
Lead Engineer, Siebel Analytics
January 2005 - December 2005 (1 year)
I was part of Siebel Analytics 7.8 product development team and led the
offshore effort for design and functional specification for ETL modules, BI
reports for Sales and Marketing horizontals of Siebel Analytics BI platform.
Page 6 of 7
Sapient
Technical Lead
January 2002 - December 2005 (4 years)
Delivered enterprise data and application solutions across financial and
government sectors.
Publicis Sapient
Senior Associate, Technology
November 2001 - December 2004 (3 years 2 months)
I worked as Senior Associate, leading various design and implementation
projects ranging from Enterprise Application Integration, Business Intelligence
and Data Warehousing, Content Management, B2B portals for clients like
Verizon telecom, Sony Electronics Audi and Expresso.
Education
Indian Institute of Technology, Delhi
Master of Technology - MTech, Biochemical Engineering &
Biotechnology · (January 1999 - June 2000)
Indian Institute of Technology, Delhi
Bachelor of Technology - BTech, Biochemical Engineering · (July
1995 - January 1999)
Kendriya Vidyalaya
CBSE 12th Board examination, CBSE 10th Board, Physics, Mathematics,
Chemistry, Biology, Languages & Litrature: English, Hindi · (1991 - 1995)
Indian Institute of Technology, Delhi
Master's Degree, Biochemical Engineering
MIT Sloan School of Management
Executive Master of Business Administration, Artificial Intelligence
Page 7 of 7
RESUME EXPERIENCE: DIVYA PRAKASH
Sr. Director – Data Strategy, Architecture & Engineering
Trabuco Canyon, CA  |  571-423-8561  |  divya.prakash.work@gmail.com  |  linkedin.com/in/divyaprakash  |  US Citizen

EXECUTIVE PROFILE
Strategic data leader with 25+ years of experience architecting enterprise-scale data platforms, driving data governance, and leading high-performing engineering organizations across healthcare, veterinary, and technology sectors. Proven track record owning the full lifecycle of data strategy—from enterprise architecture and data lakehouse design to AI/ML enablement and executive stakeholder alignment. Led multi-million-dollar programs at Mars Veterinary Health, Evolent, Providence Health, and Microsoft, consistently delivering platforms that reduce cost, accelerate analytics, and enable organizational data maturity. Adept at translating business vision into scalable data architecture and building 20–50+ person engineering teams from the ground up.

CORE COMPETENCIES

Enterprise Data Architecture: Cloud data lakehouse design, medallion architecture, multi-tenant platforms, target-state architecture roadmaps	Data Strategy & Governance: Enterprise data strategy, data governance frameworks, data quality, cataloging (Microsoft Purview, Informatica MDM, Unity Catalog)
Data Engineering Leadership: Azure Databricks, Synapse Analytics, ADF, DBT, Kafka/Event Hub, Spark Streaming, real-time pipeline engineering	AI/ML & Advanced Analytics: MLOps platform design, NLP (JohnSnow Labs), Azure AI Studio, predictive modeling, Azure AI Search, TensorFlow
Cloud & Platform Architecture: Azure (Databricks, Synapse, ADLS, CosmosDB, Purview), multi-cloud strategy, infrastructure cost optimization	Business Intelligence & Reporting: Power BI Premium COE, Tableau, Looker Studio, enterprise semantic layer, compliance and operational reporting
Organizational Leadership: P&L ownership, 50+ person teams across US & India, OKR/metric-driven DevOps, vendor/contract negotiation	Healthcare Data Standards: FHIR, HL7, EDI-837/834, clinical data models, value-based care analytics, specialty management


PROFESSIONAL EXPERIENCE
Director – Data Platform Architecture |  Mars Veterinary Health (MVH)	Sep 2024 – Present
Architect and lead the Azure Databricks-based Enterprise Data Lakehouse for MVH's hospital network (VCA, Anicura, Banfield, Blue Pearl), serving as the foundational analytics and data platform across all business units.
•	Own the enterprise target-state data architecture: designed a multi-tenant medallion architecture (Bronze/Silver/Gold) on Azure Databricks to consolidate disparate BU data warehouses into a centralized Enterprise Data Hub (EDH), reducing data silos across 4+ major hospital chains.
•	Product Owner for the Foundation Pod (10-person team), accountable for platform reliability, data quality SLAs, and cross-BU intake governance across the multi-tenant EDH.
•	Defined and operationalized the MVH Data Governance framework: standardized metadata management, data cataloging, and data quality use cases leveraging Microsoft Purview across all Databricks workspaces and Unity Catalog.
•	Architected and led migration of on-premises BU data warehouse platforms to the central Azure Databricks multi-tenant EDH, including full schema mapping, data lineage, and cutover planning.
•	Designed near-real-time streaming pipelines using KafkaConnect, Azure Event Hub, and Spark Streaming to enable sub-minute data latency for operational analytics.
•	Drove platform cost optimization: restructured cluster configurations, storage tiering, and pipeline scheduling, achieving measurable reduction in Databricks compute costs.
•	Co-led Data & AI strategy formulation with executive stakeholders, defining the multi-year product roadmap for the MVH Data Platform, including AI/ML capabilities via MLOps integration with the Voyager PIMS application.

Managing Director – Data & Analytics |  Evolent Health	Jan 2021 – Apr 2024
Led the Data Engineering & BI Center of Excellence (50+ person organization, US & India), reporting to the Chief Product Officer. Built a next-generation Value-Based Specialty Data Platform on Azure serving Oncology, Cardiology, and Musculoskeletal care management.
•	Architected and delivered an Azure Databricks/Synapse Analytics data lakehouse (Authorization Clinical Data Lake, Claims Data Lake, PMPM Model, Analytics Platform) with streaming ingestion for near-real-time analytics at enterprise scale.
•	Established and scaled a Power BI Center of Excellence: designed enterprise-wide semantic data models and compliance reporting datasets enabling value-based care operations across all lines of business.
•	Core member of Evolent Technology Steering Committee, co-owning the enterprise technology roadmap including data, digital, analytics, and AI strategy.
•	Chaired the Data & Reporting Governance Committee (executive-level): facilitated prioritization of strategic data initiatives, defined annual OKRs, and drove adoption of metric-driven DevOps practices across engineering teams.
•	Led an AI-driven Utilization Management automation initiative using JohnSnow Labs NLP to build a metastasis prediction model from lab results, reducing manual UM staffing requirements and improving authorization decision speed.
•	Managed full IT budget for Data & BI organization; negotiated vendor contracts and drove ROI-focused investment decisions across platform, tooling, and workforce.

Sr. Director / Director – Data & Analytics |  New Century Health (now Evolent)	Nov 2015 – Dec 2020
Built the Enterprise Data Warehouse and Business Intelligence platform from ground zero for a specialty management organization serving Oncology and Cardiology domains, reporting to the Chief Information Officer.
•	Designed and built an on-premises NCH Enterprise Data Lakehouse hosting clinical, claims, and finance data marts using the Microsoft BI suite, enabling operational/BI reporting and advanced analytics across the organization.
•	Led and scaled a 20+ person cross-geography team (FTEs + consultants): Architects, Data & BI Engineers, Data Analysts, QA, and Data Scientists.
•	Delivered Authorization and Claims Data Mart with full operational BI reporting within 8 months, eliminating ad-hoc analytics costs and unreliable silo-based reporting.
•	Established Data & Reporting Governance Committee (DRGC) framework in collaboration with executive leadership, driving data strategy alignment and governance adoption across the enterprise.
•	Reorganized team structure and automation strategy, reducing product and operations costs by 15% while improving data pipeline reliability and operational efficiency.
•	Insourced key consultant roles and recruited high-performance FTE talent, reducing third-party dependencies and building a durable internal engineering capability.

Sr. Manager – Data & Analytics |  St. Joseph Health (now Providence Health)	Jan 2012 – Sep 2015
Led BI & EDW team for a 16-hospital health system spanning California and Texas, managing a 100+ TB Enterprise Data Warehouse with daily load rates of ~100M records/day.
•	Led a 20+ person BI/EDW team delivering advanced analytics capabilities and self-service statistical analysis to clinical and financial business units.
•	Designed and implemented a Healthcare Clinical Data Model (Clinical and Financial Data Mart) using SSAS/SSRS and Tableau, enabling enterprise-grade reporting and analytics.
•	Led enterprise Data Governance initiative: implemented Informatica MDM platform (Data Quality, MDM, Metadata Manager) for Provider Data Management and Patient Data Management at scale.


EARLIER CAREER
•	Consulting Head of Data Architecture, i-GenticAI – Architected AI and data infrastructure for an Agentic AI-based governance and compliance platform for healthcare and finance, leading AI engineers and data architects in designing scalable onboarding pipelines.
•	Founder, Satvik Health LLC – Founded a healthcare technology startup; developed PatSage.com (patent analytics with NLP), a Patient-Physician Engagement Platform, and a Claims Analytics Platform on Azure Databricks/Power BI.
•	Sr. Program Manager, Calance Corp. (Microsoft Partner) | Dec 2007 – Dec 2011 – Led enterprise BI program delivery for Microsoft partner engagements.
•	Program Manager – BI COE, Microsoft Corporation | Dec 2005 – Dec 2007 – Drove BI Center of Excellence programs and internal data platform strategies.
•	Technical Lead, Sapient Corporation | Jan 2002 – Dec 2005 – Delivered enterprise data and application solutions across financial and government sectors.

PUBLICATIONS & RESEARCH
•	"Duration of First Line Therapy in Metastatic Non-Small Cell Lung Cancer" – Journal of the National Comprehensive Cancer Network (JNCCN), Mar 2019
•	"Usability Testing and Acceptance of an Electronic Medication Inquiry System for CKD Patients" – American Journal of Kidney Disease (AJKD), Nov 2012
•	"Usability of Mobile Technology to Screen for Drug-Drug Interactions in Kidney Transplant Patients" – PubMed, Jul 2014
•	"Remote Usability Testing and Satisfaction with a Mobile Health Medication Inquiry System in CKD" – PubMed, Aug 2015

EDUCATION & CERTIFICATIONS
Integrated M.Tech – Biochemical Engineering & Biotechnology | Indian Institute of Technology Delhi (IIT-D)
Executive Program – Artificial Intelligence: Implications for Business Strategy | MIT Sloan School of Management
Certifications: Certified Scrum Master (CSM) |  Certified Team Software Process (TSP)

TECHNICAL SKILLS

Data Architecture & Lakehouse: Azure Databricks (Unity Catalog, Delta Lake), Azure Synapse Analytics, ADLS Gen2, Medallion Architecture, Multi-tenant Platform Design	Data Governance & Cataloging: Microsoft Purview, Informatica MDM, Unity Catalog, Azure MDS, DQS, Data Quality Frameworks, Metadata Management
Data Pipelines & Integration: DBT, Azure Data Factory (ADF), SSIS, Informatica, KafkaConnect, Azure Event Hub, Spark Streaming, FHIR, EDI-837/834, HL7	AI/ML & Analytics Engineering: Azure AI Studio, Azure AI Search, Spark-NLP (JohnSnow Labs), TensorFlow, CosmosDB, Elastic Search (ELK), MLOps
Business Intelligence: Power BI Premium, Tableau Server, Google Looker Studio, Oracle BI Suite, SSAS, SSRS	Databases & Storage: Azure SQL, SQL Server, MySQL, CosmosDB, Elastic Search
Cloud & DevOps: Azure (end-to-end), Azure DevOps/TFS, Jira, Agile/SCRUM, OKR-driven DevOps	Programming & APIs: Python, Java/J2EE, Spark (PySpark), REST APIs, SpringBoot, Node.js

STARTUP : SATVIKHEALTH LLC
Satvik Health is a healthcare technology startup founded by Divya Prakash, focused on leveraging data intelligence to drive transformative outcomes in healthcare and benefits management. The company specializes in developing cutting-edge data products tailored to meet the unique needs of clients, with a team of seasoned Data and Analytics experts possessing extensive experience in the healthcare and benefits domain.

Unlocking healthcare excellence through Pure Data Insights

 Transforming Healthcare through data purity and deep insights. 

Get Started
About Satvik Health

Our Mission
 Satvik Health is dedicated to infusing purity and excellence into the US healthcare and insurance domain. Derived from the Sanskrit word meaning "Pure" or "Pious," our name reflects our commitment to integrity, quality, and innovation in every aspect of our operations.  

At Satvik Health, we are dedicated to providing top-notch Data & Analytics consulting services to our healthcare clients. Our mission is to help businesses of all sizes reach their full potential through the use of technology.
Empowering Innovation
  At Satvik Health, we are committed to driving innovation and empowering our clients with transformative solutions that redefine the future of healthcare and benefits management. Whether enabling AI/ML use cases, optimizing operational workflows, or facilitating community healthcare initiatives, we stand ready to partner with you on your journey towards excellence. 
Our Team
 At Satvik Health, we specialize in leveraging data intelligence to drive transformative outcomes in healthcare and benefits management. Our team comprises seasoned Data and Analytics experts with extensive experience in the healthcare data. With a deep understanding of clinical, healthcare claims and benefits data sets, we excel in developing cutting-edge data products tailored to meet the unique needs of our clients. 

Global Delivery Model 
Satvik Health operates with a global distributed delivery model, leveraging an offshore team based in Kolkata, India. This strategic approach allows us to optimize overall costs of implementations while ensuring high-quality deliverables and seamless collaboration across geographies. 

Products
Healthcare Claims Analytics Platform: Azure Databricks, DBT  data pipelines and PowerBI based Data & Analytics Platform that provides deep data insight into claims utilizations, enabling the identification of opportunities to optimize the cost of care. Leveraging Claims and encounters data sets, including Medical Claims, Rx Claims, Eligibility, condition, and encounter data, the platform standardizes and enriches data to provide actionable insights. 
MediSage EMR: MediSage is an Electronic Medical Record system built on Azure Power Apps & Dynamics. It enables a close-knit community of doctors/caregivers in Tier-2 and Tier-3 cities in India to streamline patient records, enhance collaboration, and improve healthcare delivery. 

Our Services
Data Product Development: We have a proven track record of building robust data products rooted in our comprehensive understanding of healthcare and benefits data. Our solutions are designed to empower organizations with actionable insights and strategic advantages. 
Cloud-Based Data Solutions: Satvik Health is at the forefront of cloud-based data and analytics platforms, utilizing technologies such as Azure Synapse, Databricks, and Microsoft Fabric to deliver scalable and efficient solutions. 
Business Intelligence: Leveraging the SQL BI suite, Power BI, and Tableau, we craft sophisticated business intelligence platforms that enable operational reporting and unlock the full potential of data-driven decision-making. 
Enterprise Data Lake and Analytics Platform: Our expertise lies in developing enterprise-grade data models that form the foundation of robust Analytics & BI platforms. These models facilitate seamless integration, efficient data management, and enhanced performance across diverse use cases. 
Cloud based Application Development : Satvik Health excels in application development using Azure Power Platform technologies, including Power Apps, MS Dynamics, and Microservices. Our team builds custom solutions that streamline processes, enhance user experience, and drive business growth. 
Data Integration and Exchange : We offer comprehensive data integration and exchange solutions using Electronic Data Interchange (EDI) formats. Our expertise facilitates seamless communication and interoperability between disparate systems, enabling efficient data exchange and collaboration across the healthcare ecosystem. 

"""

AGENT_SYSTEM_INSTRUCTION = f"""
You are an autonomous AI Professional Assistant representing Divya Prakash. 
Your target audience is executive recruiters. Answer all questions professionally, concisely, and accurately.
Strict Rule: Base your answers ONLY on the provided Background Profile Data. 
If an answer cannot be found in the text, politely respond: 'I am sorry, Divya's background data does not explicitly cover that, but you can schedule an interview to discuss it.'

Background Profile Data:
{MY_PROFILE_DATA}
"""

# ==========================================
# 2. AUTOMATED EMAIL ALERT TRIGGER
# ==========================================
def send_email_notification(recruiter_message):
    """Sends a hidden background email alert when a recruiter initializes a chat."""
    print("inside send_email_notification method")
    try:
        # Pull production environment secrets securely
        smtp_user = st.secrets["satvikhealth1@gmail.com"]          # Your Gmail address
        smtp_password = st.secrets["qgpn ghsf ttgi dazl"]  # Your Google App Password
        alert_receiver = st.secrets["divyaprakash03@gmail.com"] # Where you want to get notified
        
        # Configure standard secure email payload
        msg = MIMEText(f"Alert! A recruiter has started an AI chat.\n\nFirst Message Sent:\n\"{recruiter_message}\"")
        msg['Subject'] = "🚨 New Recruiter Activity on AI Portfolio Agent"
        msg['From'] = smtp_user
        msg['To'] = alert_receiver

        # Establish connection with Gmail's secure TLS server
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_mail(smtp_user, [alert_receiver], msg.as_string())
    except Exception as e:
        # Soft failure logs so the recruiter's UI session doesn't crash if email fails
        print(f"Background email failed: {e}")

# ==========================================
# 3. STREAMLIT APP ENGINE & UI
# ==========================================
st.set_page_config(page_title="Divya Prakash - AI Recruiter Agent", page_icon="🤖")
st.title("🤖 Chat with Divya's AI Recruiter Agent")
st.subheader("Ask anything about my background, career history, or skills.")

# Initialize conversation UI memory structure
if "messages" not in st.session_state:
    st.session_state.messages = []
if "email_sent" not in st.session_state:
    st.session_state.email_sent = False

# Render historic message log to the screen
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Capture live user chat interaction
if user_prompt := st.chat_input("Ask me about Divya's experience..."):
    # Immediately render recruiter question
    with st.chat_message("user"):
        st.markdown(user_prompt)
    st.session_state.messages.append({"role": "user", "content": user_prompt})

    # Trigger background email once on the very first message interaction
    if not st.session_state.email_sent:
        send_email_notification(user_prompt)
        st.session_state.email_sent = True

    # Call the new model engine using persistent chats
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        
        # --- SAFE INITIALIZATION LAYER ---
        try:
            # 1. Verify Client Instantiation
            if "genai_client" not in st.session_state:
                st.session_state.genai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
            
            # 2. Verify Chat Instance Creation
            if "gemini_chat" not in st.session_state:
                st.session_state.gemini_chat = st.session_state.genai_client.chats.create(
                    model="gemini-3.6-flash",
                    config=types.GenerateContentConfig(
                        system_instruction=AGENT_SYSTEM_INSTRUCTION
                    )
                )
        except Exception as init_error:
            # Captures and reveals the ACTUAL reason why Google AI failed to connect
            st.error(f"⚠️ Google Gemini Initialization Failed: {str(init_error)}")
            response_placeholder.markdown("Could not start chat engine due to a configuration error.")
            st.stop() # Halts processing cleanly so we don't hit attribute errors later

        # --- CHAT EXECUTION LAYER ---
        try:
            # Send message downstream to Google's live server endpoint
            response = st.session_state.gemini_chat.send_message(user_prompt)
            ai_response = response.text
            
            response_placeholder.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant", "content": ai_response})
        except Exception as chat_error:
            st.error(f"⚠️ Message Processing Failed: {str(chat_error)}")
            response_placeholder.markdown("My apologies, I ran into an error connecting to my database engine. Please try again.")            
