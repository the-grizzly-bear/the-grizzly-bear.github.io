# Definitions of Findings from Threat Hunts

**Findings**
- **Activity Requiring Further Investigation**: Results from a query that warrant additional analysis and verification.
- **Verification Processes**: Any subsequent review to validate observed activity is considered a finding, even if it ultimately results in a false positive. This includes existing investigations, penetration tests, and similar activities.
- **No Guarantee of True Positives**: Findings do not necessarily indicate a true positive detection.
- **True Positives as Specific Findings**: A true positive represents a detection, which is a more specific category of finding.
- **Indicators of Potential Compromise**: Signs suggesting some form of security breach or compromise.
- **Risk Factors for Customer Compromise**: Information that could lead to a customer's compromise, such as exposed credentials, unpatched vulnerabilities, or poor security practices.
- **Suspicious Behavior**: Activities that are suspicious but not strictly classified under true positive or false positive categories.
- **Higher Likelihood of False Positives**: Findings are more likely to be deemed false positives or legitimate activities rather than malicious.
- **Customer Communication**: Involves informing the customer, requesting additional information, or validating specific items.

**No Findings**
- **Absence of Results**: No results from queries or searches based on the criteria of the hypothesis.
- **Overly Broad Queries**: Queries that are too expansive, which invalidates their utility for the hunt.
- **Invalid False Positives**: False positives arising from illegitimate or invalid Indicators of Compromise (IOCs).

**Evaluating Information for Higher Quality Findings**
- **Assessing Query Effectiveness**: Determine whether the query is well-constructed and appropriate for the investigation. IF we run a query across a data source that doesn't exist, there would never be any findings.
- **Relevance of Data Sources**: Consider the age of an OSINT credential dump and the likelihood that it can be correlated effectively.
- **Managing Query Scope**: Recognize that a query may initially seem well-defined but could yield an excessive number of results; identify at what point a query becomes too large to be effective.
- **Determining Sufficient Criteria for Pivoting**: Decide what is adequate to pivot the investigation, continuing until the hypothesis is disproven or the query becomes insufficient for the hunt due to constraints.
