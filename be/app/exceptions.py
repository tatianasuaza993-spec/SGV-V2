"""
Módulo: exceptions.py
Descripción: Excepciones de dominio, cada una con su código HTTP dentro de la clase.
¿Para qué? Que la capa de servicios exprese errores de negocio sin conocer HTTP.
¿Impacto? Sin esto, el código de estado se decidía buscando texto en el mensaje (hallazgo H16)
y cambiar una palabra cambiaba la respuesta.
"""


class DomainError(Exception):
    """Error de negocio base. Las subclases fijan `status_code` y `code`."""

    status_code: int = 400
    code: str = "domain_error"
    default_message: str = "Business rule violated"

    def __init__(self, message: str | None = None) -> None:
        self.message = message or self.default_message
        super().__init__(self.message)


class NotFoundError(DomainError):
    status_code = 404
    code = "not_found"
    default_message = "Resource not found"


class ForbiddenError(DomainError):
    status_code = 403
    code = "forbidden"
    default_message = "You are not allowed to perform this action"


class UnauthorizedError(DomainError):
    status_code = 401
    code = "unauthorized"
    default_message = "Invalid credentials"


class ConflictError(DomainError):
    status_code = 409
    code = "conflict"
    default_message = "The request conflicts with the current state"


class AlreadyVotedError(ConflictError):
    code = "already_voted"
    default_message = "You have already voted for this position"


class InvalidStateTransitionError(ConflictError):
    code = "invalid_state_transition"
    default_message = "That status change is not allowed"


class ValidationRuleError(DomainError):
    status_code = 422
    code = "validation_rule"
    default_message = "The data does not satisfy a business rule"
