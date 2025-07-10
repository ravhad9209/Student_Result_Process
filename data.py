from dataclasses import dataclass, field
from typing import List

@dataclass
class Student:
    stud_id: int 
    name: str
    age: int
    marks: int
    address: str
    subjects: List[str] = field(default_factory=list)

    def is_passed(self, passing_marks: int = ) -> bool:
        return self.marks >= passing_marks

    def add_subject(self, subject: str):
        if subject not in self.subjects:
            self.subjects.append(subject)

