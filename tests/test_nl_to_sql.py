"""Test NL to SQL."""
import pytest
from src.query.nl_to_sql import NLToSQL

def test_query():
    engine = NLToSQL("test://")
    results = engine.query("test")
    assert len(results) > 0
