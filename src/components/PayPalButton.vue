<script setup lang="ts">
import { onMounted } from 'vue';
import { loadScript } from "@paypal/paypal-js";
const PAYPAL_CLIENTID = import.meta.env.VITE_PAYPAL_CLIENTID;
const props = defineProps<{
  amount: string;
}>();

onMounted(async () => {
  const paypal = await loadScript({
    "client-id": PAYPAL_CLIENTID, // Replace with your PayPal client ID
    currency: "USD"
  });

  if (paypal) {
    paypal.Buttons({
      createOrder: (data: any, actions: any) => {
        return actions.order.create({
          purchase_units: [{
            amount: {
              value: props.amount
            }
          }]
        });
      },
      onApprove: async (data: any, actions: any) => {
        const order = await actions.order.capture();
        alert("Payment successful! Order ID: " + order.id);
      }
    }).render("#paypal-button-container");
  }
});
</script>

<template>
  <div id="paypal-button-container" class="w-full max-w-md mx-auto mt-4"></div>
</template>