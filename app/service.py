# FastAPI app - reconciliador
# Clean, minimal and suitable for CI / Docker / local dev.
from fastapi import FastAPI, HTTPException
from typing import List
import logging
from .schemas import ReconcileRequest, ReconcileResult, Invoice

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('reconciliador')

app = FastAPI(title="Reconciliador - Demo", version="0.1.0")


@app.get('/health', tags=['health'])
def health():
    """Health check endpoint."""
    return {"status": "ok"}


def _simple_reconcile(a: List[Invoice], b: List[Invoice]):
    """Simple reconciliation by invoice id. Returns matched and unmatched lists."""
    map_b = {inv.id: inv for inv in b}
    matched = []
    unmatched_a = []
    for inv in a:
        if inv.id in map_b:
            matched.append(inv)
        else:
            unmatched_a.append(inv)

    unmatched_b = [inv for inv in b if inv.id not in {x.id for x in a}]
    return matched, unmatched_a, unmatched_b


@app.post('/reconcile', response_model=ReconcileResult, tags=['reconcile'])
def reconcile(payload: ReconcileRequest):
    """Compare two invoice lists and return matches/unmatched.
    This is intentionally small and testable. Replace with domain rules as needed.
    """
    try:
        matched, unmatched_a, unmatched_b = _simple_reconcile(payload.source_a, payload.source_b)
        logger.info('reconciliation executed: matched=%d, unmatched_a=%d, unmatched_b=%d', len(matched), len(unmatched_a), len(unmatched_b))
        return ReconcileResult(matched=matched, unmatched_a=unmatched_a, unmatched_b=unmatched_b)
    except Exception as exc:
        logger.exception('Error while reconciling')
        raise HTTPException(status_code=500, detail=str(exc))
