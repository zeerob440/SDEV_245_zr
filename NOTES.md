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

## MODULE 2

### CRYPTOGRAPHY

cryptography is the foundation of cybersecurity. It has been around for a long time. Encryption cna be used to make dat more transferable with pedestrian hardware, such as Morse Code. WW2 saw encrypted military hardware such as the "Turing Machine and "Enigma Machine".

#### TYPE OF CRYPTOGRAPHY

1. Plain Text - not encrypted data. 
2. Cipher Text - unprocessed it is unreadable. Once processed through a key it is a readable plain text message
3. Encryption - the process of turning plain text into cipher text.
4. Key - the function that processes plain text into cipher text. this function is know as the key
5. Decryption - the function that turns cipher text into readable plain text.

Think of the encryption process and the encryption key as the lock; the decryption process and the decryption key as the unlocked state. 

#### Encryption Decryption process
-plain text->encryption->cipher text-> decryption->-plain text.

#### Applying Cryptography to Software Engineering

1. select encryption methodology
    * RSA (Rivest Shamir Adelman)
    - uses Public Key and Private key to encrypt and decrypt
    - plain text -> public key -> encrypt -> Cipher text -> Private Key -> decrypt -> plain text
    * AES (Advanced Encryption Standard)
    - same key is used to encrypt/decrypt data. 
    - ASIP encryption is closer to AES encryption than RAS encryption.

2. functions transform plain text to cipher text.

3. decryption keys convert cipher text to plain text. 

#### cryptographic techniques

Cryptography consists of three major categories:

1. Symmetric Key Cryptography
   - Uses a single shared secret key.
   - Example: AES.
   - plain text > secret key encryption > cipher text > secret key decryption > plain text
   - faster than asymmetric encryption.
   - less secure than Asymmetric encryption
   - use for larger data sets

2. Asymmetric Key Cryptography
   - Uses a public key and a private key.
   - Example: RSA.
   - plain text > public key encryption > cipher text > private key decryption > plain text.
   - computationally expensive
   - use for smaller datasets

3. Hash Functions
   - One-way mathematical functions used to verify integrity and securely store data.
   - generates unique fixed length string, know as HASH VALUE
   - Examples: SHA-256, SHA-512.
   - plain text > hash function > hashed text.

#### other cryptography algorithms

1. Secure Hash Algorithm (SHA)
    - uses fixed length HASH VALUES.
    - used for verifying data integrity and authenticity.

2. Elliptical Curve Cryptography (ECC)
    - used math ellipses to create faster smaller keys.
    - used on pedestrian hardware such as mobile devices and smart cards.
    - promising for IoT devices.

3. Quantum Cryptography
    - undecipherable by conventional machines
    - anyone who claims to understand it is probably lying.

4. Data Encryption Standard (DES)
    - "It is an older code sir, but it still checks out."
    - US Standard in 1977, probably used to encrypt Bee Gees lyrics.
    - uses 64 bit plain text blocks, returns a 64-bit cipher text
    - generates a sub key > encrypts it

### Known Cryptography Attack Vectors

| Attack Type | Attacker Knows / Controls | Goal | Example |
|--------------|--------------------------|------|---------|
| **Brute Force** | Tries every possible key | Find the key | Password cracking |
| **Ciphertext-Only Attack** | Ciphertext only | Recover plaintext or key | Sniffing encrypted traffic |
| **Known Plaintext Attack** | Plaintext and matching ciphertext | Deduce the key | WWII codebreaking |
| **Chosen Plaintext Attack** | Attacker chooses plaintext and observes ciphertext | Analyze cipher and recover key | Cryptographic experiments |
| **Chosen Ciphertext Attack** | Attacker chooses ciphertext and observes decrypted plaintext | Recover the key or exploit weaknesses | Early RSA attacks |
| **Differential Cryptanalysis** | Differences between plaintexts and ciphertexts | Discover the key by analyzing output differences | DES analysis |

### Ordered from Least to Most Powerful Attacker

1. **Brute Force**
2. **Ciphertext-Only Attack**
3. **Known Plaintext Attack**
4. **Chosen Plaintext Attack**
5. **Chosen Ciphertext Attack**
6. **Differential Cryptanalysis**

### Memory Aid

| Attack | Think |
|----------|-------|
| **Brute Force** | Try everything |
| **Ciphertext-Only** | See encrypted messages |
| **Known Plaintext** | Know some message contents |
| **Chosen Plaintext** | Choose what gets encrypted |
| **Chosen Ciphertext** | Choose what gets decrypted |
| **Differential Cryptanalysis** | Compare differences |

### Key Idea

> The more information and control an attacker has, the easier it becomes to recover the key or decrypt messages.

### PUBLIC KEY INFRASTRUCTURE (PKI)

PKI is intended for internet application security.

PKI is a framework for assigning identity to users through digital certificates. when paired with public key cryptography.

#### Components of PKI

1. Certificate Authority (CA)
CA uses its own private key to validate digital certificates that can be verified through a requested public key.
    - trusted entity
    * Issues digital certificate (X.509 Certificate)
    * Stores digital certificate
    * signs digital cartificate
2. Registration Authority (RA)
    - The RA verifies the identity of the user or device requesting the digital certificate. This can be a third party, or the CA can also act as the RA
3. Certificate database 
    - database stores digital certificates. 
4. Central directory
    - A secure location that used for storing and indexing cryptographic keys
5. Certificate management system
    A set of protocols for managing digital certificates this includes
    - access
    - creation
    - storage
    - distribution
    - revocation
6. Certificate policy
    - A publicly accessible policy detailing the PKI’s procedures and standards. Third parties can use the certificate policy to assess the trustworthiness of the PKI.

In actionable language PKI is the framework that allows something like a bank verify that the users' requesting authorization is the actual user, verifies via digtal certificate then allows or denies entry.

#### Transport Security Layer (TLS)
    TLS uses cryptographic algorithms to establish protected connections between web browsers and servers.

#### Creating new digital certificate process
- private key is created and given to a certificate recipient for the private key owner
- the CA requests and vets any identifying info for private key owner
- the Public key and identifying attributes are encoded into a certificate signing request (CSR)
- the key owner signs the CSR to prove possession is private.
- the CA validates the request and signs the digital certificate with the CA's private key. 

### open source PKI

1. openSSL
    - most python friendly
    - library == 'ssl'
    - enterprise grade

### Database encryption

long keys might reduce the number of possible active sessions.

#### common methods

1. API Method
    - app level
    - queries are within encrypted columns and modified in the app
2. Plug-In Method
    - encryption module is attached to the DBMS
3. Transparent Data Encryption Method (TDS) 
    - executes encryption/decryption inside the database engine
    - easier to manage.


#### Transparent Database Encryption
- type of external encryption
- refers to entire database encryption
- is 'invisible' because users cannot see the encryption

### database encryption levels
1. cell level - each cell has it's own password
    * use when high-level of security is needed.
2. column level- each column has its own password
    * most common database encryption
3. Tablespace level
    * encrypts across tables
    * does not have high impact on database performance
4. File Level
    * this method scrambles entire files
    * this method may degrade database performance.

#### datbase encryption methods
1. AES
2. RAS
3. 3DES (triple data encryption)
    - 56 bit keys
    - encrypts data up to 3 times
    - depreciating
4. Twofish
    - symmetric block cipher
    - 128-256 bit
    - flexible license-free
    - encrypts 16 times always

### how does HTTPS work

- https uses public and private keys and PKI infrastructure

## Module 3 notes

### Randomness

1. Entropy is the measure of randomness
    * the more entropic a seed is the higher the security a system has
    * seed() in python
    * seed seed() with something cosmically random like time to generate keys

2. Deterministic Random Bit Generators (DRBG), predictable, underlying complex pattern
    * random() in python
    * produces prandom values
    * sequence is dependent on initial seed.

3. Cosmic Randomness- unpredictable, no apparent pattern
    * mouse movements
    * user activity
    * cpu jitter

Therefore, the initial seed value should be produced from some cosmically random value

3. weak entropy
    * weak keys generated by a deterministic seed
    * identical keys
    * compromised security

4. AES-256
    * uses 256-bits of entropy
    * each bit is cosmically random

### How to get cosmic randomness

random seed values that produce keys should be obtained from something cosmically random. The most cosmically random entity on a computer is the user, the OS acts as the handler for cosmically random behavior between  cosmically random user behavior, such as user inputs, and the deterministic behavior of machines.

1. OpenBSD Kernel
    * integrated cryptography
    * focus on high entropy randomness.
    * created in 2011, produces large amounts of randomness.

2. Linux
    * a cult primarily.
    * provides random files such as
        - /dev/random
        - /dev/urandom
        - /dev/hw_random
    * Supports Hardware TRNGs 
        - rng tools, linux software package, feeds entropy pool
        - RDRAND, AMD CPU instruction, provides random number
        - Trusted Platform Module (TPM), Hardware, security chip; secure key storage, randnum generator etc

3. Solaris
    * for linux machines
    * supports /dev/random and /dev/urandom
    * admins can add other entropy seeds. 

4. Windows

