class Gateway(object):
    def purchase(self, amount, card, options=None):
        """One go authorize and capture transaction"""
        raise NotImplementedError

    def authorize(self, amount, card, options=None):
        """Authorization for a future capture transaction"""
        raise NotImplementedError

    def capture(self, amount, card, options=None):
        """Capture funds from a previously authorized transaction"""
        raise NotImplementedError

    def void(self, identification, options=None):
        """Null/Blank/Delete a previous transaction"""
        raise NotImplementedError

    def refund(self, amount, id, options=None):
        """Refund a transaction"""
        raise NotImplementedError

    def recurring(self, money, creditcard, options=None):
        """Setup a recurring transaction"""
        raise NotImplementedError

    def store(self, creditcard, options=None):
        """Store the credit card and user profile information
        on the gateway for future use"""
        raise NotImplementedError

    def unstore(self, identification, options=None):
        """Delete the previously stored credit card and user
        profile information on the gateway"""
        raise NotImplementedError
