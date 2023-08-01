class ValidationError(Exception):
    pass


class DiscordAPIError(Exception):
    def __init__(self, code: int, message: str, errors: list):
        super(DiscordAPIError, self).__init__(
            f"A request to the Discord API was unsuccessful (Status code: {code}). {message}"
        )
        self.code = code
        self.message = message
        self.errors = errors
