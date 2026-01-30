import pytest
from src.dispense import DispenseEvent, invariant_holds

# 1. Test Constraint: Rejecting non-positive doses (Requirement 1)
def test_requirement_positive_dose():
    with pytest.raises(ValueError, match="Dose must be a positive value"):
        DispenseEvent("P001", "Advil", -50, 1)

# 2. Test Constraint: Rejecting non-integer/zero quantities (Requirement 2)
def test_requirement_positive_integer_quantity():
    with pytest.raises(ValueError, match="Quantity must be a positive integer"):
        DispenseEvent("P001", "Advil", 200, 0)

# 3. Test Invariant: Preventing duplicate medication for a patient (Requirement 4)
def test_requirement_no_duplicate_dispensing():
    event1 = DispenseEvent("P123", "Tylenol", 500, 1)
    existing_log = [event1]
    
    # Propose a second dispense for the same medication to the same patient
    new_event = DispenseEvent("P123", "Tylenol", 500, 1)
    
    assert invariant_holds(existing_log, new_event) is False
