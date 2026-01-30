<Must the dose_mg be a positive numerical value?, Constraint> 
Justification: This restricts the domain of a specific input variable to prevent physically impossible data entry.

<Is there a maximum allowable dose for specific medications?, Constraint> 
Justification: This defines a specific upper bound or limit that an individual input must not exceed for safety reasons.

<Can a patient receive the same medication twice in one day?, Invariant>
Justification: This is a system-wide consistency rule, the state of the database must always reflect that no duplicates exist for a patient per day.

<Should the system generate a confirmation log after each dispense?, Functional Requirement> 
Justification: This describes a specific action or behavior the system must perform.

<Must the patient_id follow a specific 9-digit format?, Constraint> 
Justification: This is a formatting restriction on the input data to ensure compatibility with existing pharmacy records.

<Does the system need to verify the dispensing pharmacist's credentials?, Functional Requirement> 
Justification: This describes a functional process or service the system provides to ensure authorized access.

<Can the total quantity dispensed ever exceed the pharmacy's current stock?, Invariant> 
Justification: This is a state property that must remain true across the entire system, you cannot dispense what does not exist.

<Must medication names be selected from a pre-approved list?, Constraint> 
Justification: This restricts the medication input to a specific, predefined list of valid strings.
