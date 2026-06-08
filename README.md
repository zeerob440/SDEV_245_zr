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

#### Defending C
    - Encryption use encryption methods such as AES (Advanced Encryption Standard) or RSA (Rivest-Shamir-Adleman) AVOID DES (Data Encryption Standard).
    - VPN should be used
    - Access Control strict implementation should be designed.

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
    - Failover Contingency| have backup systems on the software and operational side of the enterprise. 
    - Prevent Bottlenecks| Manage traffic. 



