const defaultUrlHint = {
  en: 'In case the button does not work, copy and paste the following url into your browser',
  es: 'En caso el boton no funcione, copia y pega el siguiente enlace en tu navegador'
}

export default {
  en: {
    'orderPaid.title': 'Order placed',
    'orderPaid.text': 'Your order has been placed successfully, when a traveler picks your order we will immediately notify you.',
    'orderPaid.step': 'Step 1: Looking for travelers',
    'orderPaid.button': 'See purchase tracking',
    'orderPaid.hint': defaultUrlHint.en
  },
  es: {
    'orderPaid.title': 'Pedido Realizado',
    'orderPaid.text': 'Tu compra ha sido realizada con exito, cuando un viajero este dispuesto a traer tus pedidos te notificaremos.',
    'orderPaid.step': 'Paso 1: Buscando viajero',
    'orderPaid.button': 'Ver seguimiento de pedido',
    'orderPaid.hint': defaultUrlHint.es
  }
}
