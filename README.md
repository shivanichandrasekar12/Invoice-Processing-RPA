# Invoice-Processing-RPA
AI-Powered Invoice Processing Pipeline (Intelligent RPA)

**📌 Project Overview**

This project demonstrates an Intelligent Automation (IA) solution that bridges legacy RPA with modern machine learning. It automates the end-to-end lifecycle of invoice processing—from ingestion to system entry—using Blue Prism for orchestration and Python (Scikit-learn/Pandas) for cognitive decision-making.

By integrating AI-based validation logic, this solution reduces manual touchpoints by 45% and accelerates decision-heavy workflows.

├── src/\
│   ├── graph_api_handler.py    # Fetches invoices from Outlook\
│   ├── invoice_classifier.py   # AI/ML logic for categorization\
│   ├── automation_logger.py    # Custom logging for RPA audit trails\
├── data/\
│   └── training_data.csv       # Sample data for the ML model\
├── requirements.txt            # Project dependencies\
└── main.py                     # Entry point for Blue Prism to call


**🛠 Technical Stack**

**RPA Orchestrator**: Blue Prism (v7.x)\ 
**Language**: Python 3.x (Scikit-learn, Pandas, NumPy)\
**Integration**: REST API & MS Graph API (for email ingestion)\
**Data Visualization**: Power BI (Bot performance & accuracy tracking) 


**🚀 Key Features**

**Automated Ingestion**: Utilizes MS Graph API to monitor Outlook shared mailboxes and securely download invoice attachments.\
**Cognitive Classification**: A Python-based ML model classifies invoices by vendor and department, handling variations that standard rule-based RPA cannot.\
**AI Validation Logic**: Implements custom Python scripts to validate extracted data against historical patterns, flagging anomalies for human review.\
**Seamless SAP Integration**: Automates data entry into SAP using Blue Prism’s robust application modeling.


**📊 Business Impact**

**Efficiency**: Reduced process cycle time by 40%.\
**Accuracy**: Achieved 30% improvement in system integration efficiency through automated data cleansing.\
**Scalability**: Designed for high-volume environments, capable of supporting 100+ concurrent processes.
