from abc import ABC, abstractmethod

# 1. Interfaz, define el contrato para cualquier metodo de pago
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount: float):
        pass


# 2. Implementaciones Concretas, maneja pagos con paypal

class PayPalPayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Pagando ${amount} usando PayPal")

#maneja pagos con stripe 
class StripePayment(PaymentMethod):

    def pay(self, amount: float):
        print(f"Pagando ${amount} usando Stripe")


# 3. Clase de Alto Nivel, se encarga de procesar pahos~
#no sabe como se realizan
class PaymentProcessor:

    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process(self, amount: float):
        self.payment_method.pay(amount)


# --- Uso ---

paypal_processor = PaymentProcessor(PayPalPayment())
paypal_processor.process(100)

stripe_processor = PaymentProcessor(StripePayment())
stripe_processor.process(200)