<script setup lang="ts">
import { ref } from 'vue';
import PayPalButton from './components/PayPalButton.vue';

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
          A <b>Steampunk Marvel</b> available as either a <b>toy</b> or <b>robot disruptor</b>
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

      <!-- Pre-order Section -->
      <div class="steampunk-border max-w-2xl mx-auto">
        <h2 class="text-3xl font-bold text-copper mb-4 text-center">
          Pre-order Now (Toy Device). Shipping end of Jun'25
        </h2>
        <p class="text-center mb-4">
          Limited first batch available at special price: $249.99
        </p>
        <PayPalButton amount="249.99" />
      </div>
      
      <!-- Pre-order Section -->
      <div class="steampunk-border max-w-2xl mx-auto">
        <h2 class="text-3xl font-bold text-copper mb-4 text-center">
          Pre-order Now (HV Device). Shipping end of August'25
        </h2>
        <p class="text-center mb-4">
          Limited first batch available at special price: $2649.99
        </p>
        <PayPalButton amount="1649.99" />
      </div>
    </div>
  </div>
</template>