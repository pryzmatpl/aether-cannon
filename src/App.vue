<script setup lang="ts">
import { ref, watch } from 'vue';
const email = ref('');
const currentImage = ref(0);

const imageData = [
  { src: 'public/emp-device-1.jpg', alt: 'Steampunk Quantum Disruptor Toy 1', description: 'A handheld toy for young explorers to learn basics of electronics! Coming with a set of knowledge to learn and have fun while building the device!' },
  { src: 'public/emp-device-2.jpg', alt: 'Steampunk Quantum Disruptor Toy 2', description: 'The Technologists version is a dangerous device for adults and will be sold to engineers only. It will be an open-source project with the license explicitly stating responsiblity. This is not a toy. This is a costly, dangerous device for responsible people.' },
  { src: 'public/emp-device-3.jpg', alt: 'Steampunk Quantum Disruptor Toy 3', description: 'Coming along with the Toy package, you will also be able to obtain a kid toy robot to have fun with!' }
];

const prevImage = () => {
  currentImage.value = (currentImage.value === 0) ? imageData.length - 1 : currentImage.value - 1;
};

const nextImage = () => {
  currentImage.value = (currentImage.value === imageData.length - 1) ? 0 : currentImage.value + 1;
};


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
      <!-- Carousel Section -->
      <div class="steampunk-border mb-16">
        <div class="relative">
          <!-- Carousel Images -->
          <img 
            :src="imageData[currentImage].src"
            :alt="imageData[currentImage].alt"
            class="w-full max-w-3xl mx-auto rounded-lg shadow-2xl"
          />
          
          <!-- Description Below Image -->
          <p class="text-center mt-4 font-bold text-lg text-copper">
            {{ imageData[currentImage].description }}
          </p>

    <!-- Navigation Buttons -->
    <div class="absolute top-1/2 left-4 transform -translate-y-1/2">
      <button @click="prevImage" class="bg-black text-white px-3 py-2 rounded-full">&lt;</button>
    </div>
    <div class="absolute top-1/2 right-4 transform -translate-y-1/2">
      <button @click="nextImage" class="bg-black text-white px-3 py-2 rounded-full">&gt;</button>
    </div>
  </div>
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
        Limited first batch available at a special price: <b>$249.99</b>. Shipping end of Jun'25.
      </span>
      <span v-if="selectedDevice === 'hvDevice'">
        Limited first batch available at a special price: <b>$2649.99</b>. Shipping end of August'25. <p class="text-red">Rights reseved to ship 1 month later.</p>
      </span>
    </p>

    <div id="paypal-button-container" class="w-full max-w-md mx-auto mt-4"></div>
  </div>
  </div>
</div>
</template>