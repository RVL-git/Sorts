from dataclasses import dataclass

@dataclass
class Date:
    YYYY: int
    MM: int
    DD: int

    def __lt__(self, other):
        return (self.YYYY, self.MM, self.DD) < (other.YYYY, other.MM, other.DD)
    def __gt__(self, other):
        return (self.YYYY, self.MM, self.DD) > (other.YYYY, other.MM, other.DD)