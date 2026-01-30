class DispenseEvent:
    # Rule 3: Example maximum daily doses per medication
    MAX_DAILY_DOSES = {
        "Aspirin": 4000,
        "Advil": 1200,
        "Tylenol": 4000
    }

    def __init__(self, patient_id, medication, dose_mg, quantity):
        
        # Rule 1: Dose must be a positive value
        if dose_mg <= 0:
            raise ValueError("Dose must be a positive value.")
        
        # Rule 2: Quantity must be a positive integer
        if not isinstance(quantity, int) or quantity <= 0:
            raise ValueError("Quantity must be a positive integer.")
            
        # Rule 3: Check against maximum allowable dose
        if medication in self.MAX_DAILY_DOSES:
            if dose_mg > self.MAX_DAILY_DOSES[medication]:
                raise ValueError(f"Dose exceeds maximum allowable for {medication}.")

        self.patient_id = patient_id
        self.medication = medication
        self.dose_mg = dose_mg
        self.quantity = quantity

def invariant_holds(existing_events, new_event):

    for event in existing_events:
        if (event.patient_id == new_event.patient_id and 
            event.medication == new_event.medication):
            return False  # Invariant violated: duplicate found
    return True
