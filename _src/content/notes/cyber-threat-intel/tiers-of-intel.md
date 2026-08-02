# Tiers of Intel

### Prioritization in Threat Hunting
Items are prioritized in a tiered system. Items within each tier are not listed in a specific order. The focus is on addressing higher-tier items first; as resources become available and higher-tier items are resolved, attention can shift to lower-tier items.

### Tier 3 (Highest Priority)
- **Critical CVEs**
	- Urgent Common Vulnerabilities and Exposures requiring immediate action.
	- Publicly available POCs increasing risk.
- **TLB:AMBER or Specific Advisories**
	- Trusted advisories labeled as TLP:AMBER, indicating sensitive information for limited distribution.
- **Zero-Day/Non-Disclosed Vulnerabilities**
	- Newly discovered vulnerabilities not yet publicly disclosed or patched.
- **Impending Doom**
	- Indicators of imminent and severe threats to critical systems.
- **High-Fidelity IOCs/IOAs/Threats**
	- Highly reliable Indicators of Compromise (IOCs), Indicators of Attack (IOAs), or specific threats that necessitate swift response.

### Tier 2 (Medium Priority)
- **Higher Business Impact Items**
	- Advisories from organizations like CISA (Cybersecurity and Infrastructure Security Agency).
	- Impacts on Industrial Control Systems (ICS).
- **Solid or Newer TTPs**
	- Recently identified or well-established Tactics, Techniques, and Procedures.
- **Emerging Threats**
	- New threats that are starting to surface and may affect operations.
- **Higher-Tier Threat Intelligence**
	- **Curated Intelligence**
		- Carefully selected and analyzed intel reports.
	- **Penetration Test Reviews**
		- Assessments of vulnerabilities identified during penetration testing.
- **Tech Stacks Across Customers**
	- Common technology platforms used by multiple clients that could be targeted.
- **Industry Vertical Threats**
	- Threats specific to certain industries or sectors.
- **Customer Matches Files and Dumps**
	- Discovery of customer data in leaked files or data dumps.
- **Reviewing Increases in Brute Force or New Activity**
	- Monitoring spikes in attack attempts or unusual behaviors.

### Tier 1 (Lowest Priority)
- **Pulse/IOC Reviews**
	- Regular examination of threat feeds and indicators.
- **Low-Tier/Blog/Open-Source Intelligence (OSINT) Hunts**
	- Investigations based on blogs, forums, and publicly available information.
- **Reviewing Older Malware**
	- Analysis of outdated malware that might still pose risks.

---

**Note:**
- **Increased Data Fidelity with CSINT:** As organizations move from Open-Source Intelligence (OSINT) to Closed-Source Intelligence (CSINT), the data obtained has higher fidelity and accuracy.
	- **Challenges for Threat Actors:** This shift from OSINT to CSINT largely makes it more difficult for threat actors to access or adapt to known security measures, enhancing the organization's defense against potential threats.
- **Tier Levels:**
	- **Tier 3**: Represents the most critical threats that require immediate attention and resources.
	- **Tier 2**: Includes significant threats that are important but less urgent than Tier 3.
	- **Tier 1**: Consists of routine or lower-priority items that can be addressed as resources permit.

**Understanding the Logic:**
- **Resource Allocation:**
	- Higher-tier items consume more resources due to their urgency and impact.
	- Once higher-tier items are managed, resources can be reallocated to address lower-tier items.

*[image unavailable]*
