class Student:
    def _init_(self, name, final_exam_score, all_units_passed, cleared):
        self.name = name
        self.final_exam_score = final_exam_score  # Out of 100 or based on grading system
        self.all_units_passed = all_units_passed  # Boolean: True if no failed units
        self.cleared = cleared  # Boolean: True if fees & disciplinary issues cleared

    def is_eligible(self, pass_mark=50):
        
        #Checks if the student is eligible for graduation.
        
        if self.final_exam_score >= pass_mark and self.all_units_passed and self.cleared:
            return True, f"Congratulations, {self.name}! You are eligible for graduation."

        reasons = []
        if self.final_exam_score < pass_mark:
            reasons.append(f"Low final exam score ({self.final_exam_score}/{pass_mark}).")
        if not self.all_units_passed:
            reasons.append("Not all required units have been passed.")
        if not self.cleared:
            reasons.append("Pending clearance (fees, disciplinary issues).")

        return False, f"Sorry, {self.name}. You are not eligible for graduation. Reasons: " + ", ".join(reasons)

# Example Usage
student1 = Student("Mwangi", 72, True, True)
student2 = Student("Akinyi", 48, True, False)  # Failed due to low score and uncleared fees

eligibility1, message1 = student1.is_eligible()
eligibility2, message2 = student2.is_eligible()

print(message1)  # Mwangi should be eligible
print(message2)  # Akinyi should not be eligible