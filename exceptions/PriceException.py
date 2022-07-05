class PriceException(Exception):
    def __init__(self, message):
        self.message = message # You can also set it by default so you don't need to input any message
        super().__init__(self.message)

    def __eq__(self, other):
        return self.message == other.message

    def __str__(self):
        return f'{self.message}' # In your case, just to display message.
        # return f'Error message: {self.message}'