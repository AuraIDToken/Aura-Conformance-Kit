"""
Aura TCK reference implementation exception hierarchy.

Organized by architectural layer:
    - ParsingError: JSON parsing, numeric type detection
    - ValidationError: EES model validation, type checking
    - CanonicalizationError: Canonical form generation (CSS)
    - OracleError: Oracle comparison and verification
    - TestVectorError: Test fixture validation
"""


class AuraError(Exception):
    """Base exception for all Aura TCK errors."""
    pass


# ============================================================================
# ParsingError
# ============================================================================


class ParsingError(AuraError):
    """Raised during parsing phase."""
    pass


class InvalidJSONError(ParsingError):
    """Raised when JSON parsing fails."""
    pass


class UnsupportedNumericTypeError(ParsingError):
    """Raised when unsupported numeric type (float, etc.) is encountered."""
    pass


# ============================================================================
# ValidationError
# ============================================================================


class ValidationError(AuraError):
    """Raised during EES model validation."""
    pass


class TypeValidationError(ValidationError):
    """Raised when type validation fails."""
    pass


class RequiredFieldError(ValidationError):
    """Raised when a required field is missing."""
    pass


class ValueConstraintError(ValidationError):
    """Raised when a value constraint is violated."""
    pass


class CryptographicTypeError(ValueConstraintError):
    """Raised when cryptographic type validation fails."""
    pass


class InvalidSHA256DigestError(CryptographicTypeError):
    """Raised when SHA256Digest validation fails."""
    pass


class InvalidPublicKeyError(CryptographicTypeError):
    """Raised when PublicKey validation fails."""
    pass


class InvalidSignatureError(CryptographicTypeError):
    """Raised when Signature validation fails."""
    pass


class InvalidKeyIdentifierError(CryptographicTypeError):
    """Raised when KeyIdentifier validation fails."""
    pass


# ============================================================================
# CanonicalizationError
# ============================================================================


class CanonicalizationError(AuraError):
    """Raised during canonical form generation (CSS)."""
    pass


class CanonicalOrderingError(CanonicalizationError):
    """Raised when canonical ordering fails."""
    pass


class CanonicalEncodingError(CanonicalizationError):
    """Raised when canonical encoding fails."""
    pass


class DeterminismError(CanonicalizationError):
    """Raised when determinism check fails."""
    pass


# ============================================================================
# OracleError
# ============================================================================


class OracleError(AuraError):
    """Raised during Oracle comparison."""
    pass


class OracleMismatchError(OracleError):
    """Raised when Oracle comparison mismatches."""
    pass


class OracleVersionMismatchError(OracleError):
    """Raised when Oracle version mismatches."""
    pass


class OracleSignatureError(OracleError):
    """Raised when Oracle signature verification fails."""
    pass


# ============================================================================
# TestVectorError
# ============================================================================


class TestVectorError(AuraError):
    """Raised during test vector processing."""
    pass


class TestVectorFormatError(TestVectorError):
    """Raised when test vector format is invalid."""
    pass


class TestVectorExpectationError(TestVectorError):
    """Raised when test vector expectation is not met."""
    pass


__all__ = [
    "AuraError",
    "ParsingError",
    "InvalidJSONError",
    "UnsupportedNumericTypeError",
    "ValidationError",
    "TypeValidationError",
    "RequiredFieldError",
    "ValueConstraintError",
    "CryptographicTypeError",
    "InvalidSHA256DigestError",
    "InvalidPublicKeyError",
    "InvalidSignatureError",
    "InvalidKeyIdentifierError",
    "CanonicalizationError",
    "CanonicalOrderingError",
    "CanonicalEncodingError",
    "DeterminismError",
    "OracleError",
    "OracleMismatchError",
    "OracleVersionMismatchError",
    "OracleSignatureError",
    "TestVectorError",
    "TestVectorFormatError",
    "TestVectorExpectationError",
]
