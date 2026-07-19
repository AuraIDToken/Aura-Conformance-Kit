"""Shared requirement types for Aura Conformance Kit.

This module contains only Enum definitions used across the project to
represent compliance status, conformance layers and verification results.

Contract: CONTRACT-004
"""

from enum import Enum


class ComplianceStatus(Enum):
    """Outcome of a single requirement verification."""

    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"
    NOT_APPLICABLE = "not_applicable"
    NOT_IMPLEMENTED = "not_implemented"


class ConformanceLayer(Enum):
    """Logical layer of the conformance test or requirement."""

    PARSER = "parser"
    CANONICALIZATION = "canonicalization"
    SERIALIZATION = "serialization"
    CRYPTOGRAPHY = "cryptography"
    MERKLE = "merkle"
    ORACLE = "oracle"
    TCK = "tck"


class VerificationResult(Enum):
    """Higher-level result of a verification action."""

    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"
