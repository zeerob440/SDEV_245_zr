# SDEV-245 Repo

Repo is for learning secure coding techniques.

# Notes

## Module 1

### CIA Triad

    - CIA Triad is the fundamental acronym for cyber security threat vectors.

1. C is CONFIDENTIALITY,opsec data should only be accessed by authroized users threat vectors include:
    - Unauthorized Access
    - Weak encryption
    - insider threats (disgruntled staff).
    - Man in the middle attacks (MITM)

#### Defending C
    - Encryption use encryption methods such as AES (Advanced Encryption Standard) or RSA (Rivest-Shamir-Adleman) AVOID DES (Data Encryption Standard).
    - VPN should be used
    - Access Control strict implementation should be designed.
    - MFA should be used. 

1. I is INTEGRITY, data should be unaltered. threat vectors include:
    - Data tampering| spoofed data altered data inserted by attackers.
    - Malware & Ransomware

#### Defending I 
    -  Hash Functions; MDA5 or SHA Family (SHA-1 - SHA 5)

This functions as HOST A sends data > Attach Hash > HOST B verifies data > hashes are compared if == integrity preserved ELSE data is altered.

1. A is AVAILABILITY, threat vectors include
    - DoS and DDoS attacks

#### Defending A
    - Hardware maintenance| upgrade hardware before EOSL
    - Regular Upgrades| Keep software updated.
    - Failover Contingency| AKA Disaster Recovery Plans. Have backup systems on the software and operational side of the enterprise. 
    - Prevent Bottlenecks| Manage traffic. 

### Authentication Vs Authorization

2. Authentication| 'Who are you?'
    - confirms identity of users.
    - establishes the legitimacy of users
    - passwords, biometrics, tokens.
    - it tries to confirm that a virtual identity corresponds with a physical identity.

2. Common Authentication Protocols
    * OAuth
    * OpenID
    * SAML

2. Authentication Methods Factors TTPs
    * Knowledge Factor| PINs, security questions
    * Possession Req| authenticator apps, Smartcards,      tokens
    * Inherence Factor| biometrics
    * SFA| only one authentication factor is needed passwords for example
    * 2fa| two factors are needed, password + auth app
    * mfa| many factors are needed
    * Adaptive Authentication| uses user behavior as an authentication factor. such as locations like getting locked out of Linkedin because nothing I own touches the Internet with out VPN active. 

2. Authentication CSEC attack vectors
    * passwords
    * Phishing
    * Credential theft| malware, Keyloggers
    * Account lockouts| burns out helpdesk 
    * Credential Stuffing| spoofed data added to a legitimate 
    * MFA absenteeism| no MFA
    * Depreciated legacy systems|     



3. Authorization 'What are you allowed to do?'
    - grants or denies access for users with that are expected in the system.
    - it authorizes users by attributes such as roles and permissions



3. Common Authorization Protocols
    - RBAC (Role-Based Access Control)
    - ABAC (Attribute-Based Access Control)

3. Authorization TTPs 
    * Identity| determines if user has correct credentials to access areas of the system. 
    * Context| permissions are determined by other factors such as time of day or location. 
    * RBAC| Role-based, users with a given role within a system can access specific parts of the system. If/elif/else logic
    * ABAC| Users with specific attributes associated with their class instance, are granted specif permissions. 
    * Rules-Based Auth| Like granting roles in Everbridge. Each role is configured to a specif type of user. 

3. Authorization CSEC Concerns
    * Too much access
    * too little access
    * Role Creep| my current job
    * Inconsistent Role Definitions
    * Access Control misconfiguration: semantic and logic errors in user class

### Access Control

#### Access Control Types
4. There are two kinds of Access control.
    * Physical| physical spaces
    * logical|intangible places like software. 
 
4. Access Control Concepts
    * Identity 'Who are you?' 
    * AuthT 'What are you?'
    * AuthZ 'What can you access within?'
    * Principle of Least Privilege 'Need to know basis.' 
    * Principal of Separation of Duties|(like nuclear codes, multiple people need to do something in order for a request to process)
    * Access Control List| (ACL) User class instances are granted access to specific functions such as read or write, or other operations.
    * Capabilities| access granted via password, token or smart card. 
    * Discretionary Access Control| (DAC) access granted by owner of resource. This is determined by business rules or how the owner is feeling on a particular day.
    * Mandatory Access Control| (MAC) A group of people or individual decide who has access, access is often defined in tiers. Often used by govt entities. 

    ### Audit, logging, access control events.

    Logging access control events involves capturing information such as user login attempts, resource access requests, permission changes, and access denials. These logs can be used for security analysis, forensic investigations, and compliance auditing.

    Auditing logging: allows developers to monitor user activity on during logging instances, thereby alerting the team of unexpected access attempts, unauthorized access and other security risks. 




    

