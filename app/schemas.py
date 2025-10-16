from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any

class Invoice(BaseModel):
    id: str = Field(..., description='Invoice identifier')
    amount: float
    metadata: Optional[Dict[str, Any]] = None

class ReconcileRequest(BaseModel):
    source_a: List[Invoice]
    source_b: List[Invoice]

class ReconcileResult(BaseModel):
    matched: List[Invoice]
    unmatched_a: List[Invoice]
    unmatched_b: List[Invoice]
