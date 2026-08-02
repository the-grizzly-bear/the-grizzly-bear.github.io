# 8 SECURITY INCIDENT IDENTIFICATION (SCHEMA)

## VOCABULARY FOR EVENTS RECORDING AND INCIDENT SHARING (VERIS)

### GENERAL

Ref. [http://veriscommunity.net/](http://veriscommunity.net/)

Use this template to identify threats uniformly:

incident_id<br>#

<br>security_incident<br>Confirmed, Suspected, False positive, Near miss, No<br>confidence<br>High, Medium, Low, None<br><br>victim.employee_count<br>#<br><br>timeline.unit<br>Unknown, NA, Seconds, Minutes, Hours, Days, Weeks, Months, Years, Never<br><br>impact.overall_rating<br>Unknown, Insignificant, Distracting, Painful, Damaging, Catastrophic<br><br>impact.loss.variety<br>Asset and fraud, Brand damage, Business disruption, Operating costs, Legal and regulatory, Competitive advantage, Response and recovery<br><br>impact.loss.rating<br>Unknown, Major, Moderate, Minor, None<br>discovery_method<br>Unknown, <br>Ext - actor disclosure, <br>Ext - fraud detection, <br>Ext - monitoring service, Ext customer, <br>Ext - unrelated party, <br>Ext - audit, Ext unknown, <br>Int - antivirus, <br>Int - incident response,<br>Int - financial audit, <br>Int - fraud detection, <br>Int HIDS, <br>Int - IT audit, <br>Int - log review, <br>Int - NIDS,<br>Ext - law enforcement, <br>Int - security alarm, <br>Int reported by user, <br>Int - unknown,<br>Other<br><br>targeted<br>Unknown, Opportunistic, Targeted, NA<br><br>cost_corrective_action<br>Unknown, Simple and cheap, Difficult and expensive,<br>Something in-between<br><br>country<br>Unknown, Two Letter, Other<br><br>iso_currency_code<br>AED, AFN, ALL, AMD, ANG, AOA, ARS, AUD, AWG, AZN,<br>BAM, BBD, BDT, BGN, BHD, BIF, BMD, BND, BOB, BRL,<br>BSD, BTN, BWP, BYR, BZD, CAD, CDF, CHF, CLP, CNY,<br>COP, CRC, CUC, CUP, CVE, CZK, DJF, DKK, DOP, DZD,<br>EGP, ERN, ETB, EUR, FJD, FKP, GBP, GEL, GGP, GHS,<br>GIP, GMD, GNF, GTQ, GYD, HKD, HNL, HRK, HTG, HUF,<br>IDR, ILS, IMP, INR, IQD, IRR, ISK, JEP, JMD, JOD,<br>JPY, KES, KGS, KHR, KMF, KPW, KRW, KWD, KYD, KZT,<br>LAK, LBP, LKR, LRD, LSL, LTL, LVL, LYD, MAD, MDL,<br>MGA, MKD, MMK, MNT, MOP, MRO, MUR, MVR, MWK, MXN,<br>MYR, MZN, NAD, NGN, NIO, NOK, NPR, NZD, OMR, PAB,<br>PEN, PGK, PHP, PKR, PLN, PYG, QAR, RON, RSD, RUB,<br>RWF, SAR, SBD, SCR, SDG, SEK, SGD, SHP, SLL, SOS,<br>SPL, SRD, STD, SVC, SYP, SZL, THB, TJS, TMT, TND,<br>TOP, TRY, TTD, TVD, TWD, TZS, UAH, UGX, USD, UYU,<br>uzs, VEF, VND, vuv, WST, XAF, XCD, XDR, XOF, XPF,<br>YER, ZAR, ZMK, ZWD

### ACTOR

actor.x.motive<br>Unknown, NA, Espionage, Fear, Financial, Fun,<br>Grudge, Ideology, Convenience, Other

actor.external.variety<br>Unknown, Activist, Auditor, Competitor, Customer,<br>Force majeure, Former employee, Nation-state,<br>Organized crime, Acquaintance, State-affiliated,<br>Terrorist, Unaffiliated, Other

actor.internal.variety<br>Unknown, Auditor, Call center, Cashier, End-user,<br>Executive, Finance, Helpdesk, Human resources,<br>Maintenance, Manager, Guard, Developer, System<br>admin, Other

### ACTION

action.malware.variety<br>Unknown, Adware, Backdoor, Brute force, Capture app<br>data, Capture stored data, Client-side attack,<br>Click fraud, C2, Destroy data, Disable controls,<br>Dos, Downloader, Exploit vuln, Export data, Packet<br>sniffer, Password dumper, Ram scraper, Ransomware,<br>Rootkit, Scan network, Spam, Spyware/Keylogger, SQL<br>iniection, Adminware, Worm, Other

action.malware.vector<br>Unknown, Direct install, Download by malware, Email<br>autoexecute, Email link, Email attachment, Instant<br>messaging, Network propagation, Remote injection,<br>Removable media, Web drive-by, Web download, Other

action.hacking.variety<br>Unknown, Abuse of functionality, Brute force,<br>Buffer overflow, Cache poisoning, Session<br>prediction, CSRF, XSS, Cryptanalysis, DoS,<br>Footprinting, Foreed browsing, Format string<br>attack, Fuzz testing, HTTP request smuggling, HTTP<br>request splitting, HTTP response smuggling, HTTP<br>Response Splitting, Integer overflows, LDAP<br>injection, Mail command injection, MitM, Null byte<br>injection, Offline cracking, OS commanding, Path<br>traversal, RFI, Reverse engineering, Routing<br>detour, Session fixation, Session replay, Soap<br>array abuse, Special element injection, SQLi, SSI<br>injection, URL redirector abuse, Use of backdoor or<br>C2, Use of stolen creds, XML attribute blowup, XML<br>entity expansion, XML external entities, XML<br>injection, XPath injection, XQuery injection,<br>Virtual machine escape, Other

action.hacking.vector<br>Unknown, 3rd party desktop, Backdoor or C2, Desktop sharing, Physical access, Command shell, Partner, VPN, Web application, Other

action.social.variety<br>Unknown, Baiting, Bribery, Elicitation, Extortion, Forgery, Influence, Scam, Phishing, Pretexting, Propaganda, Spam, Other

action.social.vector<br>Unknown, Documents, Email, In-person, IM, Phone, Removable media, SMS, Social media, Software, Website, Other

action.social.target<br>Unknown, Auditor, Call center, Cashier, Customer,<br>End-user, Executive, Finance, Former employee,<br>Helpdesk, Human resources, Maintenance, Manager,<br>Partner, Guard, Developer, System admin, Other

action.misuse.variety<br>Knowledge abuse, Privilege abuse, Unknown, Embezzlement, Data mishandling, Email misuse, Net misuse, Illicit content, Unapproved workaround, Unapproved hardware, Unapproved software, Other

action.misuse.vector<br>Unknown, Physical access, LAN access, Remote access, Non-corporate, Other

action.physical.variety<br>Unknown, Assault, Sabotage, Snooping, Surveillance, Tampering, Theft, Wiretapping, Connection, Other

action.physical.location<br>Unknown, Partner facility, Partner vehicle, Personal residence, Personal vehicle, Public facility, Public vehicle, Victim secure area, Victim work area, Victim public area, Victim grounds, Other

action.physical.vector<br>Unknown, Privileged access, Visitor privileges, Bypassed controls, Disabled controls, Uncontrolled location, Other

action.error.variety<br>Unknown, Classification error, Data entry error,<br>Disposal error, Gaffe, Loss, Maintenance error,<br>Misconfiguration, Misdelivery, Misinformation,<br>Omission, Physical accidents, Capacity shortage,<br>Programming error, Publishing error, Malfunction,<br>Other

action.error.vector<br>Unknown, Random error, Carelessness, Inadequate<br>personnel, Inadequate processes, Inadequate<br>technology, Other

action.environmental.variety<br>Unknown, Deterioration, Earthquake, EMI, ESD,<br>Temperature, Fire, Flood, Hazmat, Humidity,<br>Hurricane, Ice, Landslide, Lightning, Meteorite,<br>Particulates, Pathogen, Power failure, Tornado,<br>Tsunami, Vermin, Volcano, Leak, Wind, Other

### ASSET

asset.variety<br>Unknown, S - Authentication, S - Backup, s Database, S - DHCP, S - Directory, S - DCS, s DNS, S - File, S - Log, S - Mail, S - Mainframe, S - Payment switch, S - POS controller, S - Print, S - Proxy, S - Remote access, S - SCADA, S - Web application, S - Code repository, S - VM host, s Other N - Access reader, N - Camera, N - Firewall, N - HSM, N - IDS N - Broadband, N - PBX, N Private WAN, N - PLC, N - Public WAN, N - RTU, N Router or switch, N - SAN, N - Telephone, N - VoIP adapter, N - LAN, N - WLAN, N - Other U - Auth token, U - Desktop, U - Laptop, U - Media, u Mobile phone, U - Peripheral, U - POS terminal, u Tablet, U - Telephone, U - VoIP phone, U - Other T - ATM, T - PED pad, T - Gas terminal, T - Kiosk, T - Other M - Tapes, M - Disk media, M - Documents, M - Flash drive, M - Disk drive, M - Smart card, M Payment card, M - Other P - System admin, p Auditor, P - Call center, P - Cashier, p Customer, P - Developer, P - End-user, p Executive, P - Finance, P - Former employee, P Guard, P - Helpdesk, P - Human resources, p Maintenance, P - Manager, P - Partner, P - Other

asset.accessibility<br>Unknown, External, Internal, Isolated, NA

asset.ownership<br>Unknown, Victim, Employee, Partner, Customer, NA

asset.management<br>Unknown, Internal, External, NA

asset.hosting<br>Unknown, Internal, External shared, External<br>dedicated, External, NA

asset.cloud<br>Unknown, Hypervisor, Partner application, Hosting<br>governance, Customer attack, Hosting

### ATTRIBUTE

attribute.confidentiality.data_disclosure<br>Unknown, Yes, Potentially, No

attribute.confidentiality.data.variety<br>Unknown, Credentials, Bank, Classified, Copyrighted,<br>Medical, Payment, Personal, Internal, System,<br>Secrets, Other

attribute.confidentiality.state<br>Unknown, Stored, Stored encrypted, Stored<br>unencrypted, Transmitted, Transmitted encrypted,<br>Transmitted unencrypted, Processed

attribute.integrity.variety<br>Unknown, Created account, Hardware tampering, Alter<br>behavior, Fraudulent transaction, Log tampering,<br>Misappropriation, Misrepresentation, Modify<br>configuration, Modify privileges, Modify data,<br>Software installation, Other

attribute.availability.variety<br>Unknown, Destruction, Loss, Interruption,<br>Degradation, Acceleration, Obscuration, Other

### COURSE OF ACTION

Structured Threat Information eXp ression (STIX™ )<br>(Adapted)

Ref. [https://stixproject.github.i](https://stixproject.github.i/)

coa.type<br>Blocking, Redirecting, Harden·mg Patching,<br>Rebuilding, Monitoring, Other

coa.impact<br>Insignificant, Distracting, Painful, Damaging,<br>Catastrophic, Unknown

coa.efficacy<br>Not Effective, Somewhat Effective, Mostly<br>Effective, Completely Effective, NA

coa.stage<br>Prepare, Remedy, Response, Recovered

coa.hosting<br>Unknown, Internal, External shared, Exte mal<br>dedicated, External, NA

coa.objective<br>Detect, Deny, Disrupt, Degrade Deceive, Destroy

### KILL CHAIN MAPPING

GATHER DATA FOR MAPPING KILL CHAIN

Ref. [http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-ntel-Driven­Defense.pdf](http://www.lockheedmartin.com/content/dam/lockheed/data/corporate/documents/LM-White-Paper-ntel-Driven%C2%ADDefense.pdf)

Phase<br>Active<br>Reconnaissance<br>Customization<br>Delivery<br>Exploitation<br>Installation<br>Command &<br>Control (C2)

Action on<br>Objectives

Identified evidence, artifact, info, or intet

Course of<br>Action

For Each Phase; Detect, Deny, Disrupt, Degrade, Deceive, Destroy

### PRIORITIZED DEFENDED ASSET LIST (PDAL)

GATHER DATA AND PRIORITIZE ASSETS TO DEFEND

Asset:<br>Location:<br>Criticality:<br>Deserioption:<br>Vulnerability:<br>Purpose:<br>Time Prioritized:<br>Recoverability:<br>Ranking:

Priority I

Asset:<br>Location:<br>Criticality:<br>Description:<br>Vulnerability:<br>Purpose:<br>Time Prioritized:<br>Recoverability:<br>Ranking:<br>Priority II

Asset:<br>Location:<br>Criticality:<br>Description:<br>Vulnerability:<br>Purpose:<br>Time Prioritized:<br>Recoverability:<br>Ranking:<br>Priority: III
