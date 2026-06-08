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

2. I is INTEGRITY, data should be unaltered. threat vectors include:
    - Data tampering| spoofed data altered data inserted by attackers.
    - Malware & Ransomware

#### Defending I 
    -  Hash Functions; MDA5 or SHA Family (SHA-1 - SHA 5)

This functions as HOST A sends data > Attach Hash > HOST B verifies data > hashes are compared if == integrity preserved ELSE data is altered.

3. A is AVAILABILITY, threat vectors include
    - DoS and DDoS attacks

#### Defending A
    - Hardware maintenance| upgrade hardware before EOSL
    - Regular Upgrades| Keep software updated.
    - Failover Contingency| AKA Disaster Recovery Plans. Have backup systems on the software and operational side of the enterprise. 
    - Prevent Bottlenecks| Manage traffic. 

### Authentication Vs Authorization

1. Authentication| 'Who are you?'
    - confirms identity of users.
    - establishes the legitimacy of users
    - passwords, biometrics, tokens.
    - it tries to confirm that a virtual identity corresponds with a physical identity.

Common Authentication Protocols
    * OAuth
    * OpenID
    * SAML

Authentication Methods Factors TTPs
    * Knowledge Factor| PINs, security questions
    * Possession Req| authenticator apps, Smartcards,      tokens
    * Inherence Factor| biometrics
    * SFA| only one authentication factor is needed passwords for example
    * 2fa| two factors are needed, password + auth app
    * mfa| many factors are needed
    * Adaptive Authentication| uses user behavior as an authentication factor. such as locations like getting locked out of Linkedin because nothing I own touches the Internet with out VPN active. 

Authentication CSEC attack vectors
    * passwords
    * Phishing
    * Credential theft| malware, Keyloggers
    * Account lockouts| burns out helpdesk 
    * Credential Stuffing| spoofed data added to a legitimate 
    * MFA absenteeism| no MFA
    * Depreciated legacy systems|     



2. Authorization 'What are you allowed to do?'
    - grants or denies access for users with that are expected in the system.
    - it authorizes users by attributes such as roles and permissions



Common Authorization Protocols
    - RBAC (Role-Based Access Control)
    - ABAC (Attribute-Based Access Control)

Authorization TTPs 
    * Identity| determines if user has correct credentials to access areas of the system. 
    * Context| permissions are determined by other factors such as time of day or location. 
    * RBAC| Role-based, users with a given role within a system can access specific parts of the system. If/elif/else logic
    * ABAC| Users with specific attributes associated with their class instance, are granted specif permissions. 
    * Rules-Based Auth| Like granting roles in Everbridge. Each role is configured to a specif type of user. 

Authorization CSEC Concerns
    * Too much access
    * too little access
    * Role Creep| my current job
    * Inconsistent Role Definitions
    * Access Control misconfiguration: semantic and logic errors in user class
    

