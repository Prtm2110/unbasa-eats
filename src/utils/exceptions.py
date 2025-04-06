"""Custom exceptions for the unbasa-eats RAG Chatbot."""

class unbasa-eatsBotError(Exception):
    """Base exception for all unbasa-eats chatbot errors."""
    pass

class ScraperError(unbasa-eatsBotError):
    """Raised when there's an error in the web scraping process."""
    pass

class KnowledgeBaseError(unbasa-eatsBotError):
    """Raised when there's an error in the knowledge base operations."""
    pass

class RetrieverError(unbasa-eatsBotError):
    """Raised when there's an error in retrieving documents."""
    pass

class GeneratorError(unbasa-eatsBotError):
    """Raised when there's an error in generating responses."""
    pass

class ConfigError(unbasa-eatsBotError):
    """Raised when there's an error in configuration."""
    pass

class APIError(unbasa-eatsBotError):
    """Raised when there's an error in the API."""
    pass
