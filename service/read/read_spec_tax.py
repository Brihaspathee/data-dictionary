from sqlalchemy.orm import Session

from models.portico.V_SPEC_TAX import SpecTax
import logging

log = logging.getLogger(__name__)

SPEC_TAX: dict[str, dict[str, str]] = {}

def read_spec_tax(session: Session):
    """Load SpecTax view data into in-memory dictionary cache."""
    global SPEC_TAX
    cache: dict[str, dict[str, str]] = {}
    for row in session.query(SpecTax).all():
        cache[row.taxonomy] = {
            "spec_id": str(row.spec_id),
            "spec_ds": row.spec_ds
        }
    SPEC_TAX = cache
    log.debug(f"SpecTax cache populated:{SPEC_TAX}")
