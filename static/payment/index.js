var stripe = Stripe('pk_test_51JO7QyCuKlRfgeZf28g9geKmcCdOPECFIlglgl8fjK1DdzUpaDC85ORft2U1uJ5xlit98NDLf8ROT9z2orlhldMP000S6AzlJz')

var elem = document.getElementById('submit');
clientsecret = elem.getAttribute('data-secret');

var elements = stripe.elements();
var style = {
    base: {
        color: "#000",
        lineHeight: '2.4',
        fontSize: '16px',
    }
};
var card = elements.create("card", {style: style});
card.mount("#card-element");

card.on('change', function(event) {
var displayError = document.getElementById('card-errors')
if (event.error) {
  displayError.textContent = event.error.message;
  $('#card-errors').addClass('alert alert-info');
} else {
  displayError.textContent = '';
  $('#card-errors').removeClass('alert alert-info');
}
});

var form = document.getElementById('payment-form');

form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    
    var custName = document.getElementById("custName").value;
    var custTown = document.getElementById("custTown").value;
    var custAdd = document.getElementById("custAdd").value;
    var custAdd2 = document.getElementById("custAdd2").value;
    var custCode = document.getElementById("postCode").value;

    stripe.confirmCardPayment(clientsecret, {
        payment_method: {
            card: card,
            billing_details: {
                address: {
                    postal_code: custCode,
                    city: custTown,
                    line1: custAdd,
                    line2: custAdd2,
                },
                name: custName
            },
        }
    }).then(function(result) {
        if (result.error) {
          console.log('payment error')
          console.log(result.error.message);
        } else {
          if (result.paymentIntent.status === 'succeeded') {
            console.log('payment processed')
            // There's a risk of the customer closing the window before callback
            // execution. Set up a webhook or plugin to listen for the
            // payment_intent.succeeded event that handles any business critical
            // post-payment actions.
            window.location.replace("http://127.0.0.1:8000/payment/orderplaced/");
          }
        }
    });
});