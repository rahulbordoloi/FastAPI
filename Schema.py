"""
Helps us to enforce type hints at runtime, and provides user friendly errors when data is invalid.
"""

# Importing Libraries
from pydantic import BaseModel


# Class BankNote which describes Bank Notes Features
class BankNote(BaseModel):

    variance: float
    skewness: float
    curtosis: float
    entropy: float
