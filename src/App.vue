<script setup lang="ts">
import PayPalButton from './components/PayPalButton.vue';
import { loadScript } from "@paypal/paypal-js";
import { onMounted, ref, watch } from 'vue';
const email = ref('');
const showPreorder = ref(false);

const handleWaitlist = async () => {
  try {
    const response = await fetch('https://pryzmat.pl/waitlist', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        email: email.value,
        sku: 'emp',
        to: 'pryzmat@pryzmat.pl'
      })
    });
    
    if (response.ok) {
      alert('Successfully joined the waitlist!');
      email.value = '';
    }
  } catch (error) {
    console.error('Error:', error);
    alert('Failed to join waitlist. Please try again.');
  }
};

const PAYPAL_CLIENTID = import.meta.env.VITE_PAYPAL_CLIENTID;
const selectedDevice = ref('toyDevice');
const price = ref('249.99');
const shippingInfo = ref('Shipping end of Jun\'25');

watch(selectedDevice, (newDevice) => {
  if (newDevice === 'toyDevice') {
    price.value = '249.99';
    shippingInfo.value = "Shipping end of Jun'25";
  } else if (newDevice === 'hvDevice') {
    price.value = '2649.99';
    shippingInfo.value = "Shipping end of August'25";
  }
});

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
              value: price.value
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
  <div class="min-h-screen bg-gray-900 py-12 px-4 sm:px-6 lg:px-8">
    <div class="max-w-7xl mx-auto">
      <!-- Hero Section -->
      <div class="text-center mb-16">
        <h1 class="text-5xl font-bold text-copper mb-4">
          The Aether Disruptor
        </h1>
        <p class="text-xl text-brass mb-8">
          A <b>Steampunk Marvel</b> available as either a <b>Toy</b> or <b>Robot Disruptor</b>
        </p>
      </div>

      <!-- Main Image -->
      <div class="steampunk-border mb-16">
        <img 
          src="/emp-device.jpg" 
          alt="Steampunk Quantum Disruptor Toy" 
          class="w-full max-w-3xl mx-auto rounded-lg shadow-2xl"
        />
      </div>

      <!-- Features -->
      <div class="grid md:grid-cols-3 gap-8 mb-16">
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Handcrafted</h3>
          <p>Each piece is carefully assembled with premium materials</p>
        </div>
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Interactive</h3>
          <p>Working lights and mechanical sounds in the Kids package</p>
        </div>
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Robot Destroyer</h3>
          <p>An actual EMP tool in the Technologists package</p>
        </div>
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Shipping - June 2025</h3>
          <p>First Technologists package shipping starting June'25</p>
        </div>
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Educational</h3>
          <p>Learn about electronics and steampunk aesthetics</p>
        </div>
        <div class="steampunk-border text-center">
          <h3 class="text-xl font-bold text-copper mb-2">Open Source</h3>
          <p>Pre-orders are funding the OSS github project for the Kids package</p>
        </div>
      </div>

      <!-- Waitlist Form -->
      <div class="steampunk-border max-w-2xl mx-auto mb-16">
        <h2 class="text-3xl font-bold text-copper mb-4 text-center">
          Join the Waitlist
        </h2>
        <form @submit.prevent="handleWaitlist" class="space-y-4">
          <div>
            <input
              v-model="email"
              type="email"
              required
              placeholder="Enter your email"
              class="w-full px-4 py-2 bg-gray-800 border-2 border-brass rounded-lg focus:outline-none focus:border-copper"
            />
          </div>
          <button type="submit" class="btn-primary w-full">
            Reserve Your Spot
          </button>
        </form>
      </div>

      <div class="steampunk-border max-w-2xl mx-auto">
    <h2 class="text-3xl font-bold text-copper mb-4 text-center">
      Pre-order Now
    </h2>
    <div class="text-center mb-4">
      <label for="device-select" class="font-bold mr-2">Choose your device:</label>
      <select 
        id="device-select" 
        v-model="selectedDevice" 
        class="border p-2 rounded-md text-black"
      >
        <option value="toyDevice">Toy Device</option>
        <option value="hvDevice">HV Device</option>
      </select>
    </div>

    <p class="text-center mb-4">
      <span v-if="selectedDevice === 'toyDevice'">
        Limited first batch available at special price: <b>$249.99</b>. Shipping end of Jun'25.
      </span>
      <span v-if="selectedDevice === 'hvDevice'">
        Limited first batch available at special price: <b>$2649.99</b>. Shipping end of August'25.
      </span>
    </p>

    <div id="paypal-button-container" class="w-full max-w-md mx-auto mt-4"></div>
  </div>
  </div>
</div>
</template>