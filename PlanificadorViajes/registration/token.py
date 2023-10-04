from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six 

class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return(
            six.text_type(user.pk) + six.text_type(timestamp) + six.text_type(user.is_active)
        )
        
class AccountActivationTokenGeneratorViaje(PasswordResetTokenGenerator):
    def _make_hash_value(self, viaje, timestamp):
        return(
            six.text_type(viaje.pk) + six.text_type(timestamp)
        )

account_activation_token = AccountActivationTokenGenerator()
account_activation_token_viaje = AccountActivationTokenGeneratorViaje()

