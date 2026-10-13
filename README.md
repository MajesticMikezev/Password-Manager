# Password Manager

**A secure, self-hosted, Docker-based password manager**

Password Manager is a source-available project being developed from scratch to provide a privacy-focused solution for securely storing, managing, and accessing passwords.

Built with modern technologies and designed around client-side encryption, the application aims to give users control over their credentials and personal data without relying on third-party password storage services.

> **Development Notice**
>
> This project is currently in early development and is not ready for production use. Security features are planned but have not yet been fully implemented or independently audited. Do not store real passwords or sensitive credentials in the application.

---

## About the Project

Password Manager aims to provide a secure, easy-to-use alternative to cloud-hosted password management services.

The application is designed to run entirely within Docker containers, making deployment and management straightforward across different operating systems and self-hosted environments.

The initial focus is on providing individuals and families with separate, encrypted password vaults.

### 🎯 Project Goals

* **Privacy First:** Keep sensitive credentials encrypted and under the user's control.
* **Self-Hosted:** Allow users to host their own password manager.
* **Security Focused:** Use established encryption algorithms and security best practices.
* **Multi-User Support:** Provide individual, private vaults for family members.
* **Easy Deployment:** Simplify installation and management through Docker.
* **Cross-Platform:** Support access through modern web browsers.
* **Expandable:** Build a foundation for browser extensions and mobile applications.

---

## Planned Features

### Security & Encryption

* Client-side AES-256-GCM encryption
* Argon2id master password key derivation
* Zero-knowledge vault architecture
* Secure user authentication
* Two-factor authentication (2FA)
* Automatic vault locking
* Secure session management
* Encrypted database storage
* Encrypted backup and recovery options

### Password Management

* Secure password storage
* Password generator
* Password strength indicators
* Password folders and categories
* Search and filtering
* Favourite passwords
* Secure notes
* Copy usernames and passwords
* Password editing and deletion

### User Management

* Multiple user accounts
* Individual encrypted vaults
* Account settings
* Master password management
* Session management
* Family account support

### Self-Hosting

* Docker-based deployment
* Docker Compose configuration
* PostgreSQL database
* HTTPS support
* Persistent data storage
* Configurable environment variables
* Backup and restoration procedures

### How It Will Work

1. Users access the password manager through their web browser.
2. Users authenticate and unlock their encrypted vault locally.
3. Passwords are encrypted in the browser before being transmitted.
4. The backend handles authentication, encrypted storage, and synchronisation.
5. PostgreSQL stores encrypted vault records.
6. Credentials are decrypted locally when accessed by an authorised user.

The intended architecture ensures that the server does not require access to plaintext vault credentials or master passwords.

---

## Installation

### Prerequisites

The following software will be required:

* Docker
* Docker Compose
* Git

### Installation Instructions

Docker installation and configuration instructions will be provided once the initial application infrastructure has been implemented.

**Current Status:** Installation is not yet available.

---

## Security

Security is a primary objective of this project.

The application is intended to use established cryptographic standards and client-side encryption to protect sensitive credentials.

### Security Principles

**Client-Side Encryption**

Credentials will be encrypted before leaving the user's device.

**Zero-Knowledge Design**

The server will not require access to master passwords or decrypted vault contents.

**Authenticated Encryption**

AES-256-GCM will be used to provide confidentiality and integrity protection for vault data.

**Secure Key Derivation**

Argon2id will be used to derive cryptographic keys from master passwords.

**Secure Communication**

HTTPS will protect communication between clients and the server.

**Security Testing**

Authentication, encryption, access controls, and recovery mechanisms will undergo testing throughout development.

> **Security Disclaimer:** These are design objectives, not claims that the current application has implemented or verified these protections.

---

## Feedback & Contributions

Bug reports, security findings, feature suggestions, and general feedback are welcome.

However, this project is proprietary and source-available rather than open-source.

Modification, redistribution, and commercial use of the software are restricted under the project's licence.

Submitting a suggestion or contribution does not automatically grant permission to modify or redistribute the software.

Code contributions should be discussed with the copyright holder before submission. Any accepted contributions may require a separate written agreement.

---

## License & Copyright

**Copyright © 2026 [Michail Zevlaris]. All Rights Reserved.**

This project is distributed under a custom **Free Personal Use License**.

The original author retains copyright ownership of the software and its original source code.

### Permitted Use

Individuals and families are permitted to:

* Download the software free of charge.
* Install and run the application.
* Self-host the password manager.
* Use the application for personal, non-commercial purposes.
* View the publicly available source code for educational and security review purposes.

### Restricted Use

Without prior written permission from the copyright holder, users may not:

* Redistribute or republish the software.
* Sell, sublicense, or commercially exploit the software.
* Modify or distribute modified versions.
* Incorporate the software into commercial products or services.
* Remove or alter copyright notices.
* Claim ownership or authorship of the original software.

### Ownership

All copyright in the author's original work remains with the copyright holder.

Third-party components and contributions remain subject to their respective ownership and licensing terms.

**This project is not open-source software as defined by the Open Source Initiative.**

For the complete licensing terms, please refer to the [LICENSE](LICENSE) file.

---

## Disclaimer

This software is currently experimental and under active development.

It is provided **"AS IS"**, without warranty of any kind, to the extent permitted by applicable law.

The author makes no guarantees regarding the security, reliability, availability, or suitability of the application.

Users should not rely on this software for storing sensitive credentials until the necessary security controls have been implemented, tested, and independently reviewed.

---

## Project Status

** Early Development — Version 0.1.0 (Planned)**

The project is currently focused on establishing its Docker infrastructure, backend API, database, and frontend foundation.

Features and documentation will be updated as development progresses.

---
